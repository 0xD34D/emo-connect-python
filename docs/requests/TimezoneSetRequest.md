# Timezone Set Request
**Service UUID:** `0000ffe0-0000-1000-8000-00805f9b34fb`

**Characteristic:** `0000ffe1-0000-1000-8000-00805f9b34fb`

---
## timezone_set
### request:
```json
{
   "type":"timezone_set",
   "data":{
      "code":"",
      "name":"America/Los_Angeles",
      "offset":-28800
   }
}
```
### response:
```json
{
   "type":"timezone_rsp",
   "data":{
      "result":1
   }
}
```
