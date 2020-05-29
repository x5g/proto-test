import fight_pb2

PB_FILE_PATH = 'fight.pb'
JSON_FILE_PATH = 'fight.json'

enterFight = fight_pb2.EnterFight()
enterFight.name = 'Tom'
enterFight.content = 'i m in'



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(enterFight.SerializeToString())
f.close()

# 读enterFight
enterFight = fight_pb2.EnterFight()
f = open(PB_FILE_PATH, "rb")
enterFight.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(enterFight)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

