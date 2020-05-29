import demo3_pb2

PB_FILE_PATH = 'demo3.pb'
JSON_FILE_PATH = 'demo3.json'


builder = demo3_pb2.Demo()
builder.id = 1
builder.value = '0xffffff'
builder.likes.append('chifanfan')
builder.likes.append('shuijiaojiao')


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(builder.SerializeToString())
f.close()

# 读builder
builder = demo3_pb2.Demo()
f = open(PB_FILE_PATH, "rb")
builder.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(builder)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

