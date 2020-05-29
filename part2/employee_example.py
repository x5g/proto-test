import employee_pb2

PB_FILE_PATH = 'employee.pb'
JSON_FILE_PATH = 'employee.json'

employeeResponse = employee_pb2.EmployeeResponse()
employeeDetails = employeeResponse.message
employeeDetails.id = 1
employeeDetails.email = 'abcd@abcd.com'
employeeDetails.firstName = 'First1'
employeeDetails.lastName = 'Last1'



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(employeeResponse.SerializeToString())
f.close()

# 读employeeResponse
employeeResponse = employee_pb2.EmployeeResponse()
f = open(PB_FILE_PATH, "rb")
employeeResponse.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(employeeResponse)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

