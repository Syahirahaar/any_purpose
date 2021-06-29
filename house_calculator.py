# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 09:01:42 2021

@author: Syahirahar
"""
# NEXT THINKING OF INSERTING IT INTO A FUNCTION 


#def welcome():
#    print("Welcome to Puchong House, this is a calculator for monthly bill")
#    electric = float(input("Enter Electric bill : "))
 #   water = float(input("Enter Water bill : "))
    

MonthRent = input("Enter Rent Month : ")

BillsRent = input("Enter Bill Month : ")

electric = float(input("Enter Electric bill : "))
water = float(input("Enter Water bill : "))
        
        
orang = int(input("How many people will pay for utilities? : "))


pay_electric = round(electric/orang,2)


pay_water = round(water/orang,2)



internet = int(input("How many will pay for internet? :"))
int_bill = round(94.35/internet,2)






print(" ")
print("*****************************")
print(" ")
print("Details Rent for ",MonthRent, " bill for ", BillsRent , "2021")
print("Electric bill : ", pay_electric)
print("Water bill :", pay_water)
print("Internet bill : ", round(89/internet,2))
print("Total RM to pay : Room Rent + ", round(pay_electric + pay_water,2), " + RM ",int_bill )
print(" ")
print("Bayar kepada MAYBANK NUR SYAHIRAH BINTI AB RAHMAN 151388131022 ")
print("Selewat lewatnya 4HB setiap bulan ")
print("Terima Kasih")
