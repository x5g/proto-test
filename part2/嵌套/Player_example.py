import Player_pb2
import vector_pb2

PB_FILE_PATH = 'Player.pb'
JSON_FILE_PATH = 'Player.json'

player = Player_pb2.PlayerPos()
player.playerID = 12345
player.pos.x = 1
player.pos.y = 2
player.pos.z = 3


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(player.SerializeToString())
f.close()

# 读player
player = Player_pb2.PlayerPos()
f = open(PB_FILE_PATH, "rb")
player.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(player)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

