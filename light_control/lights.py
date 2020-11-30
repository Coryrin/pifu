# from . import credentials
import requests

def get_base_url():
    # username = credentials.HUE_USERNAME
    # url = credentials.HUE_URL
    return ''

def get_lights():
    url = get_base_url()
    url = f'{url}/lights/1'

    resp = requests.get(url)


def toggle_lights(state):
    """
    Turn the lights on or off via the state param.
    """
    url = get_base_url()
    url = f'{url}/lights/1/state'

    data = {
        "on": state
    }

    resp = requests.put(url, json=data)

if __name__ == '__main__':
    toggle_lights(True)