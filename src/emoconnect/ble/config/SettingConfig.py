
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
from emoconnect import EmoConstants
from emoconnect.ble.config.BaseConfig import BaseConfig
from enum import Enum
import json


class Op(Enum):
    IN = 'in'
    OUT = 'out'
    # auto update settings
    AUTO_UPDATE_ON = 'auto_update_on'
    AUTO_UPDATE_OFF = 'auto_update_off'
    # length settings
    LENGTH_METRIC = 'length_metric'
    LENGTH_IMPERIAL = 'length_imperial'
    # schedule settings
    SCHEDULE_ON = 'schedule_on'
    SCHEDULE_OFF = 'schedule_off'
    # schedule sound settings
    SCHEDULE_SOUND_ON = 'schedule_s_on'
    SCHEDULE_SOUND_OFF = 'schedule_s_off'
    # temperature settings
    TEMP_CELSIUS = 'temp_c'
    TEMP_FARENHEIT = 'temp_f'
    # volume settings
    VOLUME_MUTE = 'volume_mute'
    VOLUME_LOW = 'volume_low'
    VOLUME_MED = 'volume_med'
    VOLUME_HIGH = 'volume_high'


@dataclass
class SettingConfig(BaseConfig):
    data: Op

    def toJson(self) -> str:
        return json.dumps(
            {
                'data': {'op': self.data.value},
                'type': EmoConstants.BLE_SETTING_REQ
            }
        )
