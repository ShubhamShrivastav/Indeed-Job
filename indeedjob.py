from bs4 import BeautifulSoup
import requests
import json
import os.path
from multiprocessing.dummy import Pool as Threadpool
import uuid
import  pool

######
#http://www.indeed.com/jobs?q=data+scientist#
#####

def getdata(url):
    save_path=r'C:\Users\shubham\Desktop\New folder\Spring 16\Data cleansing\data'
    joblist=[]
    html= requests.get(url).text
    soup = BeautifulSoup(html,'html5lib')
    sponsered_job = soup.find_all('div',{'class':'row result'})
    for sjob in sponsered_job:
        joblist.append(
                {
                    'title':sjob.find('a').text,
                    'company':sjob.find('span', {'class':'company'}).text.strip(),
                    'location':sjob.find('span', {'class':'location'}).text
                }
            )
    jobs =soup.find_all('div',{'class':' row result'})
    for job in jobs:
        joblist.append(
             {
                    'title':job.find('a').text,
                    'company':job.find('span', {'class':'company'}).text.strip(),
                    'location':job.find('span', {'class':'location'}).text
                }
        )
    with open(os.path.join(save_path,'data_'+str(uuid.uuid1())+'.json'),'w') as outfile:
        json.dump(joblist,outfile)


if '__main__' ==__name__:
    urls=[]
    urls.append(r'http://www.indeed.com/jobs?q=data+scientist&l=')
    for i in range(20,990,10):
        urls.append(r'http://www.indeed.com/jobs?q=data+scientist&start='+str(i))

    pool = Threadpool(25)
    pool.map(getdata, urls)


    pool.close()
    pool.join()