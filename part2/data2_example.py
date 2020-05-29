import data2_pb2

PB_FILE_PATH = 'data2.pb'
JSON_FILE_PATH = 'data2.json'

message = data2_pb2.Message()
message.cmd = data2_pb2.Message.Connect
room = data2_pb2.Room()
room.channel = '1'
room.count = 1
message.room.append(room)



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(message.SerializeToString())
f.close()

# 读message
message = data2_pb2.Message()
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

