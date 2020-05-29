import demo4_pb2

PB_FILE_PATH = 'demo4.pb'
JSON_FILE_PATH = 'demo4.json'

class_ = demo4_pb2.Class()
class_.name = '三年级23班'
teacher = demo4_pb2.Teacher()
teacher.name = 'tom'
teacher.age = 17
teacher.work.isworker = 1
teacher.work.isjiaban = 1
class_.teacher.append(teacher)
student1 = demo4_pb2.Student()
student1.age = 19
student1.name = 'demo'
student1.grade = 134
class_.stu.append(student1)
student2 = demo4_pb2.Student()
student2.age = 19
student2.name = 'google'
student2.grade = 134
class_.stu.append(student2)

# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(class_.SerializeToString())
f.close()

# 读class_
class_ = demo4_pb2.Class()
f = open(PB_FILE_PATH, "rb")
class_.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(class_)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

