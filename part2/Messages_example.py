import Messages_pb2
import user_pb2

PB_FILE_PATH = 'Messages.pb'
JSON_FILE_PATH = 'Messages.json'

user = user_pb2.Users()
user.id = 1
user.username = 'demo'
user.mobile = '110'
user.email = 'demo@secdomain.com'
mmsg = Messages_pb2.Message()
mmsg.type = Messages_pb2.HOME
mmsg.msgBody = user.SerializeToString()



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(mmsg.SerializeToString())
f.close()

# 读mmsg
mmsg = Messages_pb2.Message()
f = open(PB_FILE_PATH, "rb")
mmsg.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(mmsg)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

