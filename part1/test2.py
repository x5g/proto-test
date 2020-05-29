import requests
from lxml import etree
import re
import urllib.request
from bs4 import BeautifulSoup
import requests
from lxml import etree
import os
import warnings
warnings.filterwarnings("ignore")
import time
import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# visit html when giving a url
def pagevisit(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    soup = BeautifulSoup(html)
    return soup

class Login(object):
    def __init__(self):
        self.headers = {
            'Refer': 'https://github.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/68.0.3440.75 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()   # 此函数可以帮助我们维持一个会话，而且可以自动处理cookies，我们不用再去担心cookies的问题


    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)  # 访问GitHub的登录页面
        selector = etree.HTML(response.text)
        # token = selector.xpath('//div//input[2]/@value')[0]   # 解析出登陆所需的authenticity_token信息
        import re
        token = re.findall('name="authenticity_token" value="(.*?)"', response.content.decode())[0]
        return token

    def login(self, username, email, password):
        post_data = {
            'commit': 'Sign in',
            'utf-8': '✓',
            'authenticity_token': self.token(),
            'login': email,
            'password': password
        }
        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        if response.status_code == 200:
            self.dynamics(response.text)

        response = self.session.get(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)

        self.username = username
        self.password = password

    def dynamics(self, html):  # 使用此方法提取所有动态信息
        selector = etree.HTML(html)
        dynamics = selector.xpath('//div[contains(@class, "news")]//div[contains(@class, "alert")]')
        for item in dynamics:
            dynamics = ' '.join(item.xpath('.//div[@class="title"]//text()')).strip()
            print(dynamics)

    def profile(self, html):  # 使用此方法提取个人的昵称和绑定的邮箱
        selector = etree.HTML(html)
        name = selector.xpath('//input[@id="user_profile_name"]/@value')[0]
        email = selector.xpath('//select[@id="user_profile_email"]/option[@value!=""]/text()')
        # print(name, email)

    def crawler(self, url):
        # logged_url = "https://github.com/" + self.username
        # logged_url = 'https://github.com/search?l=Protocol+Buffer&p=3&q=proto&type=Code'
        # response_3 = self.session.get(logged_url)
        response_3 = self.session.get(url)
        # print(response_3.content)

        # 保存用户页面
        # with open("GitHubasd.html", "wb")as f:
        #     f.write(response_3.content)

        # 验证登陆
        import re
        protoes = re.findall('https://github.*/blob/.*\.proto&quot', response_3.content.decode())
        # print(len(protoes))
        for i in range(len(protoes)):
            protoes[i] = protoes[i].replace('blob', 'raw').replace('&quot', '')
            # print(protoes[i])
            self.download(protoes[i])
        # print(protoes)


    def download(self, url):
        name2 = url[url.rfind('/') + 1:]
        name = url[url.rfind('/') + 1:url.rfind('.proto')] + '_' + str(int(round(time.time()*1000))) + '.proto'
        content = requests.get(url, verify=False).content
        with open('./proto/{}'.format(name), 'wb') as f:
            f.write(content)
        print(name + ' download success!')
        data = pd.DataFrame({'url': url, 'proto': name, 'proto2': name2}, index=[0])
        data.to_csv('proto.csv', header=False, index = False, mode = 'a+', encoding = 'utf-8-sig')
        # dataframe.to_csv("MultiNetV4_result.csv", index=False, sep=',')
        with open('./proto2/{}'.format(name2), 'wb') as f:
            f.write(content)
        print(name2 + ' download success!')
        data = pd.DataFrame({'url': url, 'proto': name2}, index=[0])
        data.to_csv('proto2.csv', header=False, index = False, mode = 'a+', encoding = 'utf-8-sig')

if __name__ == "__main__":
    login = Login()
    login.login(username='***', email='***', password='***')  # 此处填自己的
    for i in range(1, 101):
        print(i)
        url = 'https://github.com/search?l=Protocol+Buffer&p=' + str(i) + '&q=oneof&type=Code'
        try:
            login.crawler(url)
        except:
            login.crawler(url)
    # url = "https://github.com/search?l=Protocol+Buffer&p=3&q=proto&type=Code"
    # soup = pagevisit(url)
    # print(soup)