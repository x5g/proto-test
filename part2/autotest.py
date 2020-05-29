from selenium import webdriver
import time
# import SendKeys
import os
import difflib

def compareTwoText(text1, text2):
    # text1 = 'aaabb b'
    # text2 = 'aaab bb'
    #
    text1_lines = text1.splitlines()
    text2_lines = text2.splitlines()

    d = difflib.Differ()
    diff = d.compare(text1_lines, text2_lines)

    # print("\n".join(list(diff)))
    return '\n'.join(list(diff))

def GetFileFromThisRootDir(dir,ext = None):
    allfiles = []
    needExtFilter = (ext != None)
    for root,dirs,files in os.walk(dir):
        for filespath in files:
            filepath = os.path.join(root, filespath)
            extension = os.path.splitext(filepath)[1][1:]
            if needExtFilter and extension in ext:
                allfiles.append(filepath)
            elif not needExtFilter:
                allfiles.append(filepath)
    return allfiles

if os.path.exists('/Users/chenzixuan/Desktop/proto/.DS_Store'):
    os.remove('/Users/chenzixuan/Desktop/proto/.DS_Store')

protolist = GetFileFromThisRootDir('/Users/chenzixuan/Desktop/proto', 'proto')

filename = []
for name in protolist:
    filename.append(name[len('/Users/chenzixuan/Desktop/proto') + 1:].split('.')[0])

pblist = []
for name in filename:
    pblist.append('/Users/chenzixuan/Desktop/proto/' + str(name) + '.pb')

jsonlist = []
for name in filename:
    jsonlist.append('/Users/chenzixuan/Desktop/proto/' + str(name) + '.json')

# print(pblist)
# print(len(pblist))
# print(len(pblist))
# print(len(protolist))
# print(protolist)
# exit()
#
# browser = webdriver.Chrome()
# browser.get('http://7ke.top/show/')
# browser.implicitly_wait(5)
# upload_proto = browser.find_element_by_xpath('/html/body/div/section/main/div[1]/div[1]/div[1]/div/input')
# upload_proto.send_keys('/Users/chenzixuan/Desktop/proto/book.proto')
# browser.implicitly_wait(5)
# upload_pb = browser.find_element_by_xpath('/html/body/div/section/main/div[1]/div[1]/div[2]/div/input')
# upload_pb.send_keys('/Users/chenzixuan/Desktop/proto/book.pb')
# browser.implicitly_wait(5)
#
# # button_java = browser.find_element_by_xpath('/html/body/div/section/main/div[2]/button[1]')
# # button_java.click()
# button_python = browser.find_element_by_xpath('/html/body/div/section/main/div[2]/button[2]')
# button_python.click()
# browser.implicitly_wait(5)
# time.sleep(5)
#
# zhankai = browser.find_elements_by_class_name('jv-ellipsis')
# # for i, _ in enumerate(zhankai):
# #     if i == 0:
# #         continue
# #     zhankai[i].click()
# while(len(zhankai)):
#     if len(zhankai) != 0:
#         zhankai[0].click()
#         # time.sleep(2)
#         zhankai.clear()
#         zhankai = list(set(browser.find_elements_by_class_name('jv-ellipsis')) - set(zhankai))
#     else:
#         break
#     # for i, _ in enumerate(zhankai):
#     #     if i == 0:
#     #         continue
#     #     zhankai[i].click()
#     #     time.sleep(2)
#     # zhankai.clear()
#     # zhankai = list(set(zhankai) - set(browser.find_elements_by_class_name('jv-toggle')))
#
#
# content = browser.find_element_by_xpath('/html/body/div/section/main/div[1]/div[3]/div/pre')
# textContext = content.get_attribute('textContent')
# # print(content.get_attribute('textContent'))
# print(textContext)

# browser.refresh()

