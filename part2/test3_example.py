import test3_pb2

PB_FILE_PATH = 'test3.pb'
JSON_FILE_PATH = 'test3.json'

login = test3_pb2.Login()
login.SID = '1'
login.RID = 2
login.GPS_LNG = 3
login.GPS_LAT = 4
login.openid = '5'
login.token = '6'



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(login.SerializeToString())
f.close()

# 读login
login = test3_pb2.Login()
f = open(PB_FILE_PATH, "rb")
login.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(login)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

