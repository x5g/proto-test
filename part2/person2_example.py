import person2_pb2

PB_FILE_PATH = 'person2.pb'
JSON_FILE_PATH = 'person2.json'

uesrInfo = person2_pb2.UserInfo()
uesrInfo.name = 'userInfo'
uesrInfo.age = 2
game1 = person2_pb2.LoveGame()
game1.name = '1'
game1.type = '2'
uesrInfo.game.append(game1)
uesrInfo.sex = person2_pb2.male

# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(uesrInfo.SerializeToString())
f.close()

# 读uesrInfo
uesrInfo = person2_pb2.UserInfo()
f = open(PB_FILE_PATH, "rb")
uesrInfo.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(uesrInfo)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

