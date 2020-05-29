import protobuf_pb2

PB_FILE_PATH = 'protobuf.pb'
JSON_FILE_PATH = 'protobuf.json'

theMsg = protobuf_pb2.TheMsg()
theMsg.name = 'TheMsg.name'
theMsg.num = int(572)



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(theMsg.SerializeToString())
f.close()

# 读theMsg
theMsg = protobuf_pb2.TheMsg()
f = open(PB_FILE_PATH, "rb")
theMsg.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(theMsg)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

