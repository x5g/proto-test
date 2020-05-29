import demo7_pb2


PB_FILE_PATH = 'demo7.pb'
JSON_FILE_PATH = 'demo7.json'

demo = demo7_pb2.A()
b = demo7_pb2.B()
b.b2 = 'b2'
demo.b.append(b)
demo.id = 'b2'


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(demo.SerializeToString())
f.close()

# 读demo
demo = demo7_pb2.B()
f = open(PB_FILE_PATH, "rb")
demo.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(demo)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

