import tallMessage_pb2

PB_FILE_PATH = 'tallMessage.pb'
JSON_FILE_PATH = 'tallMessage.json'

testTallMessage = tallMessage_pb2.TestTallMessage()
testTallMessage.count = 1
testTallMessage.data0 = '2'
testTallMessage.data1 = '3'
testTallMessage.data2 = '4'
testTallMessage.data3 = '5'
testTallMessage.data4 = '6'
testTallMessage.data5 = '7'
testTallMessage.data6 = '8'
testTallMessage.data7 = '9'
testTallMessage.data8 = '10'
testTallMessage.data9 = '11'
testTallMessage.data10 = '12'
testTallMessage.data11 = '13'
testTallMessage.data12 = '14'
testTallMessage.data13 = '15'
testTallMessage.data14 = '16'
testTallMessage.data15 = '17'
testTallMessage.data16 = '18'
testTallMessage.data17 = '19'
testTallMessage.data18 = '20'
testTallMessage.data19 = '21'
testTallMessage.data20 = '22'
testTallMessage.data21 = '23'
testTallMessage.data22 = '24'
testTallMessage.data23 = '25'
testTallMessage.data24 = '26'
testTallMessage.isFinal = False



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(testTallMessage.SerializeToString())
f.close()

# 读testTallMessage
testTallMessage = tallMessage_pb2.TestTallMessage()
f = open(PB_FILE_PATH, "rb")
testTallMessage.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(testTallMessage)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

