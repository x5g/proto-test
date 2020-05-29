import HotMessage_pb2

PB_FILE_PATH = 'HotMessage.pb'
JSON_FILE_PATH = 'HotMessage.json'

message = HotMessage_pb2.Message()
message.msgType = 1
message.msg = str.encode('1011')
message.agree = True



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(message.SerializeToString())
f.close()

# 读message
message = HotMessage_pb2.Message()
f = open(PB_FILE_PATH, "rb")
message.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(message)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

