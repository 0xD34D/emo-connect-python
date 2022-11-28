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
from emoconnect import EmoConstants
from emoconnect.ble.config.RequestConfig import RequestConfig
from emoconnect.util.ByteUtil import encodePayload
from functools import cache


def request(data: list[int]) -> bytes:
    config: RequestConfig = RequestConfig(
        data=data, requestType=EmoConstants.BLE_STA_REQ)
    return encodePayload(config.toJson())


@cache
def deviceid() -> bytes:
    return request([EmoConstants.BLE_STATE_DEVICEID])


@cache
def version() -> bytes:
    return request([EmoConstants.BLE_STATE_VERSION])


@cache
def network() -> bytes:
    return request([EmoConstants.BLE_STATE_NETWORK])


@cache
def xiaoai() -> bytes:
    return request([EmoConstants.BLE_STATE_XIAOAI])


@cache
def alexa() -> bytes:
    return request([EmoConstants.BLE_STATE_ALEXA])


@cache
def light() -> bytes:
    return request([EmoConstants.BLE_STATE_LIGHT])


@cache
def alarm() -> bytes:
    return request([EmoConstants.BLE_STATE_ALARM])


@cache
def city() -> bytes:
    return request([EmoConstants.BLE_STATE_CITY])


@cache
def timezone() -> bytes:
    return request([EmoConstants.BLE_STATE_TIMEZONE])


@cache
def achievements() -> bytes:
    return request([EmoConstants.BLE_STATE_ACHIEVEMENTS])


@cache
def preference() -> bytes:
    return request([EmoConstants.BLE_STATE_PREFERENCE])


@cache
def versionAndPersonality() -> bytes:
    return request([EmoConstants.BLE_STATE_PERSONALITY, 1])


@cache
def personality() -> bytes:
    return request([EmoConstants.BLE_STATE_PERSONALITY])


@cache
def dancelist() -> bytes:
    return request([EmoConstants.BLE_STATE_DANCE_LIST])
