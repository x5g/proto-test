import person_pb2

PB_FILE_PATH = 'person.pb'
JSON_FILE_PATH = 'person.json'

person = person_pb2.Person()
person.id = 1
person.name = 'caojiafa'
person.email = 'caojiafa@imomo.com'


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(person.SerializeToString())
f.close()

# 读person
person = person_pb2.Person()
f = open(PB_FILE_PATH, "rb")
person.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(person)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

