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
from emoconnect.ble.command.ChargeStatus import ChargeStatus
from emoconnect.ble.command.HuntResponse import HuntResponse
from emoconnect.ble.command.StatusAlert import Status, StatusAlert


class CommandParser:
    def parse(self, payload: bytes):
        if payload[0] == 2 and payload[1] == 0:
            return ChargeStatus(int(payload[2]))
        elif payload[0] == 0 and payload[1] == 0:
            return StatusAlert(Status(int(f'{payload[2]}{payload[3]}')))
        elif payload[0] == 3 and payload[1] == 5:
            return HuntResponse(status=int(payload[2]), sub_status=int(payload[3]))
        else:
            return None
