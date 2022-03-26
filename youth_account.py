# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 10:39:19 2022

@author: Michael
"""

import bankaccount as bk

class YouthAccount(bk.BankAccount):
    def __init__(self, name, address, phone, date_of_birth):
        bk.BankAccount.__init__(self,name, address, phone, date_of_birth)
        if self.age > 25:
            raise ValueError("The customer is too old for a youth account.")
        self.rate = 0.02
        self.limit = 2000
        self.account_type = "Youth account"
        
    def interest(self):
        interest_rate = self.rate
        self.balance = self.balance + (interest_rate*self.balance)
        
    def withdraw(self,amount):
        if amount > 2000:
            raise ValueError("You are not allowed to withdraw more than 2000 per month.")
        else:
            self.balance = self.balance - amount
            self.limit = self.limit - amount
            if self.limit < 0:
                print("You are exceeding the limit of 2000 per month. Redoing your withdraw...")
                self.limit = self.limit + amount
                self.balance = self.balance + amount
            else:
                pass
    
    
            