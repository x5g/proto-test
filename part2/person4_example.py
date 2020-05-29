import person4_pb2

PB_FILE_PATH = 'person4.pb'
JSON_FILE_PATH = 'person4.json'

personTom = person4_pb2.Person()
personTom.name = 'Tom'
personTom.age = 32
personTom.socialMediaProfiles.linkedin = 'http://www.linkedin.com/users/tom-smith'
personTom.socialMediaProfiles.twitter = 'na'


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(personTom.SerializeToString())
f.close()

# 读personTom
personTom = person4_pb2.Person()
f = open(PB_FILE_PATH, "rb")
personTom.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(personTom)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

