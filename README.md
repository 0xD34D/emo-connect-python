# emo-connect-python
Python library for connecting and interacting with an EMO pet

## Usage
```bash
pip install src/ --user
```
## Example
```python
import asyncio
import json
import logging

from emoconnect.EmoConnectManager import EmoConnectManager
from emoconnect.ble.request import StateRequest

logging.basicConfig(format='[EMO] %(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger()
# can be changed to logging.DEBUG for debugging issues
logger.setLevel(logging.INFO)


async def main():
    ecm = EmoConnectManager()
    await ecm.connectToEmo()

    state = await ecm.sendRequest(StateRequest.everything())
    print(state)

    await ecm.disconnect()

asyncio.run(main())
```