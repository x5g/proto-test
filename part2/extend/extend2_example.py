import person_pb2
import main_pb2

PB_FILE_PATH = 'person.pb'
JSON_FILE_PATH = 'person.json'

base = main_pb2.base()
base.timestamp = 4321234
base.owner.extend(['qwe', 'ewq'])
base.Extensions[person_pb2.name] = 'person_pb2.name'
base.Extensions[person_pb2.res].extend(['person_pb2.res1', 'person_pb2.res2'])
# base.Extensions[extend_pb2.res] = 'res'


# base.RegisterExtension(name)
# print(base.__dir__())
# print(base.HasExtension(extend_pb2.name))
# print(extend_pb2.name.make.__dir__())




# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(base.SerializeToString())
f.close()

# 读base
base = main_pb2.base()
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

