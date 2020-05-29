from game_service_pb2 import RequestMessage, ResponseMessage

PB_FILE_PATH_1 = 'game_service_1.pb'
JSON_FILE_PATH_1 = 'game_service_1.json'
PB_FILE_PATH_2 = 'game_service_2.pb'
JSON_FILE_PATH_2 = 'game_service_2.json'

request = RequestMessage()
request.msg = "just for test"

response = ResponseMessage()
response.msg = "echo: just for test"

# 以二进制形式保存
f = open(PB_FILE_PATH_1, "wb")
f.write(request.SerializeToString())
f.close()

f = open(PB_FILE_PATH_2, "wb")
f.write(response.SerializeToString())

# 读request及response
request = RequestMessage()
f = open(PB_FILE_PATH_1, "rb")
request.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json1 = MessageToJson(request)
print(json1)

response = ResponseMessage()
f = open(PB_FILE_PATH_2, "rb")
response.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json2 = MessageToJson(response)
print(json2)

# 保存json
f = open(JSON_FILE_PATH_1, "w")
f.write(json1)
f.close()

f = open(JSON_FILE_PATH_2, "w")
f.write(json2)
f.close()
