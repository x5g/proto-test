import test2_pb2

PB_FILE_PATH = 'test2.pb'
JSON_FILE_PATH = 'test2.json'

example = test2_pb2.Test()
example.x = 1
example.y = 2



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(example.SerializeToString())
f.close()

# 读example
example = test2_pb2.Test()
f = open(PB_FILE_PATH, "rb")
example.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(example)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

