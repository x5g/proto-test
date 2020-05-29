import user2_pb2

PB_FILE_PATH = 'user2.pb'
JSON_FILE_PATH = 'user2.json'

userResponse = user2_pb2.UserResponse()
userResponse.id = 111
userResponse.name = 'name'
userResponse.age = 222
userResponse.title.append('title1')
userResponse.title.append('title2')
userResponse.title.append('title3')
userResponse.title.append('title4')
userResponse.title.append('title5')


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(userResponse.SerializeToString())
f.close()

# 读userResponse
userResponse = user2_pb2.UserResponse()
f = open(PB_FILE_PATH, "rb")
userResponse.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(userResponse)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

