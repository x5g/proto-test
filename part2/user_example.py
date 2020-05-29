import user_pb2

PB_FILE_PATH = 'user.pb'
JSON_FILE_PATH = 'user.json'

user = user_pb2.Users()
user.id = 1
user.username = 'demo'
user.mobile = '110'
user.email = 'demo@secdomain.com'



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(user.SerializeToString())
f.close()

# 读user
user = user_pb2.Users()
f = open(PB_FILE_PATH, "rb")
user.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(user)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

