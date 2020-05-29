import nested_pb2

PB_FILE_PATH = 'nested.pb'
JSON_FILE_PATH = 'nested.json'

building = nested_pb2.Building()
building.name = 'building'
building.buildingNumber = 'buildingNumber'
building.street.name = 'street'
building.street.city.name = 'city'
building.street.city.zipCode = 'zipCode'
building.street.city.countryName = 'countryName'


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(building.SerializeToString())
f.close()

# 读building
building = nested_pb2.Building()
f = open(PB_FILE_PATH, "rb")
building.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(building)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

