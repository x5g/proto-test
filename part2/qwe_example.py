import qwe_pb2

PB_FILE_PATH = 'qwe.pb'
JSON_FILE_PATH = 'qwe.json'

qwe = qwe_pb2.Qwe()
qwe.age = 24
qwe.name = 'ivan'


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(qwe.SerializeToString())
f.close()

# 读qwe
qwe = qwe_pb2.Qwe()
f = open(PB_FILE_PATH, "rb")
qwe.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(qwe)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

