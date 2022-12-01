# City Set Request
**Service UUID:** `0000ffe0-0000-1000-8000-00805f9b34fb`

**Characteristic:** `0000ffe1-0000-1000-8000-00805f9b34fb`

---
## city_set
### request:
```json
{
   "type":"city_set",
   "data":{
      "coord":{
         "lat":0.0,
         "lon":0.0
      },
      "country":"",
      "id":0,
      "name":"Nowhere ",
      "state":""
   }
}
```
### response:
```json
{
   "type":"city_rsp",
   "data":{
      "result":1
   }
}
```
