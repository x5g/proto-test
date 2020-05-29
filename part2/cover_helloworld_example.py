import cover_helloworld_pb2

PB_FILE_PATH = 'cover_helloworld.pb'
JSON_FILE_PATH = 'cover_helloworld.json'

helloworld = cover_helloworld_pb2.helloworld()
helloCoverReq = cover_helloworld_pb2.helloworld.helloCoverReq()
helloCoverRsp = cover_helloworld_pb2.helloworld.helloCoverRsp()
helloCoverRsp.retcode = 0
helloCoverRsp.reply = 'reply from udp server'


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(helloCoverRsp.SerializeToString())
f.close()

# 读helloCoverRsp
helloCoverRsp = cover_helloworld_pb2.helloworld.helloCoverRsp()
f = open(PB_FILE_PATH, "rb")
helloCoverRsp.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(helloCoverRsp)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

