# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 15:11:18 2022

@author: Michael
"""

from urllib.request import urlopen
import requests
import time


def bill_of_materials():   
    response = requests.get("http://160.85.252.148")
    return response

while True:  
        try:
            bom = {}
            bom = bill_of_materials()
        except Exception: #Even if the server is offline, the script will not be interrupted
            pass
        if bool(bom) == False: #Empty dictionaries evaluate to False
            time.sleep(1)
            pass
        else:
            break #If the dictionary contains Data, the while loop will break
    
    