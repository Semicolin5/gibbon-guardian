import pandas as pandas
import requests



EUROPEAN_SERVER = 'https://EUW1.api.riotgames.com'
API_KEY=''

# Types of requests

# Get account ID using summoner name
def summoner_name_to_account_id(summoner_name: str) -> str:
    query = f'{EUROPEAN_SERVER}/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={API_KEY}'
    response = requests.get(query)
    data = response.json()
    return data['accountId']


def summoner_name_to_summoner_id(summoner_name: str) -> str:
    query = f'{EUROPEAN_SERVER}/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={API_KEY}'
    response = requests.get(query)
    data = response.json()
    return data['id']


def summoner_champion_winrate(summoner_name: str, champion_id: int) -> str:
    account_id = summoner_name_to_account_id(summoner_name)
    query = f'https://EUW1.api.riotgames.com/lol/match/v4/matchlists/by-account/{account_id}?champion={champion_id}&api_key={API_KEY}'
    response = requests.get(query)
    data = response.json()
    return data  

zac = 112
vi = 109
warwick = 17

# LeftTeh_account_id = summoner_name_to_account_id('LeftTeh')
# LeftTeh_summoner_id = summoner_name_to_summoner_id('LeftTeh')


freeChampQueryLOL = '/lol/platform/v3/champion-rotations'
# url = f'https://EUW1.api.riotgames.com/lol/summoner/v4/summoners/by-name/LeftTeh?api_key={API_KEY}'
# url2 = f'https://EUW1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{encryptedSummonerId}?api_key={API_KEY}'
# url3 = f'https://EUW1.api.riotgames.com/lol/league/v4/entries/by-summoner/{encryptedSummonerId}?api_key={API_KEY}'


print(summoner_champion_winrate('LeftTeh', 20))
