import wind_pb2

PB_FILE_PATH = 'wind.pb'
JSON_FILE_PATH = 'wind.json'

wind = wind_pb2.Wind()
import random
gps1 = wind_pb2.Wind.Gps()
gps1.longitude = random.random()
gps1.dimension = random.random()
gps1.coordinate = random.random()
wind.gps.append(gps1)
gps2 = wind_pb2.Wind.Gps()
gps2.longitude = random.random()
gps2.dimension = random.random()
gps2.coordinate = random.random()
wind.gps.append(gps2)
gps3 = wind_pb2.Wind.Gps()
gps3.longitude = random.random()
gps3.dimension = random.random()
gps3.coordinate = random.random()
wind.gps.append(gps3)



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(wind.SerializeToString())
f.close()

# 读wind
wind = wind_pb2.Wind()
f = open(PB_FILE_PATH, "rb")
wind.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(wind)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

