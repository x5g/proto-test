import ProtocolModule_pb2

PB_FILE_PATH = 'ProtocolModule.pb'
JSON_FILE_PATH = 'ProtocolModule.json'

commonProtocol = ProtocolModule_pb2.CommonProtocol()
commonHeader = commonProtocol.CommHeader
commonHeader.CommandId = 0x000100FF
commonHeader.SeqId = 1000
commonHeader.Version = 1

liveCommonHeader = commonProtocol.LiveHeader
liveCommonHeader.LiveType = 1
liveCommonHeader.LiveId = 1
liveCommonHeader.DemandType = 1
liveCommonHeader.DemandId = 1



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(commonProtocol.SerializeToString())
f.close()

# 读addressbook
commonProtocol = ProtocolModule_pb2.CommonProtocol()
f = open(PB_FILE_PATH, "rb")
commonProtocol.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(commonProtocol)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

