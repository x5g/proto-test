import Person_pb2
import SearchResponse_pb2
import Result_pb2

PB_FILE_PATH = 'Person.pb'
JSON_FILE_PATH = 'Person.json'

phoneNumber = Person_pb2.PhoneNumber()
phoneNumber.number = '000-0001'
phoneNumber.type = Person_pb2.PhoneNumber.WORK

# searchResponse = SearchResponse_pb2.SearchResponse()
searchResponse = phoneNumber.searchResponse
result1 = Result_pb2.Result()
result1.url = 'result1.url'
result1.title = 'result1.title'
result1.snippets.extend(['result1.snippets1', 'result1.snippets2'])
searchResponse.results.append(result1)
result2 = Result_pb2.Result()
result2.url = 'result2.url'
result2.title = 'result2.title'
result2.snippets.extend(['result2.snippets1', 'result2.snippets2'])
searchResponse.results.append(result2)

# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(phoneNumber.SerializeToString())
f.close()

# 读phoneNumber
phoneNumber = Person_pb2.PhoneNumber()
f = open(PB_FILE_PATH, "rb")
phoneNumber.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(phoneNumber)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

