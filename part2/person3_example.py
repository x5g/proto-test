import person3_pb2

PB_FILE_PATH = 'person3.pb'
JSON_FILE_PATH = 'person3.json'

person = person3_pb2.Person()
person.name = 'John'
person.nickname = 'Johnny'
person.gender = person3_pb2.Person.MALE
person.friends.extend(['Maria', 'Joseph', "David"])


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(person.SerializeToString())
f.close()

# 读person
person = person3_pb2.Person()
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

