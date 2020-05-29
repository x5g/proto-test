# 硬编码式新建person及addressbook
from addressbook_pb2 import Person, AddressBook

PB_FILE_PATH = 'addressbook.pb'
JSON_FILE_PATH = 'addressbook.json'

addressbook = AddressBook()
people = addressbook.people.add()
people.id = 1234
people.name = "John Doe"
people.email = "jdoe@example.com"
phone = people.phones.add()
phone.number = "555-4321"
phone.type = Person.HOME

# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(addressbook.SerializeToString())
f.close()

# 读addressbook
addressbook = AddressBook()
f = open(PB_FILE_PATH, "rb")
addressbook.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(addressbook)
print(MessageToJson(addressbook))

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

