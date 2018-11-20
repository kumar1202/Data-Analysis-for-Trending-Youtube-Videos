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
AREA = ('ca', 'de', 'fr', 'gb', 'us')
_AREA_FULL_NAME = {'ca': 'Canada', 'de': 'Germany',
                   'fr': 'France', 'gb': 'Great British', 'us': 'USA'}


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
    assert isinstance(area, str)
    assert area in AREA
    return _csv[area]


def json_at(area):
    '''
    :area: str
    :rtype: str
    Get file path of specific json file `area`.
    '''
    assert isinstance(area, str)
    assert area in AREA
    return _json[area]


def full_name(area):
    '''
    :area: str
    Get full name of the area `area`.
    '''
    assert isinstance(area, str)
    assert area in AREA
    return _AREA_FULL_NAME[area]
