import os
import re
import requests
import environ

env = environ.Env()
environ.Env.read_env()

def list_of_videos():
    TOKEN = env('VIMEO_TOKEN')
    user_id = "alvicolor"
    access_token = TOKEN
    url = f"https://api.vimeo.com/users/{user_id}/videos"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    videos = response.json()["data"]
    lst= []
    for video in videos:
        video['embed']['html'] = re.sub('(?<=width=\")\d+(?=\"\s)', '480', video['embed']['html'])
        video['embed']['html'] = re.sub('(?<=height=\")\d+(?=\"\s)', '360', video['embed']['html'])
        lst.append(video['embed']['html'])
    return lst