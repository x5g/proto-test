import TimeSchema_pb2

PB_FILE_PATH = 'TimeSchema.pb'
JSON_FILE_PATH = 'TimeSchema.json'

pkg = TimeSchema_pb2.CltSvrPkg()
pHead = pkg.Head
pBody = pkg.Data
pHead.Cmd = TimeSchema_pb2.CMD_HEART
pHead.CmdSeq = 0
pHead.CmdType = 0
pHead.SrcID = 1
pHead.DstID = 2
pHead.UID = 0
pBody.Time.Time = '123456'
pBody.Time.Tick = 0


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(pkg.SerializeToString())
f.close()

# 读pkg
pkg = TimeSchema_pb2.CltSvrPkg()
f = open(PB_FILE_PATH, "rb")
pkg.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(pkg)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

