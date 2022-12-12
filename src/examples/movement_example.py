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
import asyncio
import logging
from typing import Any
import inputs
from emoconnect.EmoConnectManager import EmoConnectManager
from emoconnect.ble.command import CommandUtil
from emoconnect.ble.request import StateRequest

logging.basicConfig(format='[EMO] %(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger()
# can be changed to logging.DEBUG for debugging issues
logger.setLevel(logging.INFO)


def getKeyboard():
    keyboard = None
    keyboards = inputs.devices.keyboards
    num_keyboards = len(keyboards)
    if num_keyboards == 1:
        keyboard = keyboards[0]
    elif num_keyboards > 1:
        print('More than one keyboard detected, please choose one to use:')
        for i in range(num_keyboards):
            print(f'{i}) {keyboards[i].name}')
        choice = input('\nChoice (0=default): ')
        keyboard = keyboards[int(choice)]
    return keyboard


async def commandRx(command: Any):
    print(f'Received command: {command}')


async def main():
    running = False
    keyboard = getKeyboard()

    ecm = EmoConnectManager()
    await ecm.connectToEmo()
    state = await ecm.sendRequest(StateRequest.everything())

    ecm.setCommandCallback(commandRx)
    print('stop')

    await ecm.sendCommand(CommandUtil.clear())
    await asyncio.sleep(0.5)
    await ecm.sendCommand(CommandUtil.enterApp(4))
    await asyncio.sleep(0.5)
    await ecm.sendCommand(CommandUtil.startGame())
    await asyncio.sleep(0.5)
    await ecm.sendCommand(CommandUtil.resetting())
    await asyncio.sleep(0.5)
    await ecm.sendCommand(CommandUtil.statusOnOff(True))
    await ecm.sendCommand(CommandUtil.chargeLevelOnOff(True))
    running = True
    print('Running...  Press Escape to quit')
    while running:
        events = keyboard.read()
        for event in events:
            if event.code == 'KEY_UP':
                if event.state == 1:
                    await ecm.sendCommand(CommandUtil.forward())
                elif event.state == 0:
                    await ecm.sendCommand(CommandUtil.stop())
            if event.code == 'KEY_DOWN':
                if event.state == 1:
                    await ecm.sendCommand(CommandUtil.back())
                elif event.state == 0:
                    await ecm.sendCommand(CommandUtil.stop())
            if event.code == 'KEY_LEFT':
                if event.state == 1:
                    await ecm.sendCommand(CommandUtil.left())
                elif event.state == 0:
                    await ecm.sendCommand(CommandUtil.stop())
            if event.code == 'KEY_RIGHT':
                if event.state == 1:
                    await ecm.sendCommand(CommandUtil.right())
                elif event.state == 0:
                    await ecm.sendCommand(CommandUtil.stop())
            if event.code == 'KEY_ESC':
                running = False

        await asyncio.sleep(0.01)

    await ecm.sendCommand(CommandUtil.stop())
    await ecm.sendCommand(CommandUtil.exitApp())
    await ecm.disconnect()

asyncio.run(main())
