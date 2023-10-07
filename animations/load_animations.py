import json
import requests


def load_lottiefile(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()