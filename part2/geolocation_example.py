import geolocation_pb2

PB_FILE_PATH = 'geolocation.pb'
JSON_FILE_PATH = 'geolocation.json'

geoLocation = geolocation_pb2.GeoLocation()
geoLocation.device = 0
geoLocation.lat = 0.0
geoLocation.lng = 0.0



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(geoLocation.SerializeToString())
f.close()

# 读geoLocation
geoLocation = geolocation_pb2.GeoLocation()
f = open(PB_FILE_PATH, "rb")
geoLocation.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(geoLocation)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

