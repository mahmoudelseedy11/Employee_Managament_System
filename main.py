#! /usr/bin/python3

from employee_data import *
from authentication import *
from operations import *

print("Welcome to the Employee Managament System")
print("Please login to continue.")

if "__main__" == __name__:
        while authenticate(Employee_Info):
            print("Select an option")
            print("1. Display Employee Information")
            print("2. Calculate Bonus")
            print("3. Calculate Discount")
            print("4. Remind Legal Holidays")
            print("5. Exit")

            print("\n")
            Choice = int(input("Enter your choice: "))

            if (Choice ==1):
                display_info(Employee_Info)
            elif(Choice == 2):
                bonus = Calculate_Bonus(Employee_Info)
                print("Congratulations! You Have a Bonus Salary =",bonus)
            elif(Choice == 3):
                discount = calculate_discount(Employee_Info)
                print("Unfortunately, There is a discount of your salary =",discount)
            elif(Choice == 4):
                holidays=remind_legal_holidays(Employee_Info)
                print("You have a remind legal holidays = {} ,make Sure to use them as smart as you can".format(holidays))
            elif(Choice == 5):
                print("Thank you for using the Employment Managament System")    
                break 
            else:
                print("You Entered A Wrong Number")

            print("\n")
            if Choice in [1,2,3,4]:
                input("Please press Enter to return to the main menu...")                      
                                    
           





