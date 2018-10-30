#################################
### Read content of json file ###
#################################
import json
fname = {'us':'US_category_id.json', 'gb':'GB_category_id.json', \
    'fr':'FR_category_id.json', 'de':'DE_category_id.json', 'ca':'CA_category_id.json'}

def read_json(fname):
    '''
    :fname: str
    :return: dict
    '''
    id_category = {}
    for file in fname.values():
        # print(f"open file: {file}")
        with open('../datasets/'+file) as f:
            data = json.load(f)
            # print(f"length: {len(data['items'])}")
            for i in range(len(data['items'])):
                channel_id = data['items'][i]['id']
                channel_cat = data['items'][i]['snippet']['title']
                if channel_id not in id_category:
                    id_category.update({channel_id:channel_cat})
    return id_category

print(read_json(fname))
