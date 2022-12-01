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
from emoconnect.ble.config.SettingConfig import Op, SettingConfig


def enterSettingMode() -> bytes:
    return _request(Op.IN)


def exitSettingMode() -> bytes:
    return _request(Op.OUT)


def setAutoUpdate(on: bool) -> bytes:
    return _request(Op.AUTO_UPDATE_ON if on else Op.AUTO_UPDATE_OFF)


def setLength(useMetric: bool) -> bytes:
    return _request(Op.LENGTH_METRIC if useMetric else Op.LENGTH_IMPERIAL)


def setTemp(useCelsius: bool) -> bytes:
    return _request(Op.TEMP_CELSIUS if useCelsius else Op.TEMP_FARENHEIT)


def setSchedule(on: bool) -> bytes:
    return _request(Op.SCHEDULE_ON if on else Op.SCHEDULE_OFF)


def setScheduleSound(on: bool) -> bytes:
    return _request(Op.SCHEDULE_SOUND_ON if on else Op.SCHEDULE_SOUND_OFF)


def setVolumeMute() -> bytes:
    return _request(Op.VOLUME_MUTE)


def setVolumeLow() -> bytes:
    return _request(Op.VOLUME_LOW)


def setVolumeMedium() -> bytes:
    return _request(Op.VOLUME_MED)


def setVolumeHigh() -> bytes:
    return _request(Op.VOLUME_HIGH)


def _request(data: Op) -> bytes:
    config: SettingConfig = SettingConfig(
        data=data)
    return config.getRequest()
