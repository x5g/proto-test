import message3_pb2

PB_FILE_PATH = 'message3.pb'
JSON_FILE_PATH = 'message3.json'

test = message3_pb2.Test()
test.label = 'hello'
test.type = 111
test.somebutton.button = 'This is button'



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(test.SerializeToString())
f.close()

# 读test
test = message3_pb2.Test()
f = open(PB_FILE_PATH, "rb")
test.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(test)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

