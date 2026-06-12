import requests
from pprint import pprint

token = input('Вставьте сюда ваш скопированный токен: ')

def get_ip():
    url = 'https://api.ipify.org/?format=json'
    resp = requests.get(url)
    ip = resp.json()['ip']
    return ip

def create_folder(folder_name, token):
    url = 'https://cloud-api.yandex.net/v1/disk/resources?path='+folder_name
    headers = {'Authorization': f'OAuth {token}'}
    requests.put(url, headers=headers)

def add_ip_info(token):
    ip = get_ip()
    ip_info = 'https://ipinfo.io/'+ip+'/geo'
    create_folder(ip, token)
    url = (
        f'https://cloud-api.yandex.net/v1/disk/resources/upload?'
        f'path={ip}/{ip}_info.json&url={ip_info}'
    )
    headers = {'Authorization': f'OAuth {token}'}
    resp = requests.post(url, headers=headers)
    if resp.status_code == 202:
        print('Информация об IP успешно добавлена!')
    else:
        print('Не удалось добавить ip_info')
        print(resp.status_code)
        pprint(resp.json())

add_ip_info(token)


