# jangan lupa diinstall dulu yang belum terinstall yaa
import requests
import os
import numpy as np
from datetime import datetime, timedelta
import pandas as pd
from io import StringIO
import logging
import http.client #pip install python-http-client
import csv
import time

http.client.HTTPConnection.debuglevel = 1
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

lsids= []
now = datetime.now()
year = now.strftime("%Y")
before = datetime.now() - timedelta(minutes = 30)
# dt_b = before.strftime("%Y-%m-%d %H.%M.%S")
# dt_n = now.strftime("%Y-%m-%d %H.%M.%S")

dt_b = ("24/11/2023")
dt_n = ("31/12/2023")

list_tma= 'id_stasiun.txt' # tinggi muka air

class SN(object):
        def __init__(self, value):
                self.storage = value

def generateAPI():
    with open(list_tma) as lfl:
            for lf in lfl:
                    lsids.append(lf.replace('\n',''))
            #looping get Data sampai pintu air terakhir
            for ids in lsids:
              print("GET pintu air id :"+ids)
              response = requests.get('https://poskobanjirdsda.jakarta.go.id/Pages/GenerateDataTinggiAir.aspx?IdPintuAir='+ids+'&StartDate='+dt_b+'&EndDate='+dt_n)
              # jadikan dataframe
              response = response.text

              # delete data terakhir
              isi_data = response.split("|")[0]
              split_data = isi_data.split(';')
              data_mentah = "|".join(split_data)
              raw_data = pd.read_csv(StringIO(data_mentah), sep="|", header=None)
              raw_data = raw_data.T
              raw_data = raw_data.dropna()

              # ubah pisisi index get_time dan value
              def split_data(row):
                     row['get_time'] = datetime.strptime(row[0].split(',')[0], '%Y-%m-%d %H.%M.%S')
                     row['value'] = row[0].split(',')[1]
                     return row
              raw_data = raw_data.apply(split_data, axis=1)
              raw_data = raw_data.iloc[:,1:]

              #tambah column id pintu air sesuai id stasiun
              raw_data.insert(loc=0, column='ids', value=ids)

              #save ke bentuk csv dengan format TMA_ids_thn.csv
              raw_data.to_csv(ids+'_'+year+'.csv',  mode='a', index = False, header=None)
              header = ["ids", "get_time", "value"]
              data = pd.read_csv(ids+'_'+year+'.csv', names=header)

              # dropping ALL duplicates values
              data.drop_duplicates(subset=['get_time'], keep=False)
             
              #insert data update into the last row
              data.to_csv(ids+'_'+year+'.csv',index=False, header=None)

if __name__ == '__main__':
       generateAPI()
        #  insertDB()
       print("get data finish")

       ## tambahan kalau mau save ke database
        # def insertDB():
        #        conn = psycopg2.connect(database=' ', user=' ', password=' ', host='127.0.0.1')
        #        cursor = conn.cursor()

        #        with open(list_tma) as lfl:
        #             for lf in lfl:
        #                     lsids.append(lf.replace('\n',''))
        #             #looping get Data sampai pintu air terakhir
        #             for ids in lsids:
        #               with open(ids+'_'+year+'.csv', 'r') as f:
        #                      reader = csv.reader(f)
        #                      next(reader) # Skip header.
        #                      for row in reader:
        #                             cursor.execute("INSERT INTO tma(ids,get_time,value) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING", row)

        #        conn.commit()
        #        conn.close()
        #        return