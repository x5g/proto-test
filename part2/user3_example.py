import user3_pb2

PB_FILE_PATH = 'user3.pb'
JSON_FILE_PATH = 'user3.json'

user = user3_pb2.User()
user.id = '001'
user.name = 'dengyue'
user.role.extend(['GOD', 'ADMIN'])
user.user_type = 'User'
user.user_status = 'Normal'


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(user.SerializeToString())
f.close()

# 读user
user = user3_pb2.User()
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

