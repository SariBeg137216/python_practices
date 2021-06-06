import json
from collections import namedtuple

# data = {"key1": "value1", "key2": "value2"}
# sampleJson = """{"key1": "value1", "key2": "value2"}"""
# print(json.dumps(data))
# jsdata = json.loads(sampleJson)
# print(jsdata['key2'])
# # sampleJson = {"key1": "value1", "key2": "value2"}
# json_data = json.dumps(sampleJson, indent=2, separators=(",", " = "))
# print(json_data)
# sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
# with open('newfile.txt', 'w') as f:
#      json.dump(sampleJson, f, indent=4, sort_keys=True)

# sampleJson = """{
#    "company":{
#       "employee":{
#          "name":"emma",
#          "payble":{
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""

# jsdata = json.loads(sampleJson)
# print(jsdata['company']['employee']['payble']['salary'])

#
# class Vehicle:
#     def __init__(self, name, engine, price):
#         self.name = name
#         self.engine = engine
#         self.price = price
#
#
# class JSEncode(json.JSONEncoder):
#     def default(self, obj):
#         obj = obj.__dict__
#         return obj
#
#
# vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
# vehicleobj = json.dumps(vehicle, indent=4, cls=JSEncode)
# print(vehicleobj)
# Vehicle = '{"name": "Toyota Rav4", "engine": "2.5L", "price": 32000}'
#
#
# def tojson(obj):
#     return namedtuple('X', obj.keys())(*obj.values())
#
#
# v = json.loads(Vehicle, object_hook=tojson)
#
# print(v.name, v.engine, v.price)

# 
# samplejsonData = InvalidJsonData = """{ "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000, "bonus":800} } } }"""
# 
# 
# def jsonvalidation(obj):
#     try:
#         jsobj = json.loads(obj)
#     except ValueError as err:
#         return "invalid json object"
#     return jsobj
# 
# 
# print(jsonvalidation(samplejsonData))


sample = """[
    {
        "id": 1,
        "name": "name1",
        "color": [
            "red",
            "green"
        ]
    },
    {
        "id": 2,
        "name": "name2",
        "color": [
            "pink",
            "yellow"
        ]
    }
]"""

data = json.loads(sample)
values = [item.get('name') for item in data]
print(values)



