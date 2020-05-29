# -*- coding: utf-8 -*-
import re
import urllib.request
from bs4 import BeautifulSoup
import requests
from lxml import etree
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# visit html when giving a url
def pagevisit(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    soup = BeautifulSoup(html)
    return soup


import requests
import re

class Github(object):

    def __init__(self, username, password):
        self.headers = {
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
            'Host': 'github.com'
        } #　带上请求头伪装
        self.session = requests.Session()  # 创建一个session对象
        self.username = username
        self.password = password


    def get_login_sources(self):
        login_url = "https://github.com/login"
        responses = self.session.get(url=login_url,headers=self.headers)
        return responses


    def get_form_data(self, responses):
        form_data = {}
        # print(responses.content.decode())
        form_data["commit"] = "Sign in"
        form_data["utf8"] = "✓"
        form_data["authenticity_token"] = re.findall('name="authenticity_token" value="(.*?)"', responses.content.decode())[0]  # 得到是一个列表， 故使用下标
        form_data["ga_id"] = "1192443032.1565138303"
        form_data["login"] = self.username
        form_data["password"] = self.password
        form_data["webauthn-support"] = "supported"
        form_data["webauthn-iuvpaa-support"] = "unsupported"
        print(re.findall('name="(.*?)" id="required_field_', responses.content.decode()))
        required_field_name =  re.findall('name="(.*?)" id="required_field_', responses.content.decode())[0]
        print(required_field_name)
        form_data[required_field_name] = ""
        form_data["timestamp"] = re.findall('name="timestamp" value="(.*?)"', responses.content.decode())[0]
        form_data['timestamp_secret'] = re.findall('name="timestamp_secret" value="(.*?)"', responses.content.decode())[0]
        return form_data


    def post_form_data(self, form_data):
        post_url = "https://github.com/session"
        responses_2 = self.session.post(url=post_url, data=form_data, headers=self.headers)
        return responses_2


    def are_you_logged_in(self):
        logged_url = "https://github.com/" + self.username
        response_3 = self.session.get(logged_url)

        # 保存用户页面
        with open("GitHubasd.html", "wb")as f:
            f.write(response_3.content)

        # 验证登陆
        title = re.findall('<title>(.*?)</title>', response_3.content.decode())[0]
        print(title)
        if title == self.username:
            print("登陆成功")
        else:
            print('登陆失败')


    def run(self):
        # 1.提前访问登录页
        responses = self.get_login_sources()

        # 2.提取并构建表单数据
        form_data = self.get_form_data(responses)

        # 3.提交表单
        responses_2 = self.post_form_data(form_data)

        # 4.验证登陆
        self.are_you_logged_in()

if __name__ == '__main__':
    username = input("请输入用户名：")
    password = input("请输入密码：")
    user = Github(username, password)
    user.run()



# if __name__ == "__main__":
#     login = Login()
#     login.login(email='1098766468@qq.com', password='Czx970711')  # 此处填自己的
#     url = "https://github.com/search?l=Protocol+Buffer&p=3&q=proto&type=Code"
#     soup = pagevisit(url)
#     print(soup)