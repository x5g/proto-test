import student_pb2

PB_FILE_PATH = 'student.pb'
JSON_FILE_PATH = 'student.json'

student = student_pb2.Student()
student.name = '廖翀'
student.address = '北京'

# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(student.SerializeToString())
f.close()

# 读student
student = student_pb2.Student()
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

