import string
import random
from configparser import ConfigParser

import requests


config_object = ConfigParser()
config_object.read('config.ini')

userinfo = config_object['USERINFO']
serverinfo = config_object['SERVERCONFIG']

users = [
    {
        'username': 'adlet1',
        'password': 'adlet1234',
        'email': 'adlet1@gmail.com',
    },
    {
        'username': 'adlet2',
        'password': 'adlet1234',
        'email': 'adlet2@gmail.com',
    },
    {
        'username': 'adlet3',
        'password': 'adlet1234',
        'email': 'adlet3@gmail.com',
    }
]

SIGNUP_URL = f'http://{serverinfo["host"]}:{serverinfo["port"]}/users/signup/'
for i in range(int(userinfo['number_of_users'])):
    requests.post(url=SIGNUP_URL, data=users[i])


LOGIN_URL = f'http://{serverinfo["host"]}:{serverinfo["port"]}/users/login/'
for i in range(int(userinfo['number_of_users'])):
    created_posts_ids = []
    resp = requests.post(url=LOGIN_URL, data={
        'username': users[i]['username'],
        'password': users[i]['password'],
    })

    access_token = resp.json()['access']
    POST_CREATE_URL = f'http://{serverinfo["host"]}:{serverinfo["port"]}/api/posts/'
    for i in range(int(userinfo['max_posts_per_user'])):
        payload = {
            'title': ''.join(random.choice(string.ascii_lowercase) for _ in range(10)),
            'text': ''.join(random.choice(string.ascii_lowercase) for _ in range(10)),
        }

        resp = requests.post(url=POST_CREATE_URL, data=payload, headers={
            'Authorization': f'Bearer {access_token}',
        })

        created_posts_ids.append(resp.json()['id'])

    post_id = random.choice(created_posts_ids)
    POST_LIKE_URL = f'http://{serverinfo["host"]}:{serverinfo["port"]}/api/posts/{post_id}/like/'
    for _ in range(int(userinfo['max_likes_per_user'])):
        requests.patch(url=POST_LIKE_URL, headers={
            'Authorization': f'Bearer {access_token}',
        })
