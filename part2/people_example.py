from people_pb2 import People

PB_FILE_PATH = 'people.pb'
JSON_FILE_PATH = 'people.json'

people = People()
people.id = 2
people.name = "deli"
people.email = "lytsing@hotmail.com"


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(people.SerializeToString())
f.close()

# 读addressbook
people = People()
f = open(PB_FILE_PATH, "rb")
people.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(people)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

