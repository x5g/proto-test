import complex_pb2

PB_FILE_PATH = 'complex.pb'
JSON_FILE_PATH = 'complex.json'

message = complex_pb2.ComplexMessage()
message.one_dummy.id = 12
message.one_dummy.name = 'dummy1'
multiple_dummy = complex_pb2.DummyMessage()
multiple_dummy.id = 1
multiple_dummy.name = 'dummy1'
message.multiple_dummy.append(multiple_dummy)
multiple_dummy.id = 2
multiple_dummy.name = 'dummy2'
message.multiple_dummy.append(multiple_dummy)
multiple_dummy.id = 3
multiple_dummy.name = 'dummy3'
message.multiple_dummy.append(multiple_dummy)
multiple_dummy.id = 4
multiple_dummy.name = 'dummy4'
message.multiple_dummy.append(multiple_dummy)


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(message.SerializeToString())
f.close()

# 读message
message = complex_pb2.ComplexMessage()
f = open(PB_FILE_PATH, "rb")
message.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(message)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

