import pandas as pd
import numpy as np
import  matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap



def clean_data():
    dataframe = pd.read_json(r'C:\Users\shubham\Desktop\New folder\Spring 16\Data cleansing\Webscrapping\mapfile\mapdata.json')
    dataframe = dataframe[dataframe.state !='usa']
    dataframe = dataframe[dataframe.company!='University of Minnisota']

    dataframe['lat'] = dataframe.apply(lambda row:create_new_column_lat(row),axis=1)
    dataframe['lon'] = dataframe.apply(lambda row:create_new_column_lon(row),axis=1)

    dataframe.to_html('mapdataclean.html')
    dataframe.to_csv('mapdataclean.csv')
    dataframe.to_json('mapdataclean.json')



def create_new_column_lat(row):
    return round(float(list(row['coordinates'])[0]),6)

def create_new_column_lon(row):
    return round(float(list(row['coordinates'])[0]),6)

def map_data():
    jobs = np.genfromtxt('mapdataclean.csv', delimiter=',', dtype=[('lat',np.float32, ('lon',np.float32))],usecols =(10,11))

    themap = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,projection='11c')
if '__main__'==__name__:
    clean_data()