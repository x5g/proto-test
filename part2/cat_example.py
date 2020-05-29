import cat_pb2

PB_FILE_PATH = 'cat.pb'
JSON_FILE_PATH = 'cat.json'

newCat = cat_pb2.Cat()
dave = cat_pb2.Cat.Parent()
dave.name = 'Dave'
dave.email = 'nope@google.com'
newCat.name = 'Sonny'
newCat.age = 10
newCat.parents.append(dave)


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(newCat.SerializeToString())
f.close()

# 读newCat
newCat = cat_pb2.Cat()
f = open(PB_FILE_PATH, "rb")
newCat.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(newCat)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

