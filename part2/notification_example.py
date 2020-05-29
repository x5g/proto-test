import notification_pb2

PB_FILE_PATH = 'notification.pb'
JSON_FILE_PATH = 'notification.json'

notificationDTD = notification_pb2.NotificationDTO()
notificationDTD.message = 'Rabbit mq is there'
import time
notificationDTD.sentAt = str(time.time())


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(notificationDTD.SerializeToString())
f.close()

# 读notificationDTD
notificationDTD = notification_pb2.NotificationDTO()
f = open(PB_FILE_PATH, "rb")
notificationDTD.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(notificationDTD)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

