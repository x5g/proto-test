import msginfo_pb2

PB_FILE_PATH = 'msginfo.pb'
JSON_FILE_PATH = 'msginfo.json'

msgRecv = msginfo_pb2.CMsgReg()
msgRecv.area = 1
msgRecv.region = 1
msgRecv.shop = 1
msgRecv.ret = 1



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(msgRecv.SerializeToString())
f.close()

# 读msgRecv
msgRecv = msginfo_pb2.CMsgReg()
f = open(PB_FILE_PATH, "rb")
msgRecv.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(msgRecv)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

