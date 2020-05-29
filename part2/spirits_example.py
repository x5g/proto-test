import spirits_pb2

PB_FILE_PATH = 'spirits.pb'
JSON_FILE_PATH = 'spirits.json'

spirit = spirits_pb2.Spirit()
spirit.Id = '1'
spirit.Name = 'Chti beer'
spirit.Distiller = 'DevFest Lille'
spirit.Bottler = 'Seb'
spirit.Country = 'France'
spirit.Region = 'NPDC'
spirit.Composition = 'Malt, Houblon'
spirit.type = spirits_pb2.Spirit.TypeUnspecified
spirits_pb2.Age = 10
spirits_pb2.BottlingDate = 0
spirits_pb2.Score = 11
spirits_pb2.Comment = 'Hello Beer Drinkers !'



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(spirit.SerializeToString())
f.close()

# 读spirit
spirit = spirits_pb2.Spirit()
f = open(PB_FILE_PATH, "rb")
spirit.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(spirit)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

