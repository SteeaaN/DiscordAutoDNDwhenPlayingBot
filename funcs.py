import requests


class Info:
    def __init__(self):
        self.dnd: bool = True
        self.onl: bool = True


def write(name, content):
    with open(f'{name}', 'w', encoding='utf-8') as file:
        file.write(content)


def read(name) -> str:
    with open(f'{name}', 'r', encoding='utf-8') as file:
        return file.read()


def change_status(new) -> bool:
    auth = read('auth_token.txt')
    if new == 1:  # online
        st = read('online_status.txt')
    else:  # dnd
        st = read('dnd_status.txt')
    headers = {
        'authorization': auth
        }
    json_data = {
        'settings': st
    }
    req = requests.patch('https://discord.com/api/v9/users/@me/settings-proto/1', headers=headers, json=json_data)
    if req.status_code != 200:
        return False
    return True

