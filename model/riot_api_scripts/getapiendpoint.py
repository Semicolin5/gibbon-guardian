import pandas as pandas
import requests

# from typing_extensions import TypedDict


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


def summoner_champion_match_history(summoner_name: str, champion_id: int) -> str:
    account_id = summoner_name_to_account_id(summoner_name)
    query = f'{EUROPEAN_SERVER}/lol/match/v4/matchlists/by-account/{account_id}?champion={champion_id}&api_key={API_KEY}'
    response = requests.get(query)
    data = response.json()
    return data  

# TODO : sort out pythons shitty type hintings (why is it so bad?)
def winrate_across_matches(matches) -> str:
    for match in matches:
        match_id = match['gameId']
        query = f'{EUROPEAN_SERVER} /lol/match/v4/matches/{match_id}?api_key={API_KEY}'
        response = requests.get(query)
        data = response.json()

    return "50%"




zac = 112
vi = 109
warwick = 17


# This is the big method that we will call
def summoner_champion_stats(summoner_name: str, champion_id: str) -> str:
    
    match_history = summoner_champion_match_history(summoner_name, champion_id)

    # For now our duff stats
    stats = {
        'summoner_name': summoner_name,
        'champion': champion_id,
        'mastery': "He's pretty alright at it",
        'games': "100",
        'winrate': "51.2%"
    }

    return stats


statistics = summoner_champion_match_history('LeftTeh', 20)
print(statistics)


print("--------")
print(statistics['totalGames'])
print(len(statistics['matches']))

