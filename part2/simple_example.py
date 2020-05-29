import simple_pb2

PB_FILE_PATH = 'simple.pb'
JSON_FILE_PATH = 'simple.json'

simpleb = simple_pb2.SimpleMessage()
simpleb.id = 12345
simpleb.is_simple = True
simpleb.name = 'John'
simpleb.sample_list.extend([1, 4, 7, 8])


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(simpleb.SerializeToString())
f.close()

# 读simpleb
simpleb = simple_pb2.SimpleMessage()
f = open(PB_FILE_PATH, "rb")
simpleb.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(simpleb)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

