import Common_pb2

PB_FILE_PATH = 'Common.pb'
JSON_FILE_PATH = 'Common.json'

chatPacket = Common_pb2.ChatPacket()
userInfo = chatPacket.user_info
userInfo.user_id = 2017
userInfo.name = 'Pete Houston'
userInfo.role = Common_pb2.ADMIN
chatPacket.user_id = 2017
chatPacket.content = 'A simple chat message from user_id = 2017'



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(chatPacket.SerializeToString())
f.close()

# 读chatPacket
chatPacket = Common_pb2.ChatPacket()
f = open(PB_FILE_PATH, "rb")
chatPacket.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(chatPacket)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

