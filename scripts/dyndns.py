from dotenv import load_dotenv
from os import path, getenv
import requests

ENV_PATH = path.dirname(path.abspath(__file__)) + '/../.env'
load_dotenv(ENV_PATH, override=True)

OVH_USERNAME = getenv('OVH_USERNAME')
OVH_PASSWORD = getenv('OVH_PASSWORD')
OVH_DDDOMAIN = getenv('OVH_DDDOMAIN')

requests.get('https://www.ovh.com/nic/update?system=dyndns&hostname=' + OVH_DDDOMAIN, auth=(OVH_USERNAME, OVH_PASSWORD))
