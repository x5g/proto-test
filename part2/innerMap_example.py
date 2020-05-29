import innerMap_pb2

PB_FILE_PATH = 'innerMap.pb'
JSON_FILE_PATH = 'innerMap.json'

map = innerMap_pb2.Map()
geometry1 = innerMap_pb2.Geometry()
geometry1.type = 'Point'
geometry1.coordinates.extend([12685185.158, 2574231.378])
property1 = innerMap_pb2.Properties()
property1.id = 'B4S-137'
property1.name = 'B4S-137'
property1.icon = ''
property1.x = 12685185.1576
property1.y = 2574231.3784000017
property1.floor = -5
# property1.height = None
# property1.base = None
property1.color = ''
# property1.opacity = ''
property1.layer = 5
floor = innerMap_pb2.Floor()
floor.geometry.append(geometry1)
floor.properties.append(property1)
map.floor.append(floor)

geometry2 = innerMap_pb2.Geometry()
geometry2.coordinates.extend([12685207.296, 2574182.487])
property2 = innerMap_pb2.Properties()
property2.id = "B4N-078"
property2.name = "B4N-078"
property2.icon = ''
property2.x = 12685207.295899998
property2.y = 2574182.4866999984
property2.floor = -5
# property2.height = None
# property2.base = None
property2.color = ''
# property2.opacity = ''
property2.layer = 5
fill = innerMap_pb2.Fill()
fill.geometry.append(geometry2)
fill.properties.append(property2)
map.fill.append(fill)

geometry3 = innerMap_pb2.Geometry()
geometry3.coordinates.extend([12685209.755, 2574182.487])
property3 = innerMap_pb2.Properties()
property3.id = 'B4N-079'
property3.name = 'B4N-079'
property3.icon = ''
property3.x = 12685209.754900001
property3.y = 2574182.4866999984
property3.floor = -5
# property3.height = None
# property3.base = None
property3.color = ''
# property3.opacity = ''
property3.layer = 5
label = innerMap_pb2.Fill()
label.geometry.append(geometry3)
label.properties.append(property3)
map.fill.append(label)



# 以二进制形式保存
f = open(PB_FILE_PATH, "wb")
f.write(map.SerializeToString())
f.close()

# 读map
map = innerMap_pb2.Map()
f = open(PB_FILE_PATH, "rb")
map.ParseFromString(f.read())
f.close()
from google.protobuf.json_format import MessageToJson   # 关键
json = MessageToJson(map)
print(json)

# 保存json
f = open(JSON_FILE_PATH, "w")
f.write(json)
f.close()

