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
CMD_CATEGORY = [0, 1, 2, 3, 4, 5]
CMD_ORDER = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
CMD_ORDER_DATA = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
CMD_GAME_NUMBER = [1, 2, 3, 4, 5, 6, 7]
SEQ = 1


def cmd(data: list[int], sequential: bool = True) -> bytes:
    global SEQ
    payload = bytes([0xDD, 0xCC, SEQ if sequential else 0]) + bytes(data) + \
        bytes([0])*(17 - len(data))
    if sequential:
        SEQ += 1
        if SEQ >= 255:
            SEQ = 1
    return payload


def cmd_debug(command: int) -> bytes:
    global SEQ
    payload = bytes([0x55, 0xAA, 0x55, 0xAA, 0x33, (command & 0xFF)]) + \
        bytes([0])*13 + bytes([0xED])
    return payload


def clear() -> bytes:
    return cmd([])


def statusOnOff(on: bool) -> bytes:
    return cmd([0, 0, 1 if on else 0])


def chargeLevelOnOff(on: bool) -> bytes:
    return cmd([2, 0, 1 if on else 0])


def enterApp(appId: int) -> bytes:
    return cmd([3, 2, appId])


def exitApp() -> bytes:
    return cmd([3, 1])


def forward() -> bytes:
    return cmd([3, 4, 5], sequential=False)


def back() -> bytes:
    return cmd([3, 4, 6], sequential=False)


def left() -> bytes:
    return cmd([3, 4, 7], sequential=False)


def right() -> bytes:
    return cmd([3, 4, 8], sequential=False)


def stop() -> bytes:
    return cmd([3, 4, 9], sequential=False)


def startGame() -> bytes:
    return cmd([3, 4, 1])


def resetting() -> bytes:
    return cmd([3, 5, 7], sequential=False)


def timeout() -> bytes:
    return cmd([3, 5, 8], sequential=False)


def debugEnterTestMode() -> bytes:
    return cmd_debug(19)


def debugMicArrayTest() -> bytes:
    return cmd_debug(20)


def debugCameraTest() -> bytes:
    return cmd_debug(21)


def debugDistanceSensorTest() -> bytes:
    return cmd_debug(22)


def debugCliffSensorTest() -> bytes:
    return cmd_debug(23)


def debugTouchSensorsTest() -> bytes:
    return cmd_debug(24)


def debugImuAndCompassTest() -> bytes:
    return cmd_debug(25)


def debugExitTestMode() -> bytes:
    return cmd_debug(26)


def debug_cmd_27() -> bytes:
    return cmd_debug(27)
