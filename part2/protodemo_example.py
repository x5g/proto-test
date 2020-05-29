import protodemo_pb2


PB_FILE_PATH = 'protodemo.pb'
JSON_FILE_PATH = 'protodemo.json'

student = protodemo_pb2.Student()
student.id = 1
student.name = '凌晨1点21分'
student.email = '247600377@qq.com'
student.sex = protodemo_pb2.Student.MAN
phoneNumber = student.phone.add()
phoneNumber.number = '123456789'
phoneNumber.type = protodemo_pb2.Student.PhoneType.HOME


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(student.SerializeToString())
f.close()

# 读addressbook
student = protodemo_pb2.Student()
f = open(PB_FILE_PATH, "rb")
student.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(student)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

