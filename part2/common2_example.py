import common2_pb2

PB_FILE_PATH = 'common2.pb'
JSON_FILE_PATH = 'common2.json'

m_1101_toc = common2_pb2.m_1101_toc()
m_1101_toc.cmd = 10101
m_1101_toc.error_code = 20202
m_1101_toc.description = '30303'

# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(m_1101_toc.SerializeToString())
f.close()

# 读m_1101_toc
m_1101_toc = common2_pb2.m_1101_toc()
f = open(PB_FILE_PATH, "rb")
m_1101_toc.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(m_1101_toc)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

