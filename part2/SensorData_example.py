import SensorData_pb2

PB_FILE_PATH = 'SensorData.pb'
JSON_FILE_PATH = 'SensorData.json'

sensorData = SensorData_pb2.SensorData()
sensorData.sensorType = sensorData.HUMIDITY
sensorData.value = 35



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(sensorData.SerializeToString())
f.close()

# 读sensorData
sensorData = SensorData_pb2.SensorData()
f = open(PB_FILE_PATH, "rb")
sensorData.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(sensorData)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

