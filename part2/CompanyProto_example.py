import CompanyProto_pb2

PB_FILE_PATH = 'CompanyProto.pb'
JSON_FILE_PATH = 'CompanyProto.json'

company = CompanyProto_pb2.Compay()
company.id = 1
company.name = 'Global Company'
company.address = 'any where'
company.contact.append('66666660')
company.contact.append('66666661')
company.website = 'www.google.com'
company.type = CompanyProto_pb2.Compay.PRIVATE
staff1 = CompanyProto_pb2.Staff()
staff1.id = 10001
staff1.userName = 'Peter Jeff'
staff1.sex = CompanyProto_pb2.Staff.MALE
staff1.age = 28
staff1.department = 'Dev'
staff1.job = 'Java'
staff1.phoneNums.append('05812345678')
staff2 = CompanyProto_pb2.Staff()
staff2.id = 10001
staff2.userName = 'Jack Allen'
staff2.sex = CompanyProto_pb2.Staff.FEMALE
staff2.age = 32
staff2.department = 'HR'
staff2.job = 'manager'
staff2.phoneNums.append('05899999999')
staff2.phoneNums.append('05899999900')
company.staffs.append(staff1)
company.staffs.append(staff2)

# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(company.SerializeToString())
f.close()

# 读addressbook
company = CompanyProto_pb2.Compay()
f = open(PB_FILE_PATH, "rb")
company.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(company)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

