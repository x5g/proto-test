import test6_pb2

PB_FILE_PATH = 'test6.pb'
JSON_FILE_PATH = 'test6.json'

userInfo = test6_pb2.UserInfo()


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(userInfo.SerializeToString())
f.close()

# 读userInfo
userInfo = test6_pb2.UserInfo()
f = open(PB_FILE_PATH, "rb")
userInfo.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(userInfo)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

