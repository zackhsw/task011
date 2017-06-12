import hashlib
import socket
import requests
from bs4 import BeautifulSoup


def get_ip():
    '''获取本机局域网的IP地址'''
    result = []
    # 获取本机电脑名
    user_name = socket.getfqdn(socket.gethostname())
    result.append(user_name)
    # 获取本机ip 这是内网的ip !!!
    user_ip = socket.gethostbyname(user_name)
    # result[1] = user_ip
    result.append(user_ip)
    return result


#
# for item in get_ip():
#     print(item)



def get_outside_ip():
    '''获取本机连接外网的ip地址'''
    url = r'http://www.whereismyip.com/'
    r = requests.get(url)
    bTag = BeautifulSoup(r.txt, 'html.parser', from_encoding='utf-8').find('b')
    ip = ''.join(bTag.stripped_strings)
    print('ip:' + ip)


def get_data_identification(args):
    '''对本机ip, 进行sha256哈希算法加密，获取摘要，来做数据标识'''
    # id_items = args
    id_str = "".join(args)
    d = hashlib.sha256()
    d.update(id_str.encode())
    print(d.hexdigest())
    # for item in args:
    #     d.update(item.encode())
    #     print(d.hexdigest())


def get_out_ip():
    url = r'http://1212.ip138.com/ic.asp'
    r = requests.get(url)
    print(r)
    txt = r.text
    ip = txt[txt.find("[") + 1: txt.find("]")]
    print('ip:' + ip )
    print(type(ip))
    return ip


if __name__ == '__main__':
    # get_outside_ip()
    get_out_ip()


    # 调用本地计算机的用户名与ip 并实现hash算法标识
    # id_event = get_ip()
    # print(id_event)
    # get_data_identification(id_event)
