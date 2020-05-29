from testP_pb2 import TestMessage

PB_FILE_PATH = 'testP.pb'
JSON_FILE_PATH = 'testP.json'

testP = TestMessage()
testP.id = 1000
testP.name = 'lisiwang'


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(testP.SerializeToString())
f.close()

# 读addressbook
testP = TestMessage()
f = open(PB_FILE_PATH, "rb")
testP.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(testP)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

