import SearchResponse_pb2
import Result_pb2

PB_FILE_PATH = 'SearchResponse.pb'
JSON_FILE_PATH = 'SearchResponse.json'

searchResponse = SearchResponse_pb2.SearchResponse()
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
f.write(searchResponse.SerializeToString())
f.close()

# 读searchResponse
searchResponse = SearchResponse_pb2.SearchResponse()
f = open(PB_FILE_PATH, "rb")
searchResponse.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(searchResponse)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

