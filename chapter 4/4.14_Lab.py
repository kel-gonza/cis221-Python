"""
    File: main.py 
    Description: Write a program whose inputs are three integers, and whose output is the smallest of the three values.
    Author: Kelly Gonzalez
    Email: kellyg6294@student.vvc.edu
    Course#: cis221
    Section#: 30792
    Date: 03/07/2024

    ex. if the inputs are :
    7
    15
    3
    the output will be :
    3
"""
first_number = int(input())
second_number = int(input())
third_number = int(input())

if (first_number <= second_number) and (first_number <= third_number):
    print(first_number)
elif (second_number <= first_number) and (second_number <= third_number):
    print(second_number)
elif (third_number <= first_number) and (third_number <= second_number):
    print(third_number)