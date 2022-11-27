import emoconnect.EmoConstants as EmoConstants
from emoconnect.ble.config.RequestConfig import RequestConfig
from emoconnect.util.ByteUtil import strToBytes


def request(data: list[int]) -> bytes:
    config: RequestConfig = RequestConfig(data=data, requestType=None)
    return strToBytes(config.toJson())


def deviceid() -> bytes:
    return request([EmoConstants.BLE_STATE_DEVICEID])


def version() -> bytes:
    return request([EmoConstants.BLE_STATE_VERSION])
