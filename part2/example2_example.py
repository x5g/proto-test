import example2_pb2

PB_FILE_PATH = 'example2.pb'
JSON_FILE_PATH = 'example2.json'

set = example2_pb2.Set()
set.id = 1
set.name = 'hello'
ld = example2_pb2.LD()
ld.ip = 666
set.ld_list.append(ld)



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(set.SerializeToString())
f.close()

# 读set
set = example2_pb2.Set()
f = open(PB_FILE_PATH, "rb")
set.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(set)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

