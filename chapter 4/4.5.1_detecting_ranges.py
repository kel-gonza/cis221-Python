# challenge number 1
num_people = int(input("Please input a number of people: "))

# Modify the following line
if (num_people < 8000) or (num_people > 19000):
    print('Not a small university')
else:
    print('Small university')

# challenge #2

enrollment_input = int(input())

if (enrollment_input >= 1100) and (enrollment_input <= 4300):
    print('Mid-size town.')
else:
    print('Not a mid-size town.')

# challenge #3
silver_input = int(input())

if silver_input <= 960:
    print('Silver: solid state')
elif (silver_input > 960) and (silver_input < 2170):
    print('Silver: liquid state')
else:
    print('Silver: gaseous state')