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
from emoconnect.ble.config.TimezoneSetConfig import TimezoneSetConfig


def setTimezone(
        name: str,
        code: str = '',
        offset: int = 0) -> bytes:
    return _request(
        name=name,
        code=code,
        offset=offset)


def _request(
        name: str,
        code: str = '',
        offset: int = 0) -> bytes:
    config: TimezoneSetConfig = TimezoneSetConfig(
        name=name,
        code=code,
        offset=offset)
    return config.getRequest()
