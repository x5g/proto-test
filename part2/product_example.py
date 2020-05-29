import product_pb2

PB_FILE_PATH = 'product.pb'
JSON_FILE_PATH = 'product.json'

p = product_pb2.Product()
p.ID = '001'
p.Name = 'Nokia 6'
p.Quantity = 5
image = ['wuriyanto.com/img1', 'wuriyanto.com/img2']
p.Images.extend(image)


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(p.SerializeToString())
f.close()

# 读product
p = product_pb2.Product()
f = open(PB_FILE_PATH, "rb")
p.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(p)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

