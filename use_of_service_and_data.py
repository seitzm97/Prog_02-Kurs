# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 16:22:51 2022

@author: Michael
"""

import requests
import time
import pandas as pd
from prettytable import PrettyTable

def bill_of_materials():   
    response = requests.get("http://160.85.252.148")
    return response

def get_relevant_data():
    while True:  
        try:
            bom = bill_of_materials()
        except Exception: #Even if the server is offline, the script will not be interrupted
            pass
        if bool(bom) == False: #Empty dictionaries evaluate to False
            time.sleep(1)
            pass
        else:
            bom = bom.json()
            break #If the dictionary contains Data, the while loop will break
    return bom

def data_cleaner():
    data = get_relevant_data()
    data_df = pd.DataFrame(list(data.items()), columns=['Item', 'Price'])
    data_df = data_df[pd.to_numeric(data_df['Price'], errors='coerce').notnull()]
    data_df['Price'] = data_df.Price.abs()
    return data_df
    

def receipt():
    df = data_cleaner()
    total_price = df['Price'].sum()
    x = PrettyTable()
    x.field_names = ["Item", "Price"]
    for index, row in df.iterrows():
        x.add_row([row["Item"],row["Price"]])
    print(x)
    x.add_row(['Total', total_price])
    print( "\n".join(x.get_string().splitlines()[-2:]) )
    
#Test
receipt()