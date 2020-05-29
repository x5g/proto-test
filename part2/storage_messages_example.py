import storage_messages_pb2

PB_FILE_PATH = 'storage_messages.pb'
JSON_FILE_PATH = 'storage_messages.json'


msgWrapper = storage_messages_pb2.StorageMessageWrapper()
storeChunkMsg = msgWrapper.storeChunkMsg
storeChunkMsg.fileName = 'my_file.txt'
storeChunkMsg.chunkId = 3
storeChunkMsg.data = str.encode('Hello World!')

# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(msgWrapper.SerializeToString())
f.close()

# 读msgWrapper
msgWrapper = storage_messages_pb2.StorageMessageWrapper()
f = open(PB_FILE_PATH, "rb")
msgWrapper.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(msgWrapper)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

