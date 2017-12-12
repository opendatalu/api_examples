import requests
import argparse
import json
import shutil

parser = argparse.ArgumentParser()
parser.add_argument(
    '-a',
    '--api-key',
    dest='api_key',
    required=False,
    help="API key to use",
    type=str
)
parser.add_argument('dataset_id', type=str)
args = parser.parse_args()

api_key = args.api_key
dataset_id = args.dataset_id

headers = {}
headers['X-API-KEY'] = api_key
url = 'https://data.public.lu/api/1/datasets/%s/' % (dataset_id)
r = requests.get(url, headers=headers)
data = json.loads(r.text)


def download_file(url):
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        shutil.copyfileobj(r.raw, f)
    return local_filename

for resource in data['resources']:
    print download_file(resource['url']) 
