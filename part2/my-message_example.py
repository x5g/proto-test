import my_message_pb2

PB_FILE_PATH = 'my-message.pb'
JSON_FILE_PATH = 'my-message.json'

myMessage = my_message_pb2.MyMessage()
myMessage.id = 1981
myMessage.role = myMessage.SERVANT
myMessage.userExternalReference = 'system7'
myMessage.email = 'ahsahs@dsfsdf.com'
myMessage.correlationId = '453454-435345-111-323'



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(myMessage.SerializeToString())
f.close()

# 读myMessage
myMessage = my_message_pb2.MyMessage()
f = open(PB_FILE_PATH, "rb")
myMessage.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(myMessage)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

