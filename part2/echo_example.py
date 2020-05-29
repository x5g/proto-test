import echo_pb2

PB_FILE_PATH = 'echo.pb'
JSON_FILE_PATH = 'echo.json'

echoResponse = echo_pb2.EchoResponse()
echoResponse.message = "lizzzcai" + "echo" + "" + "123" + "123.1234"



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(echoResponse.SerializeToString())
f.close()

# 读echoResponse
echoResponse = echo_pb2.EchoResponse()
f = open(PB_FILE_PATH, "rb")
echoResponse.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(echoResponse)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

