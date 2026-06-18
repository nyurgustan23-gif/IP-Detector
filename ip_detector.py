import requests
from pprint import pprint


class YandexDisk:
    def __init__(self, token):
        self.headers = {'Authorization': f'OAuth {token}'}


    def check_folder(self, folder):
            url = 'https://cloud-api.yandex.net/v1/disk/resources?path=' + folder
            try:
                resp = requests.get(url, headers=self.headers)
                return resp.status_code
            
            except requests.exceptions.ConnectionError:
                return print(f'Ошибка сети')

            
    def create_folder(self, folder):
        folder_code = YandexDisk.check_folder(self, folder)
        if folder_code == 404:
            try:
                url = 'https://cloud-api.yandex.net/v1/disk/resources?path=' + folder
                requests.put(url, headers=self.headers) 
            except requests.exceptions.ConnectionError:
                return print(f'Ошибка сети')

    def add_ip_info(self):
        ip = IPfy.get_ip()
        ip_info = IPinfo.ip_info
        YandexDisk.create_folder(self, ip)
        url = (
            f'https://cloud-api.yandex.net/v1/disk/resources/upload?path={ip}/{ip}_info.json&url={ip_info}'
        )
        try:
            resp = requests.post(url, headers=self.headers)
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


person = YandexDisk('') #Нужно вставить сюда ваш токен
person.add_ip_info()