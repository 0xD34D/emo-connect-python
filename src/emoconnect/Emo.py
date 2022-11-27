import asyncio
from bleak import BleakScanner
import emoconnect.EmoConstants as EmoConstants
import emoconnect.ble.util.BleRequestUtil as BleRequestUtil


async def getAvailableEmos():
    devices = await BleakScanner.discover()
    emos = []
    for d in devices:
        if str(d.name).startswith(EmoConstants.BLE_NAME):
            emos.append(d)
            print(f'{d.address}\t{d.name}')
    print(emos)
    return emos

asyncio.run(getAvailableEmos())
