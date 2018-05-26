import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def getRoomId(keyword,start):
    while True:
        print('~~~~~~~~~~~~~~~')
        for room_id in range( start + 1, start + 10 ):
            url = 'https://solitaire.sayweee.cn/index.php/solitaire/api/events/' + str(room_id)
            html = requests.get(url,verify=False)
            json_data = json.loads(html.text)
            if json_data['result'] == True:
                print(str(room_id) + "\t" + json_data['object']['rec_creator_alias'])
                if json_data['object']['rec_creator_alias'] == keyword:
                    return str(room_id)
            else:
                print('----------------')
        print('~~~~~~~~~~~~~~~')


