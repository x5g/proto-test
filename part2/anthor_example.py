import anthor_pb2

PB_FILE_PATH = 'anthor.pb'
JSON_FILE_PATH = 'anthor.json'

anthor = anthor_pb2.Author()
anthor.id = 5
anthor.Name = 'Dostoyevski'
book1 = anthor_pb2.Book()
book1.id = 1
book1.name = 'Kumarbaz'
book1.type = anthor_pb2.PAPER
book2 = anthor_pb2.Book()
book2.id = 2
book2.name = 'Beyaz Geceler'
book2.type = anthor_pb2.PAPER
book3 = anthor_pb2.Book()
book3.id = 3
book3.name = 'Yeraltindan Notlar'
book3.type = anthor_pb2.EBOOK
anthor.books.append(book1)
anthor.books.append(book2)
anthor.books.append(book3)


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(anthor.SerializeToString())
f.close()

# 读anthor
anthor = anthor_pb2.Author()
f = open(PB_FILE_PATH, "rb")
anthor.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(anthor)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

