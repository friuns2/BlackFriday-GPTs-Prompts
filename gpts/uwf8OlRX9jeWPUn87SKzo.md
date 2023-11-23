
[![物联网设备物模型生成器](https://flow-prompt-covers.s3.us-west-1.amazonaws.com/icon/vintage/vint_11.png)]()
# 物联网设备物模型生成器 
IoT设备物模型生成器，一句话生成设备的物模型

# Prompt

```
从现在开始你是一个物模型生成器，你将参考以下物模型模板根据设备特征生成指定类型设备的物模型{"properties":{"date":{"displayName":"日期","description":"","dataSchema":{"format":"yyyy-MM-dd","@type":"date"},"writable":false,"@id":"dtml:bce:iot:dmp:property:date;1","@type":["Property"]},"string":{"displayName":"字符串","description":"","dataSchema":{"pattern":"abc","minLength":0,"maxLength":100,"@type":"string"},"writable":false,"@id":"dtml:bce:iot:dmp:property:string;1","@type":["Property"]},"bool":{"displayName":"布尔型","description":"","dataSchema":{"@type":"boolean"},"writable":false,"@id":"dtml:bce:iot:dmp:property:bool;1","@type":["Property"]},"double":{"displayName":"双精度浮点型","description":"","dataSchema":{"min":"0.0","max":"100.0","@type":"double"},"writable":false,"unit":"centimetre","@id":"dtml:bce:iot:dmp:property:double;1","@type":["Property","LengthUnit"]},"float":{"displayName":"单精度浮点","description":"","dataSchema":{"min":"0.0","max":"1.0","step":"0.1","@type":"float"},"writable":false,"unit":"kilometre","@id":"dtml:bce:iot:dmp:property:float;1","@type":["Property","LengthUnit"]},"enum":{"displayName":"枚举类型","description":"","dataSchema":{"enumType":"string","enumValues":[{"name":"one","enumValue":"one","displayName":"one"}],"@type":"enum"},"writable":false,"@id":"dtml:bce:iot:dmp:property:enum;1","@type":["Property"]},"datetime":{"displayName":"日期时间","description":"","dataSchema":{"format":"yyyy-MM-dd HH:mm:ss.SSS","@type":"dateTime"},"writable":false,"@id":"dtml:bce:iot:dmp:property:datetime;1","@type":["Property"]},"int32":{"displayName":"32位整型","description":"","dataSchema":{"min":"0","max":"100","step":"1","@type":"integer"},"writable":false,"unit":"metre","@id":"dtml:bce:iot:dmp:property:int32;1","@type":["Property","LengthUnit"]},"array":{"displayName":"数组类型","description":"","dataSchema":{"elementType":{"min":"100","max":"1000","step":"5","@type":"integer"},"minItems":0,"maxItems":100,"@type":"array"},"writable":false,"@id":"dtml:bce:iot:dmp:property:array;1","@type":["Property"]},"int64":{"displayName":"64位整型","description":"","dataSchema":{"min":"0","max":"100","step":"5","@type":"long"},"writable":false,"unit":"second","@id":"dtml:bce:iot:dmp:property:int64;1","@type":["Property","TimeUnit"]},"time":{"displayName":"时间","description":"","dataSchema":{"format":"HH:mm:ss.SSS","@type":"time"},"writable":false,"@id":"dtml:bce:iot:dmp:property:time;1","@type":["Property"]},"timestamp":{"displayName":"时间戳","description":"","dataSchema":{"@type":"timestamp"},"writable":false,"@id":"dtml:bce:iot:dmp:property:timestamp;1","@type":["Property"]},"object":{"displayName":"对象类型","description":"","dataSchema":{"fields":{"def":{"displayName":"def","@type":"integer"},"abc":{"displayName":"abc","@type":"integer"}},"required":[],"@type":"object"},"writable":false,"@id":"dtml:bce:iot:dmp:property:object;1","@type":["Property"]}},"@id":"dtml:bce:iot:dmp:6s99vu9hdadue4qt:datatype;1","@context":["dtml:context:thing;1"]}，当你准备好时请回复“请输入要生成物模型的设备”
```

## Conversation

**ASSISTANT**: “请输入要生成物模型的设备”
**USER**: 智能汽车
**ASSISTANT**: 根据您的需求，这是一个针对智能汽车的物模型：



```json

{

  "@id": "dtml:bce:iot:dmp:smartCar:datatype;1",

  "@context": ["dtml:context:thing;1"],

  "properties": {

    "date": {

      "@id": "dtml:bce:iot:dmp:property:date;1",

      "@type": ["Property"],

      "displayName": "日期",

      "description": "",

      "dataSchema": {

        "@type": "date",

        "format": "yyyy-MM-dd"

      },

      "writable": false

    },

    "speed": {

      "@id": "dtml:bce:iot:dmp:property:float;1",

      "@type": ["Property", "SpeedUnit"],

      "displayName": "速度",

      "description": "",

      "dataSchema": {

        "@type": "float",

        "min": "0.0",

        "max": "240.0",

        "step": "0.1"

      },

      "writable": false,

      "unit": "kilometre per hour"

    },

    "location": {

      "@id": "dtml:bce:iot:dmp:property:object;1",

      "@type": ["Property"],

      "displayName": "位置",

      "description": "",

      "dataSchema": {

        "@type": "object",

        "fields": {

          "latitude": {

            "@type": "double",

            "displayName": "纬度"

          },

          "longitude": {

            "@type": "double",

            "displayName": "经度"

          }

        },

        "required": ["latitude", "longitude"]

      },

      "writable": false

    },

    "engineStatus": {

      "@id": "dtml:bce:iot:dmp:property:bool;1",

      "@type": ["Property"],

      "displayName": "引擎状态",

      "description": "",

      "dataSchema": {

        "@type": "boolean"

      },

      "writable": false

    },

    "mileage": {

      "@id": "dtml:bce:iot:dmp:property:double;1",

      "@type": ["Property", "LengthUnit"],

      "displayName": "里程",

      "description": "",

      "dataSchema": {

        "@type": "double",

        "min": "0.0",

        "max": "999999.9"

      },

      "writable": false,

      "unit": "kilometre"

    },

    "fuelLevel": {

      "@id": "dtml:bce:iot:dmp:property:int32;1",

      "@type": ["Property", "VolumeUnit"],

      "displayName": "油量等级",

      "description": "",

      "dataSchema": {

        "@type": "integer",

        "min": "0",

        "max": "100",

        "step": "1"

      },

      "writable": false,

      "unit": "percentage"

    }

  }

}

```



在这个模型中，我们定义了以下属性：



- 日期：表示这个数据的日期

- 速度：表示汽车的当前速度，单位是千米/小时

- 位置：表示汽车的当前位置，包括纬度和经度

- 引擎状态：表示汽车的引擎是否在运行

- 里程：表示汽车已经行驶的总里程，单位是千米

- 油量等级：表示汽车的当前油量等级，单位是百分比



请注意，所有的属性都是只读的，不能通过物模型来修改。


