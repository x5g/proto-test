import test5_pb2

PB_FILE_PATH = 'test5.pb'
JSON_FILE_PATH = 'test5.json'

helloRequest = test5_pb2.HelloRequest()
helloRequest.username = 'Logan Ma'


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(helloRequest.SerializeToString())
f.close()

# 读helloRequest
helloRequest = test5_pb2.HelloRequest()
f = open(PB_FILE_PATH, "rb")
helloRequest.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(helloRequest)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

