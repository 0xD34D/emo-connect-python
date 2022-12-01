from unittest import IsolatedAsyncioTestCase
from emoconnect import EmoConstants
from emoconnect.EmoConnectManager import EmoConnectManager
from emoconnect.ble.request import SettingRequest


class SettingRequestTestCase(IsolatedAsyncioTestCase):
    ecm: EmoConnectManager

    async def asyncSetUp(self):
        self.ecm = EmoConnectManager()
        await self.ecm.connectToEmo()

    async def asyncTearDown(self):
        await self.ecm.disconnect()

    async def test_enter_exit_settings(self):
        response = await self.ecm.sendRequest(SettingRequest.enterSettingMode())
        self.assertEqual(EmoConstants.BLE_SETTING_RSP, response['type'])
        self.assertEqual(1, response['data']['result'])
        response = await self.ecm.sendRequest(SettingRequest.exitSettingMode())
        self.assertEqual(EmoConstants.BLE_SETTING_RSP, response['type'])
        self.assertEqual(1, response['data']['result'])
