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
from dataclasses import dataclass
from enum import IntEnum


class Status(IntEnum):
    BEING_SHAKEN = 10
    BEING_PETTED = 20
    PICKED_UP = 31
    FALLS_DOWN = 32
    CHARGING = 33
    PUT_DOWN = 34
    EMERGING_FROM_CLIFF = 40
    HEADSET_CHANGE = 51
    LOW_POWER = 52
    OBSTACLE_DETECTED = 61
    SOUND_DETECTED = 62
    PLAYING_GAMES = 90
    HAVING_FUN = 100
    LISTENING = 110
    SPEAKING = 120
    PLAYING_MUSIC = 130
    DANCING = 140
    BEING_HELPFUL = 150
    MOVING = 160
    LISTENING_CHATGPT = 170
    ANSWERING_QUESTIONS = 180
    MOVING_TO_TARGET = 190
    LOOKING_AT_FACE = 200
    LOOKING_AT_FACE2 = 210
    SEES_NON_HUMAN = 220
    STAYING = 230
    SLEEPING = 240
    REMOVED_FROM_CHARGER = 260
    LOOKING_AROUND = 270
    BEING_HAPPY = 281
    BEING_SAD = 282
    EXPLORING = 290
    SEARCHING = 300
    PLAYING = 310


@dataclass
class StatusAlert:
    status: Status
