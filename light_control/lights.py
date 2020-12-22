from inspect import getsourcefile
import os.path
import sys

current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir)

from functions import env
import requests

def get_base_url():
    username = env("HUE_USERNAME")
    url = env("HUE_URL")
    return f'{url}/api/{username}'

def get_lights():
    url = get_base_url()
    url = f'{url}/lights/1'

    resp = requests.get(url)

def toggle_lights(state):
    """
    Turn the lights on or off via the state param.

    TODO: the lights/1/state is a little hacky. Create a function which will allow users to cycle between lights in multiple rooms & see the name of them? e.g. Bedroom, Living Room, etc.
    """
    url = get_base_url()
    url = f'{url}/lights/1/state'

    data = {
        "on": state
    }

    return requests.put(url, json=data)

if __name__ == '__main__':
    toggle_lights(False)