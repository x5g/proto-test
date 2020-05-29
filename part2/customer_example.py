import customer_pb2

PB_FILE_PATH = 'customer.pb'
JSON_FILE_PATH = 'customer.json'

organization = customer_pb2.Organization()
organization.name = 'organization'
customer1 = customer_pb2.Customer()
customer1.id = 1
customer1.firstName = 'Chris'
customer1.lastName = 'Richardson'
email = customer1.email.add()
email.email = 'crichardson@email.com'
email.type = customer1.PROFESSIONAL
organization.customer.append(customer1)
customer2 = customer_pb2.Customer()
customer2.id = 2
customer2.firstName = 'Josh'
customer2.lastName = 'Long'
email = customer2.email.add()
email.email = 'jlong@email.com'
email.type = customer2.PROFESSIONAL
organization.customer.append(customer2)
customer3 = customer_pb2.Customer()
customer3.id = 3
customer3.firstName = 'Matt'
customer3.lastName = 'Stine'
email = customer3.email.add()
email.email = 'mstine@email.com'
email.type = customer3.PROFESSIONAL
organization.customer.append(customer3)
customer4 = customer_pb2.Customer()
customer4.id = 4
customer4.firstName = 'Russ'
customer4.lastName = 'Miles'
email = customer4.email.add()
email.email = 'rmiles@email.com'
email.type = customer4.PROFESSIONAL
organization.customer.append(customer4)

# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(organization.SerializeToString())
f.close()

# 读organization
organization = customer_pb2.Organization()
f = open(PB_FILE_PATH, "rb")
organization.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(organization)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

