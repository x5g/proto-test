import chat_pb2

PB_FILE_PATH = 'chat.pb'
JSON_FILE_PATH = 'chat.json'

tocChat = chat_pb2.TocChat()
tocChat.name = 'tocChat.name'
tocChat.content = 'tocChat.content'


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(tocChat.SerializeToString())
f.close()

# 读tocChat
tocChat = chat_pb2.TocChat()
f = open(PB_FILE_PATH, "rb")
tocChat.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(tocChat)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

