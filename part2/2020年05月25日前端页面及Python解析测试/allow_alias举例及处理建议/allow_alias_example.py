import allow_alias_pb2

PB_FILE_PATH = 'allow_alias.pb'
JSON_FILE_PATH = 'allow_alias.json'

book = allow_alias_pb2.Book()
book.isbn = 1001
book.title = 'title'
book.author = 'author'
book.status = allow_alias_pb2.Status.RUNNING


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(book.SerializeToString())
f.close()

# 读m
book = allow_alias_pb2.Book()
f = open(PB_FILE_PATH, "rb")
book.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(book)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

