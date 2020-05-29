import GpsLocation_pb2

PB_FILE_PATH = 'GpsLocation.pb'
JSON_FILE_PATH = 'GpsLocation.json'

gpsLocation = GpsLocation_pb2.GpsLocation()
gpsLocation.latitude = 488679
gpsLocation.longitude = 240093


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(gpsLocation.SerializeToString())
f.close()

# 读gpsLocation
gpsLocation = GpsLocation_pb2.GpsLocation()
f = open(PB_FILE_PATH, "rb")
gpsLocation.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(gpsLocation)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

