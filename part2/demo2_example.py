import demo2_pb2

PB_FILE_PATH = 'demo2.pb'
JSON_FILE_PATH = 'demo2.json'

person = demo2_pb2.PersonMsg()
person.id = 24
person.firstName = 'Alex'
person.lastName = 'Bondar'
person.email = 'alex@startup.com'
person.emp = demo2_pb2.PersonMsg.DEVELOPER
department = person.department
department.departmentName = 'Advanced and experimental development'

# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(person.SerializeToString())
f.close()

# person
person = demo2_pb2.PersonMsg()
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

