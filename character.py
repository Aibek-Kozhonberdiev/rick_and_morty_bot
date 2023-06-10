import requests
from pprint import pprint

def get_list_characters() -> list:
    url = f'https://rickandmortyapi.com/api/character/'
    data = requests.get(url).json()
    data = data['results']
    return data

def get_character_names() -> list:
    return [i['name'] for i in get_list_characters()]

def get_character_data(name: str) -> dict:
    characters = {i['name']: i['id'] for i in get_list_characters()}
    char_id = characters[name]
    url = f'https://rickandmortyapi.com/api/character/{char_id}'
    data = requests.get(url).json()
    return data

def get_character_text(name: str) -> str:
    try:
        data = get_character_data(name)
        text = f"""\
        \nImage: {data['image']}
        \nId: {data['id']}
        \nName: {data['name']}
        \nStatus: {data['status']}
        \nType: {data['type']}
        \nGender: {data['gender']}
        \nLocation name: {data['location']['name']}
        \nLocation: {data['location']['name']}
        """
        return text
    except Exception as error:
        return "it exists"
    
# print(get_character_text('Rick Sanchez'))