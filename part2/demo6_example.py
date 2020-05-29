import demo6_pb2

PB_FILE_PATH = 'demo6.pb'
JSON_FILE_PATH = 'demo6.json'

request = demo6_pb2.Request()
request.endpoint = ' '
request.requestType = 0
request.token = ' '
request.params['NORMAL'] = 'NORMAL'
request.params['ASYNC'] = 'ASYNC'
request.params['BATCH'] = 'BATCH'
request.params['ASYNC_BATCH'] = 'ASYNC_BATCH'
request.body = ' '




# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(request.SerializeToString())
f.close()

# 读request
request = demo6_pb2.Request()
f = open(PB_FILE_PATH, "rb")
request.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(request)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

