import MessageData_pb2
import random

PB_FILE_PATH = 'MessageData.pb'
JSON_FILE_PATH = 'MessageData.json'

messageData = MessageData_pb2.MessageData()
messageData.content = str.encode(str(random.randint(0, 65535)))
sysHeader = messageData.sysHeader
sysHeader.bizSeqNo = str(random.random())
sysHeader.sysSeqNo = str(random.random())
sysHeader.ip = str(random.random())
sysHeader.userId = str(random.random())
sysHeader.version = random.randint(0, 65535)
sysHeader.channelId = str(random.random())
sysHeader.origSysId = str(random.random())
sysHeader.prevSysId = str(random.random())

# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(messageData.SerializeToString())
f.close()

# 读messageData
messageData = MessageData_pb2.MessageData()
f = open(PB_FILE_PATH, "rb")
messageData.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(messageData)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()


