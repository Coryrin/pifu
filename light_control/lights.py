from inspect import getsourcefile
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)

from functions import env
import requests
import json

rooms = {}

def get_base_url():
    username = env("HUE_USERNAME")
    url = env("HUE_URL")
    return f'{url}/api/{username}'

def adjust_brightness(dim, room):
    url = get_base_url()
    url += f'/lights/{room}'
    data = requests.get(url).json()
    if dim:
        new_brightness = data['state']['bri'] / 2
    else:
        new_brightness = data['state']['bri'] * 2

    data_to_send = {
        "bri": int(new_brightness) 
    }
    return requests.put(url + '/state', json=data_to_send)

def toggle_lights(state, room):
    """
    Turn the lights on or off via the state param.

    TODO: the lights/1/state is a little hacky. Create a function which will allow users to cycle between lights in multiple rooms & see the name of them? e.g. Bedroom, Living Room, etc.
    """
    url = get_base_url()
    url = f'{url}/lights/{room}/state'

    data = {
        "on": state
    }

    return requests.put(url, json=data)

def get_rooms():
    url = get_base_url()
    url = f'{url}/groups'

    data = requests.get(url)
    results = data.json()

    rooms = {}

    for i in results:
        rooms[i] = results[i]['name']

    return rooms

if __name__ == '__main__':
    adjust_brightness(True, 1)