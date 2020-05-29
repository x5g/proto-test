import GroundData_pb2

PB_FILE_PATH = 'GroundData.pb'
JSON_FILE_PATH = 'GroundData.json'

groundData = GroundData_pb2.GroundData()

# gpsLocationBuilder = GroundData_pb2.GpsLocation__pb2.GpsLocation()
gpsLocationBuilder = groundData.gpsLocation
gpsLocationBuilder.latitude = 488679
gpsLocationBuilder.longitude = 240093

sensorHumidity = GroundData_pb2.SensorData__pb2.SensorData()
sensorHumidity.sensorType = sensorHumidity.HUMIDITY
sensorHumidity.value = 35

sensorTemperature = GroundData_pb2.SensorData__pb2.SensorData()
sensorTemperature.sensorType = sensorTemperature.TEMPERATURE
sensorTemperature.value = 14

groundData.id = 1
groundData.timestamp = 1570402900
# groundData.gpsLocation.add(gpsLocationBuilder)
groundData.sensorDatas.append(sensorHumidity)
groundData.sensorDatas.append(sensorTemperature)

# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(groundData.SerializeToString())
f.close()

# 读addressbook
groundData = GroundData_pb2.GroundData()
f = open(PB_FILE_PATH, "rb")
groundData.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(groundData)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

