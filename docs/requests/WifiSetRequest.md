# WiFi Set Request
**Service UUID:** `0000ffe0-0000-1000-8000-00805f9b34fb`

**Characteristic:** `0000ffe1-0000-1000-8000-00805f9b34fb`

---
## wifi_set
### request:
```json
{
   "type":"wifi_set",
   "data":{
      "ssid":"Groot",
      "password":"I_am_Groot!",
   }
}
```
### response:
```json
{
   "type":"wifi_rsp",
   "data":{
      "result":0
   }
}
```
