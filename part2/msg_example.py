import msg_pb2

PB_FILE_PATH = 'msg.pb'
JSON_FILE_PATH = 'msg.json'

msg1 = msg_pb2.Msg1()
msg1.field1 = '1'
msg1.field2 = 2
msg1.field3 = '3'



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(msg1.SerializeToString())
f.close()

# 读msg1
msg1 = msg_pb2.Msg1()
f = open(PB_FILE_PATH, "rb")
msg1.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(msg1)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

