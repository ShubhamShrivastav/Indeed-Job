import os
import pandas as pd


def add_columns(share,save_to):
    #read json data into dataframe objct
    data = pd.read_json(share)
    data['city'] =data.apply(lambda  row: create_new_column_city(row), axis=1)
    data['state'] =data.apply(lambda  row: create_new_column_state(row), axis=1)
    data['level'] =data.apply(lambda  row: create_new_column_position_type(row), axis=1)
    data.to_csv(os.path.join(save_to,'added_col.csv'))
    data.to_html(os.path.join(save_to,'added_col.html'))
    data.to_json(os.path.join(save_to,'added_col.json'))

def create_new_column_city(row):
    return str(row['location'].split(',')[0])

def create_new_column_state(row):
    if row['location'] == 'United States' or row['location'] == 'Home Based':
        return 'USA'
    else:
        return str(row['location'].split(',')[1].split()[0])

def create_new_column_position_type(row):
    if  'Sr.' in row['title']:
        return 'Senior'
    elif 'Senior' in row['title']:
        return 'Senior'
    elif 'architect' in row['title']:
        return 'Senior'
    elif 'Jr' in row['title']:
        return 'Junior'
    else:
        return 'midlevel'




if'__main__' == __name__:
    add_columns(r'C:\Users\shubham\Desktop\New folder\Spring 16\Data cleansing\combined\combined.json',r'C:\Users\shubham\Desktop\New folder\Spring 16\Data cleansing\clean')