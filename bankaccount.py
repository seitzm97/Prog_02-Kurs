# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 10:09:12 2022

@author: Seitz
"""

import random as rd
import datetime as dt
import time

class BankAccount():
    def __init__(self, name, address, phone, date_of_birth):
        default = 0
        identifier_nr = rd.randint(1000000000000000000,9999999999999999999)
        self.iban = "CH"+str(identifier_nr)
        self.balance = default
        self.today = dt.date.today()
        self.owner(name, address, phone, date_of_birth)
        
    def owner(self, name, address, phone, date_of_birth):
        self.name = name
        self.address = str(address)
        self.phone = str(phone)
        self.birthdate = dt.datetime.strptime(date_of_birth, "%d.%m.%Y") #Turning date of birth to age
        self.age = self.today.year - self.birthdate.year - ((self.today.month, self.today.day) < (self.birthdate.month, self.birthdate.day))
        
    def deposit(self,amount):
        self.balance = self.balance + float(amount)
        if self.balance < 100000:
            pass
        else:
            self.balance = self.balance - float(amount)
            print("You are exceeding the maximal amount of money on your account.")
            
    def withdraw(self,amount):
        self.balance = self.balance - float(amount)
        if self.balance < 0:
            print("You are not allowed to have a negative balance on your account.")
            self.balance = self.balance + float(amount)
        else:
            pass
        
    def sleep(self,secs):
        trig = secs/10
        for i in range(0,int(trig)):
            self.interest()
            time.sleep(10)
            #this was for testing: print(self.balance)
            self.limit = 2000
            
            
if __name__ == "__main__":
    print("File bankaccount.py is executed directly.")
else:
    print("File bankaccount.py has been imported.")