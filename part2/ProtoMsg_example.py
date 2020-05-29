import ProtoMsg_pb2

PB_FILE_PATH = 'ProtoMsg.pb'
JSON_FILE_PATH = 'ProtoMsg.json'

protoMsg = ProtoMsg_pb2.Message()
protoMsg.content = 'Hello World!'


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(protoMsg.SerializeToString())
f.close()

# 读protoMsg
protoMsg = ProtoMsg_pb2.Message()
f = open(PB_FILE_PATH, "rb")
protoMsg.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(protoMsg)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