def test1():
    browser = webdriver.Chrome()
    browser.get('http://7ke.top/show/')
    browser.implicitly_wait(5)

    for index, file in enumerate(protolist):
        upload = browser.find_element_by_xpath('/html/body/div/section/main/div[1]/div[1]/div[1]/div/input')
        upload.send_keys(file)
        browser.implicitly_wait(5)

        content = browser.find_element_by_xpath('/html/body/div/section/main/div[1]/div[2]/div/pre')

        # print(index, file)
        # print('------')
        # print('网页转换内容')
        # print('------')
        # textContext = content.get_attribute('textContent')
        # # print(content.get_attribute('textContent'))
        # print(textContext)
        # print('------')
        # print('原定义文件内容')
        # print('------')
        # with open(file) as f:
        #     # print(''.join(f.read().splitlines()))
        #     protoContext = ''.join(f.read().splitlines())
        #     print(protoContext)
        # # print('------')
        # # print(compareTwoText(text1=textContext, text2=protoContext))
        # print('======')
        with open(file) as f:
            # print(''.join(f.read().splitlines()))
            protoContext = ''.join(f.read().splitlines())
            # print(protoContext)

        with open('test1.txt', 'a') as f:
            f.writelines(str(index) + ' ' + str(file) + '\n')
            f.writelines('------' + '\n')
            f.writelines('网页转换内容' + '\n')
            f.writelines('------' + '\n')
            textContext = str(content.get_attribute('textContent')).replace('\n', '')
            # print(content.get_attribute('textContent'))
            f.writelines(textContext + '\n')
            f.writelines('------' + '\n')
            f.writelines('原定义文件内容' + '\n')
            f.writelines('------' + '\n')
            f.writelines(protoContext + '\n')
            f.writelines('------' + '\n')
            if textContext in protoContext:
                f.writelines('√' + '\n')
            else:
                f.writelines('×' + '\n')
                print(file)
            f.writelines('======' + '\n')

        browser.refresh()

# browser.quit()

def test2():
    browser = webdriver.Chrome()
    browser.get('http://7ke.top/show/')
    browser.implicitly_wait(5)
    time.sleep(5)

    for index, file in enumerate(protolist):
        # if index < 68:
        #     continue

        upload_proto = browser.find_element_by_xpath('/html/body/div/section/main/div[1]/div[1]/div[1]/div/input')
        upload_proto.send_keys(file)
        browser.implicitly_wait(5)
        upload_pb = browser.find_element_by_xpath('/html/body/div/section/main/div[1]/div[1]/div[2]/div/input')
        upload_pb.send_keys(pblist[index])
        browser.implicitly_wait(5)

        # button_java = browser.find_element_by_xpath('/html/body/div/section/main/div[2]/button[1]')
        # button_java.click()
        button_python = browser.find_element_by_xpath('/html/body/div/section/main/div[2]/button[2]')
        button_python.click()
        browser.implicitly_wait(5)
        time.sleep(2)

        zhankai = browser.find_elements_by_class_name('jv-ellipsis')
        while (len(zhankai)):
            if len(zhankai) != 0:
                zhankai[0].click()
                # time.sleep(2)
                zhankai.clear()
                zhankai = list(set(browser.find_elements_by_class_name('jv-ellipsis')) - set(zhankai))
            else:
                break

        content = browser.find_element_by_xpath('/html/body/div/section/main/div[1]/div[3]/div/pre')

        # print(index, file)
        # print('------')
        # print('网页转换内容')
        # print('------')
        # textContext = content.get_attribute('textContent')
        # # print(content.get_attribute('textContent'))
        # print(textContext)
        # print('------')
        # print('原json文件内容')
        # print('------')
        # with open(jsonlist[index]) as f:
        #     # print(''.join(f.read().splitlines()))
        #     jsonContext = ''.join(f.read().splitlines())
        #     print(jsonContext)
        # # print('------')
        # # print(compareTwoText(text1=textContext, text2=protoContext))
        # print('======')

        with open(jsonlist[index]) as f:
            # print(''.join(f.read().splitlines()))
            jsonContext = ''.join(f.read().splitlines())
            # print(jsonContext)

        with open('test2_python.txt', 'a') as f:
            f.writelines(str(index) + ' ' + str(file) + '\n')
            f.writelines('------' + '\n')
            f.writelines('网页转换内容' + '\n')
            f.writelines('------' + '\n')
            textContext = ''.join(str(content.get_attribute('textContent')).split())
            # print(content.get_attribute('textContent'))
            f.writelines(textContext + '\n')
            f.writelines('------' + '\n')
            f.writelines('原定义文件内容' + '\n')
            f.writelines('------' + '\n')
            # f.writelines(jsonContext + '\n')
            f.writelines(''.join(jsonContext.split()) + '\n')
            f.writelines('======' + '\n')

        browser.refresh()


