import lona_pb2

PB_FILE_PATH = 'lona.pb'
JSON_FILE_PATH = 'lona.json'

timeEvent = lona_pb2.LonaEvent()
timeEvent.name = 'TimerEvent'
timeEvent.gps_lat = 473637443
timeEvent.gps_lon = 85120203
timeEvent.server_timestamp = 1579520347.7409549


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(timeEvent.SerializeToString())
f.close()

# 读timeEvent
timeEvent = lona_pb2.LonaEvent()
f = open(PB_FILE_PATH, "rb")
timeEvent.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(timeEvent)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

