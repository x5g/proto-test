import socket_pb2

PB_FILE_PATH = 'socket.pb'
JSON_FILE_PATH = 'socket.json'

socket = socket_pb2.Socket()
socket.request_field = 'request_filed'
socket.receive_field = 'receive_filed'



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(socket.SerializeToString())
f.close()

# 读socket
socket = socket_pb2.Socket()
f = open(PB_FILE_PATH, "rb")
socket.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(socket)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

