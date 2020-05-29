import http_pb2

PB_FILE_PATH = 'http.pb'
JSON_FILE_PATH = 'http.json'

request = http_pb2.HttpRequest()
request.major_version = 1
request.minor_version = 2
request.url = '/index.html'
host = http_pb2.StringStringPair()
host.first = 'Host'
host.second = 'www.example.com'
request.headers.append(host)


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(request.SerializeToString())
f.close()

# 读request
request = http_pb2.HttpRequest()
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

