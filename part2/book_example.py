import book_pb2

PB_FILE_PATH = 'book.pb'
JSON_FILE_PATH = 'book.json'

book = book_pb2.Book()
book.name = 'go语言开发'
book.author.name = '张三'



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(book.SerializeToString())
f.close()

# 读book
book = book_pb2.Book()
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

