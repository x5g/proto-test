import example_pb2

PB_FILE_PATH = 'example.pb'
JSON_FILE_PATH = 'example.json'

event = example_pb2.Event()
event.message = 'Hello World!'
programming = example_pb2.Programming()
programming.language = 'C++'
event.language.append(programming)


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(event.SerializeToString())
f.close()

# 读event
event = example_pb2.Event()
f = open(PB_FILE_PATH, "rb")
event.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(event)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

