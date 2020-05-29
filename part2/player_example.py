import player_pb2

PB_FILE_PATH = 'player.pb'
JSON_FILE_PATH = 'player.json'

players = player_pb2.Players()
player1 = player_pb2.Player()
player1.id = '1'
player1.name = '1'
for i in range(10):
    player1.scores.append(i)
player2 = player_pb2.Player()
player2.id = '1'
player2.name = '1'
for i in range(10, 20):
    player2.scores.append(i)
players.players.append(player1)
players.players.append(player2)




# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(players.SerializeToString())
f.close()

# 读players
players = player_pb2.Players()
f = open(PB_FILE_PATH, "rb")
players.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(players)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

