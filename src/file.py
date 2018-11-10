# file path of csv files
_csv = {
    'ca': '../datasets/CAvideos.csv',
    'de': '../datasets/DEvideos.csv',
    'fr': '../datasets/FRvideos.csv',
    'gb': '../datasets/GBvideos.csv',
    'us': '../datasets/USvideos.csv'}

# file path of json files
_json = {
    'ca': '../datasets/CA_category_id.json',
    'de': '../datasets/DE_category_id.json',
    'fr': '../datasets/FR_category_id.json',
    'gb': '../datasets/GB_category_id.json',
    'us': '../datasets/US_category_id.json'}


# Location abbreviation
LOC_ABBR = ('ca', 'de', 'fr', 'gb', 'us')

def all_csv():
    '''
    :rtype: dict_values
    Get file path of all csv files.
    '''
    return _csv.values()


def all_json():
    '''
    :rtype: dict_values
    Get file path of all json files.
    '''
    return _json.values()


def csv_at(area):
    '''
    :area: str
    :rtype: str
    Get file path of specific csv file `area`.
    '''
    assert area in LOC_ABBR
    return _csv[area]


def json_at(area):
    '''
    :area: str
    :rtype: str
    Get file path of specific json file `area`.
    '''
    assert area in LOC_ABBR
    return _json[area]
