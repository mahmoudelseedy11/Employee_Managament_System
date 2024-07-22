#!/usr/bin/python3

from employee_data import *

def Calculate_Bonus(employee_data):
    return 0.1 * employee_data["Salary"]

def calculate_discount(employee_data):
    return 0.05 * employee_data["Salary"]

def remind_legal_holidays(employee_data):
    return employee_data["Days_of_Absence"]
