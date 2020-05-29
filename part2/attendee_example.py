import attendee_pb2

PB_FILE_PATH = 'attendee.pb'
JSON_FILE_PATH = 'attendee.json'

attendee = attendee_pb2.Attendee()
attendee.first_name = 'John Json'
attendee.last_name = 'Doe'
address = attendee.address
address.city = 'Bristol'
address.street = "Canon's Road"
address.number = 1


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(attendee.SerializeToString())
f.close()

# 读attendee
attendee = attendee_pb2.Attendee()
f = open(PB_FILE_PATH, "rb")
attendee.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(attendee)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

