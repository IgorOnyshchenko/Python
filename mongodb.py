# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:59:34 2015

@author: User
"""
import json
from pymongo import MongoClient

#EXPORT TO MONGO      
            
client = MongoClient('localhost', 27017)
db = client.ssprequest
all_us_dsp = db['all_us_dsp']

n=0
n_lines=0
with open("d:/logs/all-US-dsp.log",encoding="utf8") as f:
    
    for line in f:
        
        if 'Date' in line[:-1]:
            date=line[:-1]
            
        if 'SSP content' in line[:-1]:
            SSP=line[14:-2]
            
        if 'DSP' in line:
            
            if '==' in line:
                pass
            
            elif 'DSP content' in line:
                pass
            
            elif 'response' in line:
                pass
            
            elif 'time' in line:
                DSP_rsp=line
                
            else:
                DSP=line
                
        if 'statusCode' in line[:-1]:
            
            status=line[:-1]
            doc={'date': date,
                     'request': json.loads(SSP),
                    'dsp': DSP[:DSP.find('-')],
                    'dsp_time_resp': DSP_rsp,
                    'status': status}
            all_us_dsp.insert(doc)
            n_lines+=1
            
            if n_lines%500000==0:
                print(n_lines)

          