import requests

def get_random_joke():
    url = "https://icanhazdadjoke.com"

    resp = requests.get(url, headers={"Accept": "application/json"})
    return resp.json()['joke']

if __name__ == '__main__':
    get_random_joke()