def test3():
    browser = webdriver.Chrome()
    browser.get('http://7ke.top/show/')
    browser.implicitly_wait(1)
    time.sleep(1)

    for index, file in enumerate(protolist):
        if index < 4:
            continue

        for idx, pb in enumerate(pblist):
            upload_proto = browser.find_element_by_xpath('/html/body/div/section/main/div[1]/div[1]/div[1]/div/input')
            upload_pb = browser.find_element_by_xpath('/html/body/div/section/main/div[1]/div[1]/div[2]/div/input')
            if index == idx:
                continue

            upload_proto.send_keys(file)
            browser.implicitly_wait(5)
            upload_pb.send_keys(pblist[idx])
            browser.implicitly_wait(5)

            # button_java = browser.find_element_by_xpath('/html/body/div/section/main/div[2]/button[1]')
            # button_java.click()
            button_python = browser.find_element_by_xpath('/html/body/div/section/main/div[2]/button[2]')
            button_python.click()
            browser.implicitly_wait(5)
            # time.sleep(2)

            zhankai = browser.find_elements_by_class_name('jv-ellipsis')
            while (len(zhankai)):
                if len(zhankai) != 0:
                    zhankai[0].click()
                    # time.sleep(2)
                    zhankai.clear()
                    zhankai = list(set(browser.find_elements_by_class_name('jv-ellipsis')) - set(zhankai))
                else:
                    break

            content = browser.find_element_by_xpath('/html/body/div/section/main/div[1]/div[3]/div/pre')

            print(index, idx, file, pb)
            # if '未知错误' not in content.get_attribute('textContent'):
            if '{result:"wait for input"}' not in content.get_attribute('textContent') and 'error message' not in content.get_attribute('textContent') and '{}' not in content.get_attribute('textContent'):
                print('------')
                print('网页转换内容')
                print('------')
                textContext = content.get_attribute('textContent')
                print(textContext)
                print('------')
                print('原json文件内容')
                print('------')
                with open(jsonlist[idx]) as f:
                    # print(''.join(f.read().splitlines()))
                    jsonContext = ''.join(f.read().splitlines())
                    print(jsonContext)
                # print('------')
                print('======')

            with open(jsonlist[idx]) as f:
                # print(''.join(f.read().splitlines()))
                jsonContext = ''.join(f.read().splitlines())
                # print(jsonContext)

            with open('test3_python.txt', 'a') as f:
                f.writelines(str(index) + ' ' + str(idx) + ' ' + str(file) + ' ' + str(pb) + '\n')
                # if '未知错误' not in content.get_attribute('textContent'):
                if '{result:"wait for input"}' not in content.get_attribute('textContent') and 'error message' not in content.get_attribute('textContent') and '{}' not in content.get_attribute('textContent'):
                    f.writelines('------' + '\n')
                    f.writelines('网页转换内容' + '\n')
                    f.writelines('------' + '\n')
                    textContext = ''.join(str(content.get_attribute('textContent')).split())
                    # print(content.get_attribute('textContent'))
                    f.writelines(textContext + '\n')
                    f.writelines('------' + '\n')
                    f.writelines('原json文件内容' + '\n')
                    f.writelines('------' + '\n')
                    # f.writelines(jsonContext + '\n')
                    f.writelines(''.join(jsonContext.split()) + '\n')
                    f.writelines('======' + '\n')

            browser.refresh()
            browser.implicitly_wait(1)
            # time.sleep(2)

def test4():
    # import data2_pb2
    # PB_FILE_PATH_LIST = ['http.pb', 'test4.pb', 'HotMessage.pb', 'anthor.pb', 'test2.pb', 'demo3.pb',
    #                      'UDP.pb', 'cover_helloworld.pb', 'dog.pb', 'Message.pb', 'data.pb', 'example2.pb',
    #                      'msginfo.pb', 'GroundData.pb', 'person.pb', 'message2.pb', 'protodemo.pb', 'user.pb']

    import http_pb2
    PB_FILE_PATH_LIST = ['data2.pb', 'test6.pb', 'test4.pb', 'simple.pb', 'test2.pb', 'GpsLocation.pb', 'dog.pb', 'SensorData.pb', 'common2.pb']

    for PB_FILE_PATH in PB_FILE_PATH_LIST:
        print(PB_FILE_PATH)
        print('-------')
        # 读message
        # message = data2_pb2.Message()
        message = http_pb2.HttpRequest()

        f = open(PB_FILE_PATH, "rb")
        message.ParseFromString(f.read())
        f.close()
        from google.protobuf.json_format import MessageToJson  # 关键
        json = MessageToJson(message)
        print(json)
        print('-------')


if __name__ == '__main__':
    # import difflib
    # text1 = 'aaabb b'
    # text2 = 'aaab bb'
    # text1_lines = text1.splitlines()
    # text2_lines = text2.splitlines()
    # d = difflib.HtmlDiff()
    # fid = open('report.html', 'w')
    # fid.write(d.make_file(text1, text2))
    # fid.close()


    # test1()
    test2()
    # test3()
    # test4()
