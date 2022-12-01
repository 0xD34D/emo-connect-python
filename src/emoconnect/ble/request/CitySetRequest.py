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
from emoconnect.ble.config.CitySetConfig import CitySetConfig


def setLocation(
        name: str,
        country: str = '',
        state: str = '',
        id: int = 0,
        lat: float = 0.0,
        lon: float = 0.0) -> bytes:
    return _request(
        name=name,
        country=country,
        state=state,
        id=id,
        lat=lat,
        lon=lon)


def _request(
        name: str,
        country: str = '',
        state: str = '',
        id: int = 0,
        lat: float = 0.0,
        lon: float = 0.0) -> bytes:
    config: CitySetConfig = CitySetConfig(
        name=name,
        country=country,
        state=state,
        id=id,
        lat=lat,
        lon=lon)
    return config.getRequest()
