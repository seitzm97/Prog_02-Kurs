# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 08:58:18 2022

@author: Seitz
"""
import bankaccount as bk
import saving_account as sa
import youth_account as ya
import sys


#To test just run this file
class BankApp():    
    def __init__(self):
        self.acc_creator()
        
    def menu(self,option_1, option_2, option_3, option_4, option_5, option_6):
        print(20*"-","MENU",20*"-")
        print("1. ", option_1)
        print("2. ", option_2)
        print("3. ", option_3)
        print("4. ", option_4)
        print("5. ", option_5)
        print("6. ", option_6)
        print(46*"-")
        self.choice = int(input("Please choose an option."))
        
    def owner(self, name, address, phone, date_of_birth):
        bk.BankAccount.owner(self, name, address, phone, date_of_birth)
        
    #After creating an account initally you need to use the selecter to manage the existing accounts or create new ones
    def selecter(): 
        acc = input("Please type the accounts name you'd like to manage: ")
        accounts[acc].action()
    
    def action(self):
        while True:
            self.menu("Deposit","Withdraw","Create another account","Delete/Close the account","Tax report", "Exit")
            if self.choice == 1:
                amount = int(input("Please enter the amount you would like to deposit."))
                if self.account_type == "Bank account" or self.account_type == "Youth account":
                    bk.BankAccount.deposit(self, amount)
                if self.account_type == "Saving account":
                    sa.SavingAccount.deposit(self, amount)
            if self.choice == 2:
                amount = int(input("Please enter the amount you would like to withdraw."))
                if self.account_type == "Bank account":    
                    bk.BankAccount.withdraw(self, amount)
                if self.account_type == "Saving account":
                    sa.SavingAccount.withdraw(self, amount)
                if self.account_type == "Youth account":
                    ya.YouthAccount.deposit(self, amount)
            if self.choice == 3:
                dict_key = input("Please give your new account a new name.")
                accounts[dict_key] = BankApp()
                break
            if self.choice == 4:
                dict_key = input("Please enter the accounts name. ")
                accounts.pop(dict_key)
                break
            if self.choice == 5:
                TaxReport.generate(self)
                break
            if self.choice == 6:
                print("Leaving the Menu")
                del self.choice
                break
            
    def deleter(self):
        del self.name, self.account_type, self.choice,self.rate, self.address, self.age, self.balance, self.birthdate, self.date_of_birth, self.iban, self.opening_date, self.phone
    
    def acc_creator(self):
        self.menu("Bank account", "Saving account", "Youth account","Exit", "--", "--")
        if self.choice == 4:
            sys.exit("Exitiing the application")
        self.name = input("What is your name. ")
        self.address = input("Please enter your address. ")
        self.phone = input("Please enter your phone. ")
        self.date_of_birth = input("Please enter your date of birth in the format dd.mm.yyyy. ")
        if self.choice == 1:
            self.account_type = "Bank account"
            bk.BankAccount.__init__(self, self.name, self.address, self.phone, self.date_of_birth)
        if self.choice == 2:
            self.account_type = "Saving account"
            sa.SavingAccount.__init__(self, self.name, self.address, self.phone, self.date_of_birth)
        if self.choice == 3:
            self.account_type = "Youth account"
            ya.YouthAccount.__init__(self, self.name, self.address, self.phone, self.date_of_birth)
        else:
            pass
            

class TaxReport(BankApp):    
    def generate(self):
        print("Tax report 2022 for fiscal year 2021")
        print("**",self.account_type,"**", self.balance, "CHF")


if __name__ == '__main__':
    acc_name = str(input("You don't have an account yet.Enter an account name: "))
    accounts = {acc_name:BankApp()}
    del acc_name
else:
    print("BankApp has been imported.")
    pass


        
