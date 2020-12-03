from functions import env

def get_base_url():
    username = env("HUE_USERNAME")
    url = env("HUE_URL")
    return f'{url}/{username}'

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

    resp = requests.put(url, json=data)

if __name__ == '__main__':
    toggle_lights(True)