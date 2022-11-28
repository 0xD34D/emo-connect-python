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
from bleak import (
    AdvertisementData,
    BleakClient,
    BleakGATTCharacteristic,
    BleakScanner,
    BLEDevice,
)
from typing import (
    Any,
    Awaitable, 
    Callable, 
    Dict, 
    Optional, 
    Union,
)
from emoconnect import EmoConstants
import inspect
import logging

logger = logging.getLogger()

class EmoConnectManager:
    _client: Optional[BleakClient]
    _emo: Optional[BLEDevice]
    _to_emo_char: Optional[BleakGATTCharacteristic]
    _packet: bytearray
    _packet_size: int
    _callback: Callable[[Union[None, str]], Union[None, Awaitable[None]]]

    def __init__(self, callback: Callable[
        [Union[None, str]], Union[None, Awaitable[None]]
    ]):
        self._client = None
        self._emo = None
        self._callback = callback

    async def connectToEmo(self) -> bool:
        async def _handle_rx(_: BleakGATTCharacteristic, data: bytearray):
            if data[0] == 0xbb and data[1] == 0xaa:
                self._packet_size = int.from_bytes(
                    data[2:4], byteorder='little')
                self._packet = data[4:len(data)]
                logger.info(f'New packet of size {self._packet_size} started ')
            elif len(self._packet) < self._packet_size:
                self._packet += data

            if len(self._packet) >= self._packet_size:
                s = self._packet.decode('utf-8')
                if inspect.iscoroutinefunction(self._callback):
                    await self._callback(s)
                else:
                    self._callback(s)

        if self._client is not None and self._client.is_connected:
            raise EmoConnectManagerException(f'Already connected {self._emo}.')

        def match_write_uuid(device: BLEDevice, adv: AdvertisementData):
            if EmoConstants.SERVICE_UUID.lower() in adv.service_uuids:
                return True

            return False

        self._emo = await BleakScanner.find_device_by_filter(match_write_uuid)
        if self._emo is not None:
            self._client = BleakClient(self._emo)
            await self._client.connect()
            await self._client.start_notify(EmoConstants.NOTIFY_UUID, _handle_rx)
            emoService = self._client.services.get_service(
                EmoConstants.SERVICE_UUID)
            self._toEmoChar = emoService.get_characteristic(
                EmoConstants.WRITE_UUID)
            return True

        return False

    async def disconnect(self) -> bool:
        if self._client is not None:
            if not self._client.is_connected:
                raise EmoConnectManagerException(
                    f'Not connected to EMO.')
            return await self._client.disconnect()
        return False

    async def sendRequest(self, request: Union[bytes, bytearray]):
        if self._client is None or not self._client.is_connected:
            raise EmoConnectManagerException(
                'Cannot send request, EMO is not connected')

        logger.info(f'Sending request: {request}')
        await self._client.write_gatt_char(self._toEmoChar, request)

    class EmoConnectManagerException(Exception):
        ...
