import twist_pb2

PB_FILE_PATH = 'twist.pb'
JSON_FILE_PATH = 'twist.json'

twist = twist_pb2.Twist()
twist.linear.x = 1
twist.linear.y = 2
twist.linear.z = 3
twist.angular.x = 4
twist.angular.y = 5
twist.angular.z = 6


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(twist.SerializeToString())
f.close()

# 读twist
twist = twist_pb2.Twist()
f = open(PB_FILE_PATH, "rb")
twist.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(twist)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

