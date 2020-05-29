import dog_pb2

PB_FILE_PATH = 'dog.pb'
JSON_FILE_PATH = 'dog.json'

dog = dog_pb2.Dog()
dog.barks = True
dog.yearsold = 6



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(dog.SerializeToString())
f.close()

# 读dog
dog = dog_pb2.Dog()
f = open(PB_FILE_PATH, "rb")
dog.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(dog)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

