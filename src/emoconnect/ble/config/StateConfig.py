
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
from dataclasses import dataclass
from enum import IntEnum
from emoconnect import EmoConstants
from emoconnect.ble.config.BaseConfig import BaseConfig
import json


class State(IntEnum):
    DEVICEID = 0,
    VERSION = 1,
    NETWORK = 2,
    XIAOAI = 3,
    ALEXA = 4,
    LIGHT = 5,
    ALARM = 6,
    CITY = 7,
    TIMEZONE = 8,
    ACHIEVEMENTS = 9,
    DANCE_LIST = 10,
    PERSONALITY = 11,
    PREFERENCE = 12,


@dataclass
class StateConfig(BaseConfig):
    # data is a list of states being requested
    data: list[int]

    def toJson(self) -> str:
        return json.dumps(
            {
                'data': {'request': self.data},
                'type': EmoConstants.BLE_STA_REQ
            }
        )
