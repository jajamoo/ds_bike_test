import os
from urllib.request import urlretrieve
import pandas as pd

FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'


def get_data(file = 'fremont.csv', url = FREMONT_URL, force_dl = False):
    if force_dl or not os.path.exists(file):
        urlretrieve(url, file)
    data = pd.read_csv('fremont.csv', index_col = 'Date')

    try:
        data.index = pd.to_datetime(data.index, format = '%m/%d/%Y %H:%M:%S %p')
    except TypeError:
        data.index = pd.to_datetime(data.index)

    data.columns = ['West', 'East']
    data['Total'] = data['West'] + data['East']
    return data
