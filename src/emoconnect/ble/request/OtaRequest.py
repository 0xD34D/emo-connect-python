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
from emoconnect.ble.config.OtaConfig import OtaConfig


def setVersion(versionNum: int) -> bytes:
    return _request(versionNum)


def _request(versionNum: int) -> bytes:
    config: OtatConfig = OtaConfig(
        versionNum=versionNum)
    return config.getRequest()
