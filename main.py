import requests
import json


file_path = 'TEST2.txt'

with open(file_path) as f:
    mydata = f.read()

header = {'Authorization' : 'AgAAAAAUQONkAADLW01wR5v2DkWggMGRqeR0VHg'}

param = {'file': file_path}
def upload():
  disc = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload?path=/file_path', headers = header)
  href = (disc.json()['href'])
  response = requests.put(href, data= mydata, params = param)
  print(f'Ваш {file_path} успешно загружен')


upload()


      
