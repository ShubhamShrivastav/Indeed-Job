import os
import pandas as pd
from geopy.geocoders import Nominatim


def clean_data(share, save_to):
    data =pd.read_json(share)
    data['coordinates'] = data.apply(lambda row: create_column_coordinates(row), axis=1)
    data.to_html(os.path.join(save_to,'mapdata.html'))
    data.to_csv(os.path.join(save_to,'mapdata.csv'))
    data.to_json(os.path.join(save_to,'mapdata.json'))

def create_column_coordinates(row):
    if row['coordinates'] == None:
        if row['location']!='United states' or row['location']!='Home':
            try:
                location = Nominatim().geocode(row['city']+' '+row['state'])
                return (location.latitude,location.longitude)
            except Exception as e:
                print(str(e))

        else:
            return(0.0,0.0)
    else:
        return row['coordinates']

def function_awesome():
    path_to_file=r'C:\Users\shubham\Desktop\New folder\Spring 16\Data cleansing\Webscrapping\mapfile\mapdata.json'
    data_frame = pd.read_json(path_to_file)
    print(data_frame.isnull())


if '__main__'==__name__:
    clean_data(r'C:\Users\shubham\Desktop\New folder\Spring 16\Data cleansing\Webscrapping\clean\added_col.json',r'C:\Users\shubham\Desktop\New folder\Spring 16\Data cleansing\Webscrapping\mapfile')