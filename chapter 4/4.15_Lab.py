"""
    File: main.py 
    Description: Write a program that tells the user if it is an auxiliary or primary highway.
    Author: Kelly Gonzalez
    Email: kellyg6294@student.vvc.edu
    Course#: cis221
    Section#: 30792
    Date: 03/09/2024
"""
highway_number = int(input())
string_highway_num = str(highway_number)
extracted_highway_num = abs(highway_number) % 100

if len(string_highway_num) == 2 or len(string_highway_num) == 1 and highway_number != 0:
    if highway_number % 2 == 0:
        print(f'I-{highway_number}, is a primary, going east/west.')
    else:
        print(f'I-{highway_number}, is a primary, going north/south.')
if len(string_highway_num) == 3 and extracted_highway_num != 00:
    if extracted_highway_num % 2 == 0:
        print(f'I-{highway_number} is auxiliary, serving I-{extracted_highway_num}, going east/west.')
    else:
        print(f'I-{highway_number} is auxiliary, serving I-{extracted_highway_num}, going north/south.')

if highway_number == 0 or extracted_highway_num == 00:
    print(f'{highway_number} is not a valid interstate highway number.')


