import Login_pb2

PB_FILE_PATH = 'Login.pb'
JSON_FILE_PATH = 'Login.json'

pbLoginList = Login_pb2.PBLoginList()
for idx in range(1, 50):
    pbLoginField = Login_pb2.PBLoginField()
    pbLoginField.userid = idx
    pbLoginField.szusername = 'xiaohong'
    pbLoginField.szpassword = '2222'
    pbLoginField.remember = True
    pbLoginField.startup = False
    pbLoginList.loginlist.append(pbLoginField)



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(pbLoginList.SerializeToString())
f.close()

# 读pbLoginList
pbLoginList = Login_pb2.PBLoginList()
f = open(PB_FILE_PATH, "rb")
pbLoginList.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(pbLoginList)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

