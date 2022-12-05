#
# This file is part of emo-connect-python (https://github.com/0xD34D/emo-connect-python).
# Copyright (c) 2022 Clark Scheff.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
from typing import (
    Any,
    Dict,
    Optional,
    Union,
)
import asyncio
import json
import logging
from enum import IntEnum
from bleak import (
    AdvertisementData,
    BleakClient,
    BleakGATTCharacteristic,
    BleakScanner,
    BLEDevice,
)
from emoconnect import EmoConstants

logger = logging.getLogger()


class EmoConnectManagerException(Exception):
    ...


class PacketType(IntEnum):
    Response = 0
    Command = 1


class EmoConnectManager:
    _client: Optional[BleakClient]
    _emo: Optional[BLEDevice]
    _to_emo_char: Optional[BleakGATTCharacteristic]
    _packet: bytearray
    _packet_size: int
    _packet_type: PacketType
    _sending_request: bool
    _resonse: Optional[Dict[str, Any]]

    def __init__(self):
        self._client = None
        self._emo = None
        self._sending_request = False

    async def connectToEmo(self) -> bool:
        async def _handle_rx(_: BleakGATTCharacteristic, data: bytearray):
            logger.debug(f'client <-- emo: {data}')
            if data[0] == 0xbb and data[1] == 0xaa:
                self._packet_size = int.from_bytes(
                    data[2:4], byteorder='little')
                self._packet = data[4:len(data)]
                self._packet_type = PacketType.Response
                logger.debug(
                    f'New packet of size {self._packet_size} started ')
            elif data[0] == 0xdd and data[1] == 0xcc:
                self._packet_size = 17
                self._packet = data[3:len(data)]
                self._packet_type = PacketType.Command
                logger.debug('New command packet started')
            elif len(self._packet) < self._packet_size:
                self._packet += data

            if len(self._packet) >= self._packet_size:
                if self._packet_type == PacketType.Response:
                    s = self._packet.decode('utf-8')
                    self._resonse = json.loads(s)
                else:
                    logger.info(f'received command packet: {self._packet}')

        if self._client is not None and self._client.is_connected:
            raise EmoConnectManagerException(f'Already connected {self._emo}.')

        def match_write_uuid(_: BLEDevice, adv: AdvertisementData):
            if EmoConstants.SERVICE_UUID.lower() in adv.service_uuids:
                return True

            return False

        self._emo = await BleakScanner.find_device_by_filter(match_write_uuid)
        if self._emo is not None:
            self._client = BleakClient(self._emo)
            await self._client.connect()
            await self._client.start_notify(EmoConstants.NOTIFY_UUID,
                                            _handle_rx)
            emo_service = self._client.services.get_service(
                EmoConstants.SERVICE_UUID)
            self._to_emo_char = emo_service.get_characteristic(
                EmoConstants.WRITE_UUID)
            return True

        return False

    async def disconnect(self) -> bool:
        if self._client is not None:
            if not self._client.is_connected:
                raise EmoConnectManagerException(
                    'Not connected to EMO.')
            return await self._client.disconnect()
        return False

    async def sendRequest(self,
                          request: Union[bytes, bytearray]) -> Optional[Dict[str, Any]]:
        if self._client is None or not self._client.is_connected:
            raise EmoConnectManagerException(
                'Cannot send request, EMO is not connected')

        logger.info(f'client->emo: {request}')

        self._resonse = None
        await self._client.write_gatt_char(self._to_emo_char, request)

        while self._resonse is None:
            await asyncio.sleep(0.25)

        logger.info(f'emo->client: {self._resonse}')
        return self._resonse

    async def sendCommand(self,
                          command: Union[bytes, bytearray]):
        if self._client is None or not self._client.is_connected:
            raise EmoConnectManagerException(
                'Cannot send command, EMO is not connected')

        logger.info(f'client->emo: {command}')

        await self._client.write_gatt_char(self._to_emo_char, command)
