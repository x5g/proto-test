import service_pb2

PB_FILE_PATH_1 = 'service_1.pb'
JSON_FILE_PATH_1 = 'service_1.json'
PB_FILE_PATH_2 = 'service_2.pb'
JSON_FILE_PATH_2 = 'service_2.json'

req = service_pb2.GetWeatherRequest()
req.city = "Austin"
req.days = 3

r = service_pb2.GetWeatherResponse()
wi = r.weatherinfo.add()
wi.city = req.city
wi.date = "2017-04-08"
wi.temperature_low = 57
wi.temperature_high = 67
wi.wind = 10
wi.humidity = 72
wi = r.weatherinfo.add()
wi.city = req.city
wi.date = "2017-04-09"
wi.temperature_low = 58
wi.temperature_high = 68
wi.wind = 12
wi.humidity = 80

# 以二进制形式保存
f = open(PB_FILE_PATH_1, "wb")
f.write(req.SerializeToString())
f.close()

f = open(PB_FILE_PATH_2, "wb")
f.write(r.SerializeToString())
f.close()

# 读req及r
req = service_pb2.GetWeatherRequest()
f = open(PB_FILE_PATH_1, "rb")
req.ParseFromString(f.read())
f.close()
r = service_pb2.GetWeatherResponse()
f = open(PB_FILE_PATH_2, "rb")
r.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json1 = MessageToJson(req)
json2 = MessageToJson(r)
print(json1)
print(json2)

# 保存json
f = open(JSON_FILE_PATH_1, "w")
f.write(json1)
f.close()

f = open(JSON_FILE_PATH_2, "w")
f.write(json2)
f.close()

