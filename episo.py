import requests

def get_list_episode() -> list:
    url = f'https://rickandmortyapi.com/api/episode'
    data = requests.get(url).json()
    data = data['results']
    return data

def get_episode_names() -> list:
    return [i['name'] for i in get_list_episode()]

def get_episode_data(name: str) -> dict:
    characters = {i['name']: i['id'] for i in get_list_episode()}
    char_id = characters[name]
    url = f'https://rickandmortyapi.com/api/episode/{char_id}'
    data = requests.get(url).json()
    return data

def get_episode_text(name: str) -> str:
    try:
        data = get_episode_data(name)
        text = f"""\
        \nId: {data['id']}
        \nName: {data['name']}
        \nAir date: {data['air_date']}
        \nEpisode: {data['episode']}
        \nCreated: {data['created']}
        """
        return text
    except Exception as error:
        return "it exists"
    
# print(get_episode_text("Pilot"))