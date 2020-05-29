import msg_pb2

PB_FILE_PATH = 'msg.pb'
JSON_FILE_PATH = 'msg.json'

msg = msg_pb2.Msg()
msg.head.cid = 123
msg.ret = 321
msg.Extensions[msg_pb2.id] = 111
msg.Extensions[msg_pb2.mod_req].b = True


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(msg.SerializeToString())
f.close()

# 读base
base = msg_pb2.Msg()
f = open(PB_FILE_PATH, "rb")
base.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(base)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

