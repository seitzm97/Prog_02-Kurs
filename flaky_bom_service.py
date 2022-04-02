# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 15:11:18 2022

@author: Michael
"""

from urllib.request import urlopen
import json


def bill_of_materials():   
    url = "http://160.85.252.148"
    page = urlopen(url)
    data_json = json.loads(page.read())
    return data_json

while True:  
        try:
            bom = {}
            bom = bill_of_materials()
        except Exception: #Even if the server is offline, the script will not be interrupted
            pass
        if bool(bom) == False: #Empty dictionaries evaluate to False
            pass
        else:
            break #If the dictionary contains Data, the while loop will break
    
    
