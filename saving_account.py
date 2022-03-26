# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 09:48:06 2022

@author: Michael
"""

import bankaccount as bk


class SavingAccount(bk.BankAccount):
    def __init__(self,name, address, phone, date_of_birth):
        bk.BankAccount.__init__(self, name, address, phone, date_of_birth)
        self.rate = 0.001
        self.account_type = "Saving account"
        
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def interest_change(self):
        self.rate=int(input("What is the desired rate in %?"))/100
        return self.rate
        
    def interest(self):
        rate = self.rate
        self.balance = self.balance + (rate*self.balance)
        
    def withdraw(self, amount):
        self.balance = self.balance - amount
        if self.balance < 0:
            dept = 0 - self.balance
            add_charge = (dept/100)*2
            self.balance = self.balance - add_charge
        else:
            pass
    
    
    

