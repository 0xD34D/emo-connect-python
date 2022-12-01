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
from emoconnect.ble.config.AnimationConfig import Op, AnimationConfig

DANCE_LIST = [
    'd1_EmoDance',
    'd2_WontLetGo',
    'd3_Blindless',
    'd4_Click1',
    'd5_TimeOfMyLife',
    'd6_Rollercoaster',
    'd7_FlashBack',
    'd8_Click2',
    'd9_BlameYourself',
    'd10_CanITakeYouThere',
    'd11_OceanBlue',
]


def enterAnimationMode() -> bytes:
    return _request(Op.IN)


def exitAnimationMode() -> bytes:
    return _request(Op.OUT)


def playEmoDance(dance_num: int) -> bytes:
    return _request(Op.PLAY, DANCE_LIST[dance_num])


def _request(op: Op, name: str = None) -> bytes:
    config: AnimationConfig = AnimationConfig(op=op, name=name)
    return config.getRequest()
