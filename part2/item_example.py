import item_pb2

PB_FILE_PATH = 'item.pb'
JSON_FILE_PATH = 'item.json'

collection = item_pb2.Collection()
item1 = item_pb2.Item()
item1.id = '001'
item1.name = '100'
item2 = item_pb2.Item()
item2.id = '010'
item2.name = '010'
item3 = item_pb2.Item()
item3.id = '100'
item3.name = '001'
collection.items.append(item1)
collection.items.append(item2)
collection.items.append(item3)



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(collection.SerializeToString())
f.close()

# 读collection
collection = item_pb2.Collection()
f = open(PB_FILE_PATH, "rb")
collection.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(collection)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

