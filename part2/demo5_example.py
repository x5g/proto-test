import demo5_pb2

PB_FILE_PATH = 'demo5.pb'
JSON_FILE_PATH = 'demo5.json'

o = demo5_pb2.Demo()
o.query = 'hello from Python'
o.number = 30704


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(o.SerializeToString())
f.close()

# 读o
o = demo5_pb2.Demo()
f = open(PB_FILE_PATH, "rb")
o.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(o)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

