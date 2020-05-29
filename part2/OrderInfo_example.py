import OrderInfo_pb2
import random

PB_FILE_PATH = 'OrderInfo.pb'
JSON_FILE_PATH = 'OrderInfo.json'

orderInfo = OrderInfo_pb2.OrderInfo()
orderInfo.orderId = str(random.random())
orderInfo.userId = 'pinkpig'
orderInfo.orderPrice = 100.00
orderInfo.deliveryPrice = 20.00
orderInfo.deliveryMethod = '京东物流'
orderInfo.receiverName = 'pinkpig'
orderInfo.receiverAddress = '广东省深圳市宝安区西乡街道'
orderInfo.orderDatetime = '20190728231800'
orderInfo.payMethod = '微信支付'
orderInfo.payDatetime = '20190728232000'

# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(orderInfo.SerializeToString())
f.close()

# 读addressbook
orderInfo = OrderInfo_pb2.OrderInfo()
f = open(PB_FILE_PATH, "rb")
orderInfo.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(orderInfo)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

