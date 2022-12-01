# State Request
**Service UUID:** `0000ffe0-0000-1000-8000-00805f9b34fb`

**Characteristic:** `0000ffe1-0000-1000-8000-00805f9b34fb`

---
## get_device_id
### request:
```json
{
   "data":{
      "request": [0]
   },
   "type":"sta_req"
}
```
### response:
```json
{
   "type":"sta_rsp",
   "data":{
      "device":{
         "device_id":"b8d6d34df162"
      }
   }
}
```
## get_version
### request:
```json
{
   "data":{
      "request": [1]
   },
   "type":"sta_req"
}
```
### response:
```json
{
   "type":"sta_rsp",
   "data":{
      "version":{
         "number":24,
         "name":"1.7.0"
      }
   }
}
```
## get_network
### request:
```json
{
   "data":{
      "request": [2]
   },
   "type":"sta_req"
}
```
### response:
```json
{
   "type":"sta_rsp",
   "data":{
      "network":{
         "connected":1,
         "name":"Ye Ole FBI Van"
      }
   }
}
```
## get_xiaoai
### request:
```json
{
   "data":{
      "request": [3]
   },
   "type":"sta_req"
}
```
### response:
```json
{
   "type":"sta_rsp",
   "data":{
      "xiaoai":{
         "connected":0
      }
   }
}
```

## get_alexa
### request:
```json
{
   "data":{
      "request": [4]
   },
   "type":"sta_req"
}
```
### response:
```json
{
   "type":"sta_rsp",
   "data":{
      "alexa":{
         "connected":0
      }
   }
}
```

## get_light
### request:
```json
{
   "data":{
      "request": [5]
   },
   "type":"sta_req"
}
```
### response:
```json
{
   "type":"sta_rsp",
   "data":{
      "light":{
         "state":[
            
         ]
      }
   }
}
```
## get_alarm
### request:
```json
{
   "data":{
      "request": [6]
   },
   "type":"sta_req"
}
```
### response:
```json
{
   "type":"sta_rsp",
   "data":{
      "alarm":{
         "state":[
            {
               "index":1,
               "on":1,
               "time":"20:00",
               "recurrence":"ONCE",
               "tag":"alarm"
            },
            {
               "index":2,
               "on":1,
               "time":"22:00",
               "recurrence":"ONCE",
               "tag":"alarm"
            },
            {
               "index":3,
               "on":1,
               "time":"07:00",
               "recurrence":"ONCE",
               "tag":"alarm"
            }
         ]
      }
   }
}
```
## get_location
### request:
```json
{
   "data":{
      "request": [7]
   },
   "type":"sta_req"
}
```
### response:
```json
{
   "type":"sta_rsp",
   "data":{
      "city":{
         "id":0,
         "name":"Portland",
         "state":"",
         "country":"",
         "coord":{
            "lon":0,
            "lat":0
         }
      }
   }
}
```
## get_timezone
### request:
```json
{
   "data":{
      "request": [8]
   },
   "type":"sta_req"
}
```
### response:
```json
{
   "type":"sta_rsp",
   "data":{
      "timezone":{
         "name":"America/Los_Angeles",
         "code":"",
         "offset":-25200
      }
   }
}
```
## get_achievements
### request:
```json
{
   "data":{
      "request": [9]
   },
   "type":"sta_req"
}
```
### response:
```json
{
   "type":"sta_rsp",
   "data":{
      "achievements":{
         "unlocked":[
            3,
            4,
            5,
            8,
            15,
            24
         ]
      }
   }
}
```
## get_dance_list
### request:
```json
{
   "data":{
      "request": [10]
   },
   "type":"sta_req"
}
```
### response:
```json
{
   "type":"sta_rsp",
   "data":{
      "dances":{
         "joris_unlocked":[
            1,
            2,
            3,
            4
         ]
      }
   }
}
```
## get_personality
### request:
```json
{
   "data":{
      "request": [11]
   },
   "type":"sta_req"
}
```
### response:
```json
{
   "type":"sta_rsp",
   "data":{
      "personality":{
         "name":"EMO",
         "age":162,
         "birthday":"6.18.",
         "color":"orange",
         "lucky_number":1,
         "sign":"geminai",
         "number":"f162"
      }
   }
}
```
## get_personality_and_version
### request:
```json
{
   "data":{
      "request": [11, 1]
   },
   "type":"sta_req"
}
```
### response:
```json
{
   "type":"sta_rsp",
   "data":{
      "personality":{
         "name":"EMO",
         "age":162,
         "birthday":"6.18.",
         "color":"orange",
         "lucky_number":1,
         "sign":"geminai",
         "number":"f162"
      },
      "version":{
         "number":24,
         "name":"1.7.0"
      }
   }
}
```
## get_preference
### request:
```json
{
   "data":{
      "request": [12]
   },
   "type":"sta_req"
}
```
### response:
```json
{
   "type":"sta_rsp",
   "data":{
      "preference":{
         "volume":1,
         "temperature":1,
         "length":1,
         "auto_update":0,
         "schedule_sound":1,
         "schedule":1
      }
   }
}
```
## get_everything
### request:
```json
{
   "data":{
      "request": [0,1,2,3,4,5,6,7,8,9,10,11,12]
   },
   "type":"sta_req"
}
```
### response:
```json
{
   "type":"sta_rsp",
   "data":{
      "device":{
         "device_id":"b8d6d34df162"
      },
      "version":{
         "number":24,
         "name":"1.7.0"
      },
      "network":{
         "connected":0,
         "name":""
      },
      "xiaoai":{
         "connected":0
      },
      "alexa":{
         "connected":0
      },
      "light":{
         "state":[
            
         ]
      },
      "alarm":{
         "state":[
            {
               "index":1,
               "on":0,
               "time":"20:00",
               "recurrence":"ONCE",
               "tag":"alarm"
            },
            {
               "index":2,
               "on":0,
               "time":"22:00",
               "recurrence":"ONCE",
               "tag":"alarm"
            },
            {
               "index":3,
               "on":0,
               "time":"07:00",
               "recurrence":"ONCE",
               "tag":"alarm"
            }
         ]
      },
      "city":{
         "id":0,
         "name":"Portland",
         "state":"OR",
         "country":"US",
         "coord":{
            "lon":-122.6784,
            "lat":45.5152
         }
      },
      "timezone":{
         "name":"America/Los_Angeles",
         "code":"",
         "offset":-25200
      },
      "achievements":{
         "unlocked":[
            3,
            4,
            5,
            6,
            8,
            15,
            24
         ]
      },
      "dances":{
         "joris_unlocked":[
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8
         ]
      },
      "personality":{
         "name":"EMO",
         "age":163,
         "birthday":"6.18.",
         "color":"orange",
         "lucky_number":1,
         "sign":"geminai",
         "number":"f162"
      },
      "preference":{
         "volume":1,
         "temperature":1,
         "length":1,
         "auto_update":0,
         "schedule_sound":0,
         "schedule":1
      }
   }
}
```
