import Rule_pb2

PB_FILE_PATH = 'Rule.pb'
JSON_FILE_PATH = 'Rule.json'

rule = Rule_pb2.Rule()
rule.name = 'Test Name'
rule.priority = 99999
rule.description = 'This is a demo rule'
rule.action = 'Test Action'
rule.condition = 'Test Condition'


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(rule.SerializeToString())
f.close()

# 读rule
rule = Rule_pb2.Rule()
f = open(PB_FILE_PATH, "rb")
rule.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(rule)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

