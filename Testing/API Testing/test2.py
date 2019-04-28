import pandas as pd
import requests
import json
# Testing genius api


#df = pd.read_csv('https://query.data.world/s/vcrpi6mujkey5pvil4337o7mm2b6r5')


client_access_token = 'TRqR0flwc15QLwJmC4fWGysc1ubcPxUGLa6BLhR00ZLPVLUby6HCD8QGDaU1PlcJ'
base_url = 'https://api.genius.com'

user_input = input('artist and song: ').replace(" ", "-")

path = 'search/'
request_uri = '/'.join([base_url, path])
print(request_uri + user_input)

params = {'q': user_input}

token = 'Bearer {}'.format(client_access_token)
headers = {'Authorization': token}

writefile = open('genius_info.json', 'w')
r = requests.get(request_uri, params=params, headers=headers)
writefile.write(r.text)
writefile.close()

data = json.loads(r.text)

print(data['response']['hits'][0])
