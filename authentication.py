#!/usr/bin/python3

from employee_data import *

def authenticate(Employee_Data):
    pass_id_try = 0
    MAX_ATTEMPTS = 3
    
    while pass_id_try < MAX_ATTEMPTS:
        input_id = int(input("Please Enter User ID: "))
        input_password = input("Please Enter User Password: ")
        
        if input_id != Employee_Data["ID"]:
            print("Invalid ID. Please enter it correctly.")
        elif input_password != Employee_Data["Password"]:
            print("Invalid Password. Please try again.")
        else:
            print("Login Successful")
            print("\n")
            return 1           
        
        pass_id_try += 1
    
    print("Access denied. Maximum login attempts exceeded.")
    return 0

