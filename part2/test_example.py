import test_pb2

PB_FILE_PATH = 'test.pb'
JSON_FILE_PATH = 'test.json'

person = test_pb2.person()
student1 = test_pb2.student()
student1.name = 'Toy'
student1.age = 21
student1.sex = 'boy'
student2 = test_pb2.student()
student2.name = 'jack'
student2.age = 25
student2.sex = 'boy'
student3 = test_pb2.student()
student3.name = 'lili'
student3.age = 20
student3.sex = 'gril'
person.member.append(student1)
person.member.append(student2)
person.member.append(student3)


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(person.SerializeToString())
f.close()

# 读person
person = test_pb2.person()
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

