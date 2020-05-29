import yages_schema_pb2

PB_FILE_PATH = 'yages-schema.pb'
JSON_FILE_PATH = 'yages-schema.json'

content = yages_schema_pb2.Content()
content.text = 'text'



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(content.SerializeToString())
f.close()

# 读content
content = yages_schema_pb2.Content()
f = open(PB_FILE_PATH, "rb")
content.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(content)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

