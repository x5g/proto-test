import Account_pb2

PB_FILE_PATH = 'Account.pb'
JSON_FILE_PATH = 'Account.json'

employeeName = Account_pb2.EmployeeName()
employeeName.first_name = "John"
employeeName.last_name = "Doe"




# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(employeeName.SerializeToString())
f.close()

# 读employeeName
employeeName = Account_pb2.EmployeeName()
f = open(PB_FILE_PATH, "rb")
employeeName.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(employeeName)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

