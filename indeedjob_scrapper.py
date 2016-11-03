from bs4 import BeautifulSoup
import requests
import json
import os.path
from multiprocessing.dummy import Pool as Threadpool
import uuid

######
#http://www.indeed.com/jobs?q=data+scientist#
#####

def getdata(url):
    save_path=r'C:\Users\shubham\Desktop\New folder\Spring 16\Data cleansing\data'
    joblist=[]
    html= requests.get(url).text
    soup = BeautifulSoup(html,'html5lib')
    sponsered_job = soup.find_all('div',{'class':' row result'})
    for sjob in sponsered_job:
        joblist.append(
                {
                    'title':sjob.find('a').text,
                    'company':sjob.find('span', {'class':'company'}).text.strip(),
                    'location':sjob.find('span', {'class':'location'}).text
                }
            )
    print (joblist)

getdata('http://www.indeed.com/jobs?q=data+scientist&l=')