import UDP_pb2

PB_FILE_PATH = 'UDP.pb'
JSON_FILE_PATH = 'UDP.json'

update = UDP_pb2.Update()
update.id = 1
update.text = "test"

# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(update.SerializeToString())
f.close()

# 读update
update = UDP_pb2.Update()
f = open(PB_FILE_PATH, "rb")
update.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(update)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

