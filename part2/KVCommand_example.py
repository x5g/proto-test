import KVCommand_pb2

PB_FILE_PATH = 'KVCommand.pb'
JSON_FILE_PATH = 'KVCommand.json'

kvMessage = KVCommand_pb2.KVMessage()
kvMessage.id = 2020
kvMessage.len = 1010
kvResponse = kvMessage.response
kvResponse.status = 2010
kvResponse.message = '1020'
kvRequest = kvMessage.request
kvRequest.type = KVCommand_pb2.KVRequest.ITEM
kvRequest.item.command = 'command'
kvRequest.login.username = 'username'
kvRequest.login.password = 'password'



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(kvMessage.SerializeToString())
f.close()

# 读kvMessage
kvMessage = KVCommand_pb2.KVMessage()
f = open(PB_FILE_PATH, "rb")
kvMessage.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(kvMessage)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

