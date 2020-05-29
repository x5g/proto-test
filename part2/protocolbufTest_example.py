import protocolbufTest_pb2

PB_FILE_PATH = 'protocolbufTest.pb'
JSON_FILE_PATH = 'protocolbufTest.json'

myprotobuf = protocolbufTest_pb2.HeartInfo()
import time
myprotobuf.curtime = int(time.time())
myprotobuf.hostip = '127.0.0.1'


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(myprotobuf.SerializeToString())
f.close()

# 读myprotobuf
myprotobuf = protocolbufTest_pb2.HeartInfo()
f = open(PB_FILE_PATH, "rb")
myprotobuf.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(myprotobuf)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

