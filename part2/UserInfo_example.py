import UserInfo_pb2
import random

PB_FILE_PATH = 'UserInfo.pb'
JSON_FILE_PATH = 'UserInfo.json'

listOfUsers = UserInfo_pb2.ListOfUsers()
for i in range(10):
    user = listOfUsers.users.add()
    user.account = str(random.random())
    user.password = str(random.random())

# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(listOfUsers.SerializeToString())
f.close()

# 读addressbook
listOfUsers = UserInfo_pb2.ListOfUsers()
f = open(PB_FILE_PATH, "rb")
listOfUsers.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(listOfUsers)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

