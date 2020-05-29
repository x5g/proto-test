import maps_pb2

PB_FILE_PATH = 'maps.pb'
JSON_FILE_PATH = 'maps.json'

getDistanceRequest = maps_pb2.GetDistanceRequest()
getDistanceRequest.origin = "38.8633,65.7978"
getDistanceRequest.dest = "44.8633,75.7978"



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(getDistanceRequest.SerializeToString())
f.close()

# 读getDistanceRequest
getDistanceRequest = maps_pb2.GetDistanceRequest()
f = open(PB_FILE_PATH, "rb")
getDistanceRequest.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(getDistanceRequest)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

