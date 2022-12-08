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
import signal
from typing import Any
from emoconnect.EmoConnectManager import EmoConnectManager
from emoconnect.ble.command import CommandUtil
from emoconnect.ble.request import StateRequest

logging.basicConfig(format='[EMO] %(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger()
# can be changed to logging.DEBUG for debugging issues
logger.setLevel(logging.INFO)

running: bool = False


async def commandRx(command: Any):
    print(f'Received command: {command}')


async def main():
    global running
    ecm = EmoConnectManager()
    await ecm.connectToEmo()
    state = await ecm.sendRequest(StateRequest.everything())

    def handler(_signum, _frame):
        global running
        running = False
        print('\nCtrl-C received, shutting down...\n')
    signal.signal(signal.SIGINT, handler)

    ecm.setCommandCallback(commandRx)
    await ecm.sendCommand(CommandUtil.statusOnOff(True))
    await ecm.sendCommand(CommandUtil.chargeLevelOnOff(True))
    running = True
    print('Running...  Use Ctrl-C to exit')
    while running:
        await asyncio.sleep(0.1)

    await ecm.disconnect()

asyncio.run(main())
