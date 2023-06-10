import requests

def get_list_location() -> list:
    url = f'https://rickandmortyapi.com/api/location'
    data = requests.get(url).json()
    data = data['results']
    return data

def get_location_names() -> list:
    return [i['name'] for i in get_list_location()]

def get_location_data(name: str) -> dict:
    characters = {i['name']: i['id'] for i in get_list_location()}
    char_id = characters[name]
    url = f'https://rickandmortyapi.com/api/location/{char_id}'
    data = requests.get(url).json()
    return data

def get_location_text(name: str) -> str:
    try:
        data = get_location_data(name)
        text = f"""\
        \nCreated: {data['created']}
        \nDimension: {data['dimension']}
        \nId: {data['id']}
        \nName: {data['name']}
        \nType: {data['type']}
        """
        return text
    except Exception as error:
        return "it exists"
    
print(get_location_text('Earth (C-137)'))