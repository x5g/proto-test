# from Message_pb2 import Request, Response
#
# PB_FILE_PATH_1 = 'Message_1.pb'
# JSON_FILE_PATH_1 = 'Message_1.json'
# PB_FILE_PATH_2 = 'Message_2.pb'
# JSON_FILE_PATH_2 = 'Message_2.json'
#
# request = Request()
# request.type = Request.GET
# request.table = 'request table'
# request.key = 'request key'
# request.value = 'request value'
#
# response = Response()
# response.type = Response.ERROR
# response.error_message = 'response error_message'
# table = response.data.add()
# table.name = 'table'
# table.values['key1'] = 'value1'
# table.values['key2'] = 'value2'
# table.values['key3'] = 'value3'
# response.value.append('value1')
# response.value.append('value2')
# response.value.append('value3')
#
#
# # 以二进制形式保存
# f = open(PB_FILE_PATH_1, "wb")
# f.write(request.SerializeToString())
# f.close()
# f = open(PB_FILE_PATH_2, "wb")
# f.write(response.SerializeToString())
# f.close()
#
# # 读request及response
# request = Request()
# f = open(PB_FILE_PATH_1, "rb")
# request.ParseFromString(f.read())
# f.close()
# response = Response()
# f = open(PB_FILE_PATH_2, "rb")
# response.ParseFromString(f.read())
# f.close()
# from google.protobuf.json_format import MessageToJson   # 关键
# json1 = MessageToJson(request)
# json2 = MessageToJson(response)
# print(json1)
# print(json2)
#
# # 保存json
# f = open(JSON_FILE_PATH_1, "w")
# f.write(json1)
# f.close()
# f = open(JSON_FILE_PATH_2, "w")
# f.write(json2)
# f.close()
#

from Message_pb2 import Request, Response

PB_FILE_PATH = 'Message.pb'
JSON_FILE_PATH = 'Message.json'

response = Response()
response.type = Response.ERROR
response.error_message = 'response error_message'
table = response.data.add()
table.name = 'table'
table.values['key1'] = 'value1'
table.values['key2'] = 'value2'
table.values['key3'] = 'value3'
response.value.append('value1')
response.value.append('value2')
response.value.append('value3')


# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(response.SerializeToString())
f.close()

# 读response
request = Request()
response = Response()
f = open(PB_FILE_PATH, "rb")
response.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(response)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()


