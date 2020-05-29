import message2_pb2

PB_FILE_PATH = 'message2.pb'
JSON_FILE_PATH = 'message2.json'

command = message2_pb2.Command()
command.type = message2_pb2.Command.START_TEST
command.name = 'Test Case 1'
command.data = 'Test Data'

# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(command.SerializeToString())
f.close()

# 读command
command = message2_pb2.Command()
f = open(PB_FILE_PATH, "rb")
command.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(command)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

