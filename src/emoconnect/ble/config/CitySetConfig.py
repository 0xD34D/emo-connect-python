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
import json
from emoconnect import EmoConstants
from emoconnect.ble.config.BaseConfig import BaseConfig


@dataclass
class CitySetConfig(BaseConfig):
    name: str
    country: str = ""
    state: str = ""
    id: int = 0
    lat: float = 0.0
    lon: float = 0.0

    def toJson(self) -> str:
        return json.dumps(
            {
                'type': EmoConstants.BLE_CITY_SET,
                'data': {
                    'name': self.name,
                    'country': self.country,
                    'state': self.state,
                    'id': self.id,
                    'coord': {
                        'lat': self.lat,
                        'lon': self.lon,
                    }
                }
            }
        )
