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
from emoconnect.ble.config.StateConfig import State, StateConfig


def deviceid() -> bytes:
    return _request([State.DEVICEID])


def version() -> bytes:
    return _request([State.VERSION])


def network() -> bytes:
    return _request([State.NETWORK])


def xiaoai() -> bytes:
    return _request([State.XIAOAI])


def alexa() -> bytes:
    return _request([State.ALEXA])


def light() -> bytes:
    return _request([State.LIGHT])


def alarm() -> bytes:
    return _request([State.ALARM])


def city() -> bytes:
    return _request([State.CITY])


def timezone() -> bytes:
    return _request([State.TIMEZONE])


def achievements() -> bytes:
    return _request([State.ACHIEVEMENTS])


def preference() -> bytes:
    return _request([State.PREFERENCE])


def versionAndPersonality() -> bytes:
    return _request([State.PERSONALITY, 1])


def personality() -> bytes:
    return _request([State.PERSONALITY])


def dancelist() -> bytes:
    return _request([State.DANCE_LIST])


def everything() -> bytes:
    return _request([
        State.DEVICEID,
        State.VERSION,
        State.NETWORK,
        State.XIAOAI,
        State.ALEXA,
        State.LIGHT,
        State.ALARM,
        State.CITY,
        State.TIMEZONE,
        State.ACHIEVEMENTS,
        State.DANCE_LIST,
        State.PERSONALITY,
        State.PREFERENCE,
    ])


def _request(data: list[int]) -> bytes:
    config: StateConfig = StateConfig(
        data=data)
    return config.getRequest()
