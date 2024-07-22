#! /usr/bin/python3

Employee_Info = {
    "Name": "Mahmoud Hamdy Elseedy",
    "ID": 1,
    "Department": "Mechatronics",
    "Salary": 5000,
    "Days_of_Absence": 10,
    "Password": '7474'
}

def display_info(employee_data):
    print("\n")
    for key, value in employee_data.items():
        print(f"{key}: {value}")