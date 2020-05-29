import PersonProto_pb2

PB_FILE_PATH = 'PersonProto.pb'
JSON_FILE_PATH = 'PersonProto.json'

personProto = PersonProto_pb2.PersonProto()
personProto.firstName = 'Jake'
personProto.lastName = 'Partusch'
personProto.emailAddress = 'jakepartusch@abc.com'
personProto.homeAddress = '123 Seasame Street'
phoneNumbers = personProto.phoneNumbers.add()
phoneNumbers.areaCode = 123
phoneNumbers.phoneNumber = 1234567

# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(personProto.SerializeToString())
f.close()

# personProto
personProto = PersonProto_pb2.PersonProto()
f = open(PB_FILE_PATH, "rb")
personProto.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(personProto)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

