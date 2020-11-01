import pandas as pandas
import requests

API_KEY='RGAPI-77d1fe4a-f9ad-4df0-bd61-22844dbeee39'


url = 'https://EUW1.api.riotgames.com/lol/summoner/v4/summoners/by-name/LeftTeh?api_key=RGAPI-77d1fe4a-f9ad-4df0-bd61-22844dbeee39'
url2 = 'https://EUW1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/l7Pmpyu4eeiY3qp26NXtgwf-8zefZtIpD7CAiRpCrenMQxA?api_key=RGAPI-77d1fe4a-f9ad-4df0-bd61-22844dbeee39'


response = requests.get(url)

#print(response.text)

data = response.json()

print(data)

print("---")
boogla = requests.get(url2)
data2 = boogla.json()

print(data2)

