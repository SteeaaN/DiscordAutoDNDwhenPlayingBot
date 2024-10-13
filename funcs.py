import requests
from const import online_status, dnd_status


class Info:
    def __init__(self):
        self.dnd: bool = True
        self.onl: bool = True


def write(name, content):
    with open(f'{name}', 'w', encoding='utf-8') as file:
        file.write(content)


def read(name):
    with open(f'{name}', 'r', encoding='utf-8') as file:
        return file.read()


def change_status(auth, new):
    if new == 1:  # online
        st = online_status
    else:  # dnd
        st = dnd_status
    headers = {
        'authorization': auth
        }
    json_data = {
        'settings': st
    }
    requests.patch('https://discord.com/api/v9/users/@me/settings-proto/1', headers=headers, json=json_data)

