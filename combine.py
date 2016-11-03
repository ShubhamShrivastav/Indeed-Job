import os
import pandas as pd

def combine_file(share,save_to):
    data = pd.DataFrame(pd.concat([pd.read_json(os.path.join(share,file)) for file in os.listdir(share)], ignore_index=True))
    data.to_csv(os.path.join(save_to,'combined.csv'))
    data.to_html(os.path.join(save_to,'combined.html'))
    data.to_json(os.path.join(save_to,'combined.json'))





if'__main__' == __name__:
    combine_file(r'C:\Users\shubham\Desktop\New folder\Spring 16\Data cleansing\data',r'C:\Users\shubham\Desktop\New folder\Spring 16\Data cleansing\combined')
