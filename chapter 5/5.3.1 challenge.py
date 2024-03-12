curr_age = int(input())

while (curr_age < 16 or curr_age > 60):
    if curr_age < 16:
        print('20% discount')
    else:
         print('15% discount')
    curr_age = int(input())

print('Regular ticket price')