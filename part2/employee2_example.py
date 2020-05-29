import employee2_pb2

PB_FILE_PATH = 'employee2.pb'
JSON_FILE_PATH = 'employee2.json'

employee = employee2_pb2.Employee()
employee.EmployeeId = 1001
employee.FirstName = 'Ishu'
employee.LastName = 'Pathipaka'
employee.Age = 27


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(employee.SerializeToString())
f.close()

# 读employee
employee = employee2_pb2.Employee()
f = open(PB_FILE_PATH, "rb")
employee.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(employee)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

