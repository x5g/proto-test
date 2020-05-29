import data_pb2

PB_FILE_PATH = 'data.pb'
JSON_FILE_PATH = 'data.json'

data = data_pb2.Demo()
data.A = int(5)
data.B = int(5)
data.C = int(2015)



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(data.SerializeToString())
f.close()

# 读data
data = data_pb2.Demo()
f = open(PB_FILE_PATH, "rb")
data.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(data)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

