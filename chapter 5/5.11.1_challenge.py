#result = 1
#n = 2
#while n < 5:
#    print(n, end=' ')
#    result *= 2
#    n += 1
#else:
#    print(f'/ {result}')
#print('done')

#result = 1
#n = 1
#while n < 8:
#    print(n, end=' ')
#    result *= 4
#    if result > 241:
#        print('*')
#        break
#    n += 1
#else:
#    print(f'\ {result}')
#print('done')


#result = 0
#for n in range(5):
#    print(n, end=' ')
#    result -= 4
#else:
#    print(f'\ {result}')
#print('done')


#stop = -20
#total = 0
#for number in [6, 6, 7, 5, 6, 6]:
#    print(number, end=' ')
#    total -= number
#    if total < stop:
#        print('!')
#        break
#else:
#    print(f'/ {total}')
#print('done')

# this is 5. 12.1

numbers = [4, -7, 9, -2, -1, -6]
for position, number in enumerate(numbers):
    if number < 0:
        print(f'{position} x')
    else:
        print(f'{position} {number}')