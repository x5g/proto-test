import product2_pb2

PB_FILE_PATH = 'product2.pb'
JSON_FILE_PATH = 'product2.json'

productList = product2_pb2.ProductList()
product1 = product2_pb2.Product()
product1.ID = '1'
product1.Name = 'Samsung Galaxy S10'
product1.Quantity = 10
product1.Images.extend(['img1', 'img2'])
productList.Products.append(product1)
product2 = product2_pb2.Product()
product2.ID = '2'
product2.Name = 'iPhone X'
product2.Quantity = 12
product2.Images.extend(['img3', 'img4'])
productList.Products.append(product2)


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(productList.SerializeToString())
f.close()

# 读productList
productList = product2_pb2.ProductList()
f = open(PB_FILE_PATH, "rb")
productList.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(productList)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

