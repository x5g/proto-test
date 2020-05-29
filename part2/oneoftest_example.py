import oneoftest_pb2

PB_FILE_PATH = 'oneoftest.pb'
JSON_FILE_PATH = 'oneoftest.json'

demoBrokenCbor = oneoftest_pb2.DemoBrokenCbor()
oneKind = demoBrokenCbor.one_kind
oneKind.value = 'oneKind.value'


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(demoBrokenCbor.SerializeToString())
f.close()

# 读demoBrokenCbor
demoBrokenCbor = oneoftest_pb2.DemoBrokenCbor()
f = open(PB_FILE_PATH, "rb")
demoBrokenCbor.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(demoBrokenCbor)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

