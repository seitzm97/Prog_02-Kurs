# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 11:26:17 2022

@author: Seitz
"""

import bankaccount as bk
import saving_account as sa
import youth_account as ya


#Accountcreation
acc1 = bk.BankAccount("Michael Seitz","Elggerstrasse 5","0786426678","05.02.1997")
acc2 = sa.SavingAccount("Yannick Seitz","Frauenackerstrasse 5","0785245578","14.09.1995")
acc3 = ya.YouthAccount("Joel Müller","Hauptstrasse 45", "0799942554","05.08.2005")

#Depositing on the accounts
acc1.deposit(50000)
acc2.deposit(150000)
acc3.deposit(20000)

#Printing all data of the accounts
print(vars(acc1),"\n")
print(vars(acc2),"\n")
print(vars(acc3),"\n")

#Testing restrictions on BankAccount(acc1)
#1. Exceeding the limit of 100'000 on the Bankaccount (expected print is "You are exceeding the maximal amount of money on your account.")
acc1.deposit(52000)
#2. Trying to reach a negative balance (expected print is "You are not allowed to have a negative balance on your account.")
acc1.withdraw(51000)
print("\n")

#Testing on SaveAccount(acc2)
#1. Testing 3 months of interest
print(acc2.balance,"\n")
acc2.sleep(30)
print(acc2.balance,"\n") #with an interest rate of 0.1% the expected new balance should be 150450.45

#2. Testing the additional 2% charge when withdrawing more than there is on the account
acc2.withdraw(160450.45015) #going 10000 under the balance of 0 /the expected additional charge is 200
print(acc2.balance,"\n") #the expected balance should be -10200

#3. Testing a change of the interest rate
acc2.interest_change() #changing the interest rate
acc2.sleep(10) #One month of interest
print(acc2.balance,"\n") #with 1% of interest there should now be a dept of 10302

#Testing on YouthAccount
#1. Trying to create a YouthAccount for someone older than 25
acc4 = ya.YouthAccount("Max Muster", "Musterstrasse 1", "0777777777", "01.01.1995") #This is supposed to cause an Error

#2. Trying to withdraw more than 2000 in one month(10 seconds)
acc3.withdraw(1500) #should work
acc3.withdraw(600) #should not work

#3. Waiting a month to withdraw the additional 600
acc3.sleep(10) #waiting a month
acc3.withdraw(600) #should work now
print(acc3.balance,"\n") #should be 18270

#4. Testing the default interest of 2%
acc3.sleep(10)
print(acc3.balance) #should be 18635.4