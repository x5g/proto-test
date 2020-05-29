import addressbook3_pb2

PB_FILE_PATH = 'addressbook3.pb'
JSON_FILE_PATH = 'addressbook3.json'

addresses = addressbook3_pb2.AddressBook()

alice = addresses.people.add()
alice.id = 123
alice.name = 'Alice'
alice.email = "alice@example.com"
phone = alice.phones.add()
phone.type = phone.MOBILE
phone.number = "555-1212"

bob = addresses.people.add()
bob.id = 456
bob.name = 'Bob'
bob.email = 'bob@example.com'
bobPhone0 = bob.phones.add()
bobPhone0.type = phone.HOME
bobPhone0.number = "555-4567"
bobPhone1 = bob.phones.add()
bobPhone1.type = phone.WORK
bobPhone1.number = "555-7654"

# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(addresses.SerializeToString())
f.close()

# 读addressbook
addresses = addressbook3_pb2.AddressBook()
f = open(PB_FILE_PATH, "rb")
addresses.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(addresses)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()
