# emo-connect-python
Python library for connecting and interacting with an EMO pet

## Usage
```bash
pip install src/ --user
```
## Example
```python
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
```