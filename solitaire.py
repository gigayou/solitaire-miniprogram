import requests
import urllib.parse
import urllib3
import time
from multiprocessing import Pool

from info import *
from roomid import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

KEYWORD = ''
START_POSITION = 135936
event_id = getRoomId(KEYWORD, START_POSITION)

headers = {
    'Host': 'solitaire.sayweee.cn',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'br, gzip, deflate',
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_1 like Mac OS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C153 MicroMessenger/6.6.6 NetType/WIFI Language/zh_CN',
    'Referer': 'https://servicewechat.com/wx3fc2ed10a4b917b3/18/page-frame.html',
    'Content-Length': '198',
    'Accept-Langugage': 'zh-cn'
}


def getJsonData():
    data = {
        'event_id': event_id,
        'name': '',
        'comment': '+1',
        'form_id': 'e6d229969718afdbb7e05a657a3c41ec',
        'user_id': '',
        'time_zone': '8',
        'touser': 'o7SLq0NZIuSo9GyllYPxLRdRMX1o',
        'page': '/pages/share/share?event_id=' + event_id
    }

    for selfInfo in INFODICT:
        data['name'] = selfInfo
        data['user_id'] = INFODICT[selfInfo]
        yield data


def getPostDataList():
    dataList = []
    for item in getJsonData():
        tmp_dict = item.copy()
        dataList.append(tmp_dict)
    return dataList


def main(selfdata):
    url = 'https://solitaire.sayweee.cn/index.php/solitaire/api/events/' + event_id + '/signup_post'
    name = selfdata['name']
    print(name + "正在接龙")
    response = requests.post(url, data=urllib.parse.urlencode(selfdata), headers=headers, verify=False)
    if response.status_code == 200:
        print(name + "接龙成功")


if __name__ == '__main__':
    start = time.time()
    pool = Pool()
    dataList = getPostDataList()
    pool.map(main, dataList)
    end = time.time()
    print(end - start)
