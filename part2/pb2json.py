import re
import struct
import json
import sys
import base64

# 输入参数不足
class Error510(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# 读取.proto文件失败
class Error511(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# .proto版本错误:未知版本
class Error512(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# .proto版本错误:指定多个版本
class Error513(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# <packed>选项为布尔变量
class Error514(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# 属性中出现错误选项:proto2支持<default>和<packed>;proto3只支持<packed>;且<packed>仅用于repeated primitive fields
class Error515(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# 属性中出现错误修饰词:proto2支持<required>,<optional>和<repeated>,必须显式声明;proto3支持<singular>和<repeated>,默认为<singular>
class Error516(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# 读取pb数据失败
class Error517(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# proto中可获得的wire types为:<type 0>,<type 1>,<type 2>,<type 5>;<type 3>和<type 4>已经废弃
class Error518(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# 解析pb数据时发生错误,不应该发生的错误
class Error519(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# proto2中,required修饰的属性必填
class Error520(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# 默认值与类型不符
class Error521(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# 自定义类型不能设置默认值
class Error522(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# 解析失败
class Error523(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# 变量ID不允许相同, enum中ID相同需要设置<option allow_alias = true;>选项
class Error524(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# 含有多个extensions
class Error525(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# 出现同名的message
class Error526(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# 只有proto2支持extend
class Error527(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# extend ID超出支持的范围
class Error528(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# enum中值不存在
class Error529(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# 未知错误
class Error530(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TypeParser(dict):

    # 获取字节中的最高位
    def __getMostBit(self, Byte):
        return (Byte >> 7) & 0b1

    def __parseVarint(self, data):
        index = 0
        end = data.__len__()
        while index < end:
            shiftLeft = 0
            rawData = data[index] & 0b1111111
            while self.__getMostBit(data[index]) == 1:
                index += 1
                shiftLeft += 7
                rawData += (data[index] & 0b1111111) << shiftLeft
            yield (rawData,shiftLeft//8+1)
            index += 1

    def __parseZigZag(self,data):
        if data % 2 == 0:
            value = data // 2
        else:
            value = - (data + 1) // 2
        return value

    def __parseFixedData(self,data,pieceSize):
        index = 0
        end = data.__len__()
        while index < end:
            rawData = data[index:index+pieceSize]
            yield rawData
            index += pieceSize

    def __int32(self, data, adjunct=None):
        if adjunct == 'repeated':
            value = []
            for rawData,dataSize in self.__parseVarint(data):
                if dataSize == 8:
                    value.append(struct.unpack('q',rawData.to_bytes(8,byteorder='big'))[0])
                else:
                    value.append(rawData)
        else:
            value = data
            if value > 9223372036854775807:
                value = -(18446744073709551616 - value)
        return value

    def __int64(self, data, adjunct=None):
        return self.__int32(data, adjunct)

    def __uint32(self, data, adjunct=None):
        if adjunct == 'repeated':
            value = []
            for rawData,dataSize in self.__parseVarint(data):
                value.append(rawData)
        else:
            value = data
        return value

    def __uint64(self, data, adjunct=None):
        return self.__uint32(data,adjunct)

    def __sint32(self, data, adjunct=None):
        if adjunct == 'repeated':
            value = []
            for rawData,dataSize in self.__parseVarint(data):
                value.append(self.__parseZigZag(rawData))
        else:
            value = self.__parseZigZag(data)
        return value

    def __sint64(self, data, adjunct=None):
        return self.__sint32(data,adjunct)

    def __fixed32(self, data, adjunct=None):
        if adjunct == 'repeated':
            value = []
            for rawData in self.__parseFixedData(data,4):
                value.append(struct.unpack('i',rawData)[0])
        else:
            value = struct.unpack('i',data)[0]
        return value

    def __fixed64(self, data, adjunct=None):
        if adjunct == 'repeated':
            value = []
            for rawData in self.__parseFixedData(data,8):
                value.append(struct.unpack('q',rawData)[0])
        else:
            value = struct.unpack('q',data)[0]
        return value

    def __sfixed32(self, data, adjunct=None):
        if adjunct == 'repeated':
            value = []
            for rawData in self.__parseFixedData(data,4):
                value.append(struct.unpack('i',rawData)[0])
        else:
            value = struct.unpack('i',data)[0]
        return value

    def __sfixed64(self, data, adjunct=None):
        if adjunct == 'repeated':
            value = []
            for rawData in self.__parseFixedData(data,8):
                value.append(struct.unpack('q',rawData)[0])
        else:
            value = struct.unpack('q',data)[0]
        return value

    def __float(self, data, adjunct=None):
        if adjunct == 'repeated':
            value = []
            for rawData in self.__parseFixedData(data,4):
                value.append(struct.unpack('f',rawData)[0])
        else:
            value = struct.unpack('f',data)[0]
        return value

    def __double(self, data, adjunct=None):
        if adjunct == 'repeated':
            value = []
            for rawData in self.__parseFixedData(data,8):
                value.append(struct.unpack('d',rawData)[0])
        else:
            value = struct.unpack('d',data)[0]
        return value

    def __bool(self, data, adjunct=None):
        if adjunct == 'repeated':
            value = []
            for rawData in self.__parseFixedData(data,1):
                value.append(struct.unpack('?',rawData)[0])
        else:
            value = data!=0
        return value

    def __string(self, data, adjunct=None):
        return str(data,encoding='utf-8')

    def __bytes(self, data, adjunct=None):
        return str(base64.b64encode(data),encoding='utf-8')
        # return str(data,encoding='utf-8')

    def __enum(self, data, adjunct=None):
        if adjunct == 'repeated':
            value = []
            for rawData,dataSize in self.__parseVarint(data):
                value.append(rawData)
        else:
            value = data
        return value

    def __init__(self, iterable={}):
        super().__init__(iterable)
        self['int32'] =  self.__int32
        self['int64'] =  self.__int64
        self['uint32'] =  self.__uint32
        self['uint64'] =  self.__uint64
        self['sint32'] =  self.__sint32
        self['sint64'] =  self.__sint64
        self['fixed32'] =  self.__fixed32
        self['fixed64'] =  self.__fixed64
        self['sfixed32'] =  self.__sfixed32
        self['sfixed64'] =  self.__sfixed64
        self['float'] =  self.__float
        self['double'] =  self.__double
        self['bool'] =  self.__bool
        self['string'] =  self.__string
        self['bytes'] =  self.__bytes
        self['enum'] =  self.__enum


class Pb2Json:
    __reDeleteNote = re.compile(r'''\/\/.*''')
    __reGetProtoVersion = re.compile(r'''syntax *= *"(\S*?)" *;''')
    __reGetMessage = re.compile(r'''(?P<messageType>message|enum|extend|oneof)\s*(?P<messageName>.\S*?)\s*\{''')
    __reFindMessageEnd = re.compile(r'''\{|\}''')
    __reAllowAlias = re.compile(r'''option\s+allow_alias\s*=\s*true\s*;''')
    __reParseField = re.compile(r'''((?P<adjunct>required|optional|repeated|singular)\s+)?((?P<className>[^=\s;<]+?)\s+|(?P<map>map\s*<\s*(?P<mapKey>[^=\s;]+?)\s*,\s*(?P<mapValue>[^=\s;]+?)\s*>\s*))?(?P<fieldName>[^=\s;>]+?)\s*=\s*(?P<fieldID>\d+?)\s*(\[\s*(?P<optionName>[^=\s;]+?)\s*=\s*(["']?)(?P<optionValue>[^=\s;]+?)(["']?)\s*\]\s*)?;''')
    __reExtendRange = re.compile(r'''extensions\s*(?P<extendStart>\d+)\s*to\s*(?P<extendEnd>\d+);''')

    def __init__(self, protoFilePath=None, PBFilePath=None):
        self.__version = ''
        self.__messages = {}
        self.__data = {}
        self.result = {}
        self.__typeParser = TypeParser()
        if protoFilePath !=None:
            self.loadProto(protoFilePath)
        if PBFilePath !=None:
            self.loadPB(PBFilePath)
        self.__primitiveType = ['int32', 'int64', 'uint32', 'uint64', 'sint32', 'sint64', 'fixed32', 'fixed64', 'sfixed32', 'sfixed64', 'float', 'double', 'bool']
        self.__builtinType = ['string', 'bytes']
        self.__enumType = []
        self.__expandType = []
        self.__expandMessages = []
        self.__oneOfMessages = []

    # 删除注释
    def __deleteNote(self, data):
        return self.__reDeleteNote.sub('', data)
    
    # 版本判断,目前只处理proto3
    def __versionJudge(self, data):
        versionList = self.__reGetProtoVersion.findall(data)
        # if len(versionList)!= 1 or versionList[0]!= 'proto3':
        if len(versionList) == 1:
            self.__version = versionList[0]
        elif len(versionList) == 0:
            self.__version = 'proto2'
        else:
            raise Error513
        return self.__reGetProtoVersion.sub('', data)

    def __findMessageContentEnd(self,data):
        brackets = 1
        for match in self.__reFindMessageEnd.finditer(data):
            if match.group() == '{':
                brackets += 1
            elif match.group() == '}':
                brackets -= 1
            if brackets == 0:
                return match.start()

    # 获得所有Message
    def __getMessage(self, parent='', data=None):
        if data == None:
            data = self.__deleteNote(self.protoFile)
            data = self.__versionJudge(data)
        
        message = self.__reGetMessage.search(data)
        messageName = ''
        while message:
            messageName = message.groupdict()['messageName']
            messageType = message.groupdict()['messageType']
            messageContentStart = message.end()
            messageContentEnd = messageContentStart + self.__findMessageContentEnd(data[messageContentStart:])
            content,child = self.__getMessage(messageName, data[messageContentStart:messageContentEnd])
            key = (messageName,parent,child,messageType)
            self.__messages[key] = content
            data = data[:message.start()] + data[messageContentEnd+1:]
            message = self.__reGetMessage.search(data)
        return data,messageName

    # 解析message
    def __parseMessage(self):
        messages = {}
        for key in list(self.__messages.keys()):
            value = {}
            value['parent'] = key[1]
            value['child'] = key[2]
            value['class'] = key[3]
            for match in self.__reParseField.finditer(self.__messages[key]):
                fieldDict = match.groupdict()
                fieldKey = int(fieldDict.pop('fieldID'))
                fieldValue = fieldDict
                if fieldKey not in value:
                    value[fieldKey] = fieldValue
                elif key[3] != 'enum' or self.__reAllowAlias.search(self.__messages[key]) == None:
                    raise Error524

            value['extendRange'] = None
            for match in self.__reExtendRange.finditer(self.__messages[key]):
                extendDict = match.groupdict()
                start = int(extendDict['extendStart'])
                end = int(extendDict['extendEnd'])
                if value['extendRange'] == None:
                    value['extendRange'] = (start,end)
                else:
                    raise Error525
                
            if key[3] == 'message' or key[3] == 'enum':
                if key[0] not in messages:
                    messages[key[0]] = value
                else:
                    raise Error526
            elif key[3] == 'extend':
                self.__expandMessages.append((key[0],value))
            else:
                self.__oneOfMessages.append(key[0])
                value['class'] = 'message'
                if key[0] not in messages:
                    messages[key[0]] = value
                else:
                    raise Error526

        self.__messages = messages

    def __parseExtendMessage(self):
        if self.__expandMessages != [] and self.__version != 'proto2':
            raise Error527
        for extendName,extendBody in self.__expandMessages:
            message = self.__messages[extendName]
            start, end = message['extendRange']
            for fieldKey in extendBody:
                if type(fieldKey) == int:
                    if fieldKey >= start and fieldKey <= end:
                        fieldValue = extendBody[fieldKey]
                        if fieldKey not in message:
                            message[fieldKey] = fieldValue
                        else:
                            raise Error524
                    else:
                        raise Error528

    def __checkMessage(self):
        if self.__version == 'proto3':
            for messageNmae in self.__messages:
                message = self.__messages[messageNmae]
                if message['class'] == 'enum':
                    self.__enumType.append(messageNmae)
                elif message['class'] == 'message':
                    self.__expandType.append(messageNmae)
                    for fieldKey in message:
                        if type(fieldKey) == int:
                            fieldValue = message[fieldKey]
                            if fieldValue['adjunct'] == 'repeated':
                                if fieldValue['optionName'] == None:
                                    fieldValue['optionName'] = 'packed'
                                    fieldValue['optionValue'] = 'true'
                                elif fieldValue['optionName'] == 'packed':
                                    if fieldValue['optionValue'] != 'true' and fieldValue['optionValue'] != 'false':
                                        raise Error514
                                else:
                                    raise Error515
                            elif fieldValue['adjunct'] == 'singular':
                                if fieldValue['optionName'] != None:
                                    raise Error515
                                else:
                                    fieldValue['optionName'] = 'default'
                            elif fieldValue['adjunct'] == None:
                                if fieldValue['optionName'] != None:
                                    raise Error515
                                else:
                                    fieldValue['optionName'] = 'default'
                            else:
                                raise Error516
        elif self.__version == 'proto2':
            for messageNmae in self.__messages:
                message = self.__messages[messageNmae]
                if message['class'] == 'enum':
                    self.__enumType.append(messageNmae)
                elif message['class'] == 'message':
                    self.__expandType.append(messageNmae)
                    for fieldKey in message:
                        if type(fieldKey) == int:
                            fieldValue = message[fieldKey]
                            if messageNmae in self.__oneOfMessages:
                                fieldValue['adjunct'] = 'optional'
                            if fieldValue['adjunct'] == 'repeated':
                                if fieldValue['optionName'] == None:
                                    fieldValue['optionName'] = 'packed'
                                    fieldValue['optionValue'] = 'false'
                                elif fieldValue['optionName'] == 'packed':
                                    if fieldValue['optionValue'] != 'true' and fieldValue['optionValue'] != 'false':
                                        raise Error514
                                else:
                                    raise Error515
                            elif fieldValue['adjunct'] == 'optional':
                                if fieldValue['optionName'] == None:
                                    fieldValue['optionName'] = 'default'
                                elif fieldValue['optionName'] != 'default':
                                    raise Error515
                            elif fieldValue['adjunct'] == 'required':
                                if fieldValue['optionName'] == None:
                                    fieldValue['optionName'] = 'default'
                                elif fieldValue['optionName'] != 'default':
                                    raise Error515
                            else:
                                raise Error516
        else:
            raise Error512

    # 解析proto
    def __parseProto(self):
        self.__getMessage()
        self.__parseMessage()
        self.__parseExtendMessage()
        self.__checkMessage()

    # 加载proto文件
    def loadProto(self, protoFilePath):
        try:
            with open(protoFilePath,'r',encoding='utf-8') as f:
                self.protoFile = f.read()
        except Exception as e:
            raise Error511
        self.__parseProto()
        return self
    
    # 加载PB文件
    def loadPB(self, PBFilePath):
        try:
            with open(PBFilePath,'rb') as f:
                self.PBFile = f.read()
        except Exception as e:
            raise Error517
        return self

    # 获取字节中的最高位
    def __getMostBit(self, Byte):
        return (Byte >> 7) & 0b1

    # 对pb数据进行解析,返回包含ID、数据的字典
    def __parsePBData(self,data=None):
        if data == None:
            data = self.PBFile
        isParsingKey = True
        index = 0
        end = data.__len__()
        while index < end:
            if isParsingKey:
                isParsingKey = False
                keyType = data[index] & 0b111
                shiftLeft = 4
                fieldID = (data[index] >> 3) & 0b1111
                while self.__getMostBit(data[index]) == 1:
                    index += 1
                    fieldID += (data[index] & 0b1111111) << shiftLeft
                    shiftLeft += 7
                index += 1
            else:
                isParsingKey = True
                shiftLeft = 0
                if keyType == 0:
                    fieldData = data[index] & 0b1111111
                    while self.__getMostBit(data[index]) == 1:
                        index += 1
                        shiftLeft += 7
                        fieldData += (data[index] & 0b1111111) << shiftLeft
                    index += 1
                elif keyType == 5:
                    fieldData = data[index:index+4]
                    index += 4
                elif keyType == 1:
                    fieldData = data[index:index+8]
                    index += 8
                elif keyType == 2:
                    fieldDataLenth = data[index] & 0b1111111
                    while self.__getMostBit(data[index]) == 1:
                        index += 1
                        shiftLeft += 7
                        fieldDataLenth += (data[index] & 0b1111111) << shiftLeft
                    index += 1
                    fieldData = data[index:index+fieldDataLenth]
                    index += fieldDataLenth
                else:
                    raise Error518
                yield (fieldID,fieldData)

    # 接收变量的所有属性和原始数据, 返回该变量的匹配结果, 可能是值、列表或字典
    def __parseOneData(self, fieldAttribute, fieldData):
        result = {}
        adjunct = fieldAttribute['adjunct']
        className = fieldAttribute['className']
        key = fieldAttribute['fieldName']
        optionName = fieldAttribute['optionName']
        optionValue = fieldAttribute['optionValue']
        try:
            if className in self.__primitiveType:
                if optionName == 'packed' and optionValue == 'false':
                    value = self.__typeParser[className](fieldData)
                    if adjunct == 'repeated':
                        if key in result:
                            result[key].append(value)
                        else:
                            result[key] = [value]
                    else:
                        result[key] = value
                else:
                    value = self.__typeParser[className](fieldData,adjunct)
                    result[key] = value
            elif className in self.__builtinType:
                value = self.__typeParser[className](fieldData)
                if adjunct == 'repeated':
                    if key in result:
                        result[key].append(value)
                    else:
                        result[key] = [value]
                else:
                    result[key] = value
            elif className in self.__enumType:
                if optionName == 'packed' and optionValue == 'false':
                    value = self.__typeParser['enum'](fieldData)
                    if adjunct == 'repeated':
                        if key in result:
                            result[key].append(value)
                        else:
                            result[key] = [value]
                    else:
                        result[key] = value
                else:
                    value = self.__typeParser['enum'](fieldData,adjunct)
                    result[key] = value
            elif className in self.__expandType:
                value = self.__parseData(className,fieldData)
                if adjunct == 'repeated':
                    if key in result:
                        result[key].append(value)
                    else:
                        result[key] = [value]
                else:
                    result[key] = value
            elif className == None:
                if fieldAttribute['map'] != None:
                    value = {}
                    result[key] = value
                    mapKeyType = fieldAttribute['mapKey']
                    mapValueType = fieldAttribute['mapValue']
                    isParsingKey = True
                    for mapData in self.__parsePBData(fieldData):
                        if isParsingKey:
                            isParsingKey = False
                            mapKeyAttribute = {'adjunct': None, 'className': fieldAttribute['mapKey'], 'map': None, 'mapKey': None, 'mapValue': None, 'fieldName': mapData['fieldID'], 'optionName': 'default', 'optionValue': None}
                            mapKeyData = mapData['fieldData']
                            mapKey = self.__parseOneData(mapKeyAttribute,mapKeyData)
                        else:
                            isParsingKey = True
                            mapValueAttribute = {'adjunct': None, 'className': fieldAttribute['mapValue'], 'map': None, 'mapKey': None, 'mapValue': None, 'fieldName': mapData['fieldID'], 'optionName': 'default', 'optionValue': None}
                            mapValueData = mapData['fieldData']
                            mapValue = self.__parseOneData(mapValueAttribute,mapValueData)
                            value[mapKey] = mapValue
            else:
                raise Error519
        except Error518 as e:
            raise e
        except Error519 as e:
            raise e
        return result[key]

    # 接收message和pb数据, 返回该message的匹配结果
    def __parseData(self,messageName,PB=None):
        result = {}
        isMatch = True
        messageBody = self.__messages[messageName]
        for fieldID,fieldData in self.__parsePBData(PB):
            if fieldID in messageBody:
                fieldAttribute = messageBody[fieldID]
                key = fieldAttribute['fieldName'] 
                try:
                    value = self.__parseOneData(fieldAttribute,fieldData)
                    if key not in result:
                        result[key] = value
                    else:
                        if type(value) == dict:
                            result[key].update(value)
                        elif type(value) == list:
                            result[key].extend(value)
                        else:
                            result[key] = value
                except Error518 as e:
                    raise e
                except Error519 as e:
                    raise e
                except Exception as e:
                    isMatch = False
            else:
                isMatch = False
                for oneOfMessgaeName in self.__oneOfMessages:
                    oneOfMessgaeBody = self.__messages[oneOfMessgaeName]
                    parent = oneOfMessgaeBody['parent']
                    if parent == messageName:
                        value = self.__parseData(oneOfMessgaeName,PB)
                        if value:
                            result.update(value)
                            isMatch = True
            if isMatch == False:
                break
        if isMatch:
            return result
        else:
            return {}

    def __fillDefaultValue(self):
        for key in list(self.result.keys()):
            value = self.result.pop(key)
            try:
                self.__fillOneDefaultValue({key:value})
                self.result[key] = value
            except Exception as e:
                pass

    def __fillOneDefaultValue(self,result=None):
        if result == None:
            result = self.result
        for resultName in result:
            resultValue = result[resultName]
            message = self.__messages[resultName]
            for fieldKey in message:
                if type(fieldKey) == int:
                    fieldValue = message[fieldKey]
                    fieldName = fieldValue['fieldName']
                    adjunct = fieldValue['adjunct']
                    className = fieldValue['className']
                    if fieldName not in resultValue:
                        if self.__version == 'proto3':
                            if adjunct == 'repeated':
                                resultValue[fieldName] = []
                            elif className == 'bool':
                                resultValue[fieldName] = False
                            elif className in self.__primitiveType:
                                resultValue[fieldName] = 0
                            elif className in self.__enumType:
                                resultValue[fieldName] = 0
                            elif className in self.__builtinType:
                                resultValue[fieldName] = ''
                            elif className in self.__expandType:
                                resultValue[fieldName] = None
                            else:
                                raise Error523
                        elif self.__version == 'proto2':
                            if adjunct == 'repeated':
                                resultValue[fieldName] = []
                            elif adjunct == 'optional':
                                defalutValue = fieldValue['optionValue']
                                if defalutValue == None:
                                    if className == 'bool':
                                        resultValue[fieldName] = False
                                    elif className in self.__primitiveType:
                                        resultValue[fieldName] = 0
                                    elif className in self.__enumType:
                                        for enumID in self.__messages[className]:
                                            if type(enumID) == int:
                                                resultValue[fieldName] = enumID
                                                break
                                    elif className in self.__builtinType:
                                        resultValue[fieldName] = ''
                                    elif className in self.__expandType:
                                        resultValue[fieldName] = None
                                    else:
                                        raise Error523
                                else:
                                    if className == 'bool':
                                        if defalutValue == 'true':
                                            resultValue[fieldName] = True
                                        elif defalutValue == 'false':
                                            resultValue[fieldName] = False
                                        else:
                                            raise Error521
                                    elif className in self.__primitiveType:
                                        try:
                                            resultValue[fieldName] = int(defalutValue)
                                        except Exception as e:
                                            raise Error521 
                                    elif className in self.__enumType:
                                        try:
                                            if type(defalutValue) == int:
                                                resultValue[fieldName] = int(defalutValue)
                                            else:
                                                enumMessage = self.__messages[className]
                                                for enumKey in enumMessage:
                                                    if type(enumKey) == int:
                                                        if defalutValue == enumMessage[enumKey]['fieldName']:
                                                            resultValue[fieldName] = enumKey
                                        except Exception as e:
                                            raise Error521 
                                    elif className in self.__builtinType:
                                        resultValue[fieldName] = defalutValue
                                    elif className in self.__expandType:
                                        raise Error522
                                    else:
                                        raise Error523
                            else:
                                raise Error523
                        else:
                            raise Error523
                    else:
                        if className in self.__expandType:
                            if adjunct == 'repeated':
                                for resultV in resultValue[fieldName]:
                                    self.__fillOneDefaultValue({className:resultV})
                            else:
                                self.__fillOneDefaultValue({className:resultValue[fieldName]})

    def __enumTypeTransform(self,resultBody,messageBody):
        for fieldKey in messageBody:
            if type(fieldKey) == int:
                fieldValue = messageBody[fieldKey]
                fieldName = fieldValue['fieldName']
                adjunct = fieldValue['adjunct']
                className = fieldValue['className']
                if className in self.__enumType:
                    enumBody = self.__messages[className]
                    if adjunct == 'repeated':
                        newEnum = []
                        for enum in resultBody[fieldName]:
                            newEnum.append(enumBody[enum]['fieldName'])
                        resultBody[fieldName].clear()
                        resultBody[fieldName].extend(newEnum)
                    else:
                        rawEnum = resultBody[fieldName]
                        if rawEnum in enumBody:
                            enumFieldName = enumBody[rawEnum]['fieldName']
                            resultBody[fieldName] = enumFieldName
                        else:
                            raise Error529
                elif className in self.__expandType:
                    if adjunct == 'repeated':
                        expandBody = self.__messages[className]
                        for rawExpand in resultBody[fieldName]:
                            if rawExpand:
                                self.__enumTypeTransform(rawExpand,expandBody)
                    else:
                        rawExpand = resultBody[fieldName]
                        expandBody = self.__messages[className]
                        if rawExpand:
                            self.__enumTypeTransform(rawExpand,expandBody)

    def __typeTransform(self):
        for resultName in self.result:
            resultBody = self.result[resultName]
            messageBody = self.__messages[resultName]
            self.__enumTypeTransform(resultBody,messageBody)

    def parser(self,messages=None,rawdata=None):
        for message in self.__messages:
            result = None
            try:
                if self.__messages[message]['class'] == 'message':
                    result = self.__parseData(message)
            except Exception as e:
                raise e
            else:
                if result:
                    self.result[message] = result
        self.__fillDefaultValue()
        self.__typeTransform()
        return self

    def dump(self):
        for key in list(self.result.keys()):
            value = self.result.pop(key)
            try:
                result = json.dumps({key:value})
                self.result.update(json.loads(result))
            except Exception as e:
                pass
        if self.result:
            return json.dumps(self.result)
        else:
            raise Error523

if __name__ == "__main__":
    try:
        argument = []
        argumentCount = len(sys.argv)
        if argumentCount < 3:
            raise Error510
        for i in range(1, argumentCount):
            argument.append((sys.argv[i]))
    
        demo = Pb2Json()
        demo.loadProto(argument[0])
        demo.loadPB(argument[1])
        demo.parser()
        
        result = demo.dump()
        print(200)
        print(result)
    except Error510 as e:
        print(510)
    except Error511 as e:
        print(511)
    except Error512 as e:
        print(512)
    except Error513 as e:
        print(513)
    except Error514 as e:
        print(514)
    except Error515 as e:
        print(515)
    except Error516 as e:
        print(516)
    except Error517 as e:
        print(517)
    except Error518 as e:
        print(518)
    except Error519 as e:
        print(519)
    except Error520 as e:
        print(520)
    except Error521 as e:
        print(521)
    except Error522 as e:
        print(522)
    except Error523 as e:
        print(523)
    except Error524 as e:
        print(524)
    except Error525 as e:
        print(525)
    except Error526 as e:
        print(526)
    except Error527 as e:
        print(527)
    except Error528 as e:
        print(528)
    except Error529 as e:
        print(529)
    except Exception as e:
        print(530)

