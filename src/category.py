import json
from file import *

# load file paths
_fname = all_json()
_category_dict = {}
for file in _fname:
    with open(file) as f:
        data = json.load(f)
        for i in range(len(data['items'])):
            channel_id = data['items'][i]['id']
            channel_cat = data['items'][i]['snippet']['title']
            if channel_id not in _category_dict:
                _category_dict.update({channel_id: channel_cat})

def category_dict():
    '''
    :rtype: dict
    Get a dictionary of id corresponding to its name.
    '''
    return _category_dict

def category_name(id):
    '''
    :id: int
    ;rtype: str
    Get category name with given number `id`.
    '''
    assert isinstance(id, int)
    return _category_dict[str(id)]

