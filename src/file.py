# file path of csv files
csv_loc = {
    'ca': '../datasets/CAvideos.csv',
    'de': '../datasets/DEvideos.csv',
    'fr': '../datasets/FRvideos.csv',
    'gb': '../datasets/GBvideos.csv',
    'us': '../datasets/USvideos.csv'}

# file path of csv files
json_loc = {
    'us': '../datasets/US_category_id.json',
    'gb': '../datasets/GB_category_id.json',
    'fr': '../datasets/FR_category_id.json',
    'de': '../datasets/DE_category_id.json',
    'ca': '../datasets/CA_category_id.json'}


def all_csv():
    '''
    :rtype: dict_values
    Get file path of all csv files.
    '''
    return csv_loc.values()


def all_json():
    '''
    :rtype: dict_values
    Get file path of all json files.
    '''
    return json_loc.values()


def csv_str(area):
    '''
    :area: str
    :rtype: str
    Get file path of specific csv file `area`.
    '''
    assert area == 'ca' or area == 'de' or area == 'fr' or area == 'gb' or area == 'us'
    return csv_loc[area]


def json_str(area):
    '''
    :area: str
    :rtype: str
    Get file path of specific json file `area`.
    '''
    assert area == 'ca' or area == 'de' or area == 'fr' or area == 'gb' or area == 'us'
    return json_loc[area]
