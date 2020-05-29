import demo_pb2
import time

PB_FILE_PATH = 'demo.pb'
JSON_FILE_PATH = 'demo.json'

peticion = demo_pb2.Peticion()
peticion.id = 1234
peticion.user = "username"
peticion.password = "password"
peticion.product = "product"
peticion.amount = 12.34
peticion.account = "12345678"
peticion.date = int(time.time() % 60)




# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(peticion.SerializeToString())
f.close()

# 读addressbook
peticion = demo_pb2.Peticion()
f = open(PB_FILE_PATH, "rb")
peticion.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(peticion)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

