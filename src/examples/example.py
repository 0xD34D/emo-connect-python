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
from emoconnect import EmoConstants
from emoconnect.EmoConnectManager import EmoConnectManager
from emoconnect.ble.util import BleRequestUtil
import logging

logging.basicConfig(format='[EMO] %(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger()
# can be changed to logging.DEBUG for debugging issues
logger.setLevel(logging.INFO)


async def main():
    async def _handle_rx(data: str):
        print(f'received: {data}')

    emc = EmoConnectManager(_handle_rx)
    await emc.connectToEmo()

    await emc.sendRequest(BleRequestUtil.deviceid())
    await asyncio.sleep(0.5)

    await emc.disconnect()

asyncio.run(main())
