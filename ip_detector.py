import requests
from pprint import pprint


class YandexDisk:
    token = '' 
    data = {'Authorization': f'OAuth {token}'}

    def check_folder(folder):
            url = 'https://cloud-api.yandex.net/v1/disk/resources?path=' + folder
            try:
                resp = requests.get(url, headers=YandexDisk.data)
                return resp.status_code
            
            except requests.exceptions.ConnectionError:
                return print(f'Ошибка сети')
            
    def create_folder(folder):
        folder_code = YandexDisk.check_folder(folder)
        if folder_code == 404:
            try:
                url = 'https://cloud-api.yandex.net/v1/disk/resources?path=' + folder
                requests.put(url, headers=YandexDisk.data) 

            except requests.exceptions.ConnectionError:
                return print(f'Ошибка сети')

    def add_ip_info():
        ip = IPfy.get_ip()
        ip_info = IPinfo.ip_info
        YandexDisk.create_folder(ip)
        url = (
            f'https://cloud-api.yandex.net/v1/disk/resources/upload?path={ip}/{ip}_info.json&url={ip_info}'
        )
        try:
            resp = requests.post(url, headers=YandexDisk.data)
            if resp.status_code == 202:
                print('Информация об IP успешно добавлена!')
            else:
                print('Не удалось добавить ip_info')
                print(resp.status_code)
                pprint(resp.json())
        except requests.exceptions.ConnectionError:
            return print(f'Ошибка сети')
        

class IPfy:
    def get_ip():
        url = 'https://api.ipify.org/?format=json'
        resp = requests.get(url)
        ip = resp.json()['ip']
        return ip


class IPinfo:
    ip = IPfy.get_ip()
    ip_info = 'https://ipinfo.io/' + ip + '/geo'

YandexDisk.add_ip_info()