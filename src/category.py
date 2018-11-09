import json
from file import *

# load file paths
fname = all_json()
category_dict = {}
for file in fname:
    with open(file) as f:
        data = json.load(f)
        for i in range(len(data['items'])):
            channel_id = data['items'][i]['id']
            channel_cat = data['items'][i]['snippet']['title']
            if channel_id not in category_dict:
                category_dict.update({channel_id: channel_cat})


def cat_name(id):
    '''
    :id: int
    ;rtype: str
    Get category name with given number `id`.
    '''
    assert isinstance(id, int)
    return category_dict[str(id)]

# print(cat_name(23)) # Comedy
