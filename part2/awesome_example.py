import awesome_pb2

PB_FILE_PATH = 'awesome.pb'
JSON_FILE_PATH = 'awesome.json'

message = awesome_pb2.AwesomeMessage()
message.awesome_field = 'Hello World!'



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(message.SerializeToString())
f.close()

# 读message
message = awesome_pb2.AwesomeMessage()
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

