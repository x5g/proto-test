import hello_pb2

PB_FILE_PATH = 'hello.pb'
JSON_FILE_PATH = 'hello.json'

helloArray = hello_pb2.HelloArray()
for i in range(480 * 480):
    helloWorld = hello_pb2.HelloWorld()
    helloWorld.x = i
    helloWorld.y = i
    helloArray.helloWorld.append(helloWorld)


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(helloArray.SerializeToString())
f.close()

# 读helloArray
helloArray = hello_pb2.HelloArray()
f = open(PB_FILE_PATH, "rb")
helloArray.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(helloArray)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

