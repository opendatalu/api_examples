import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('api_key', help="API key to use", type=str)
parser.add_argument('dataset_id', type=str)
parser.add_argument('resource_id', type=str)
parser.add_argument('filename', help="file to upload")
args = parser.parse_args()

api_key = args.api_key
dataset_id = args.dataset_id
resource_id = args.resource_id
file_name = args.filename

files = {'file': (args.filename, open(args.filename, 'rb'), 'text/plain')}
headers = {'X-API-KEY': api_key}
url = 'https://data.public.lu/api/1/datasets/%s/resources/%s/upload/' % (dataset_id, resource_id)

r = requests.post(url, files=files, headers=headers)
print r.text
