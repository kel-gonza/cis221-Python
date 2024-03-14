
#result = 0
#
#for n in range(7):
#    result = n - 4
#    
#    if (result % 2) != 0:
#        print('_', end=' ')
#        continue
#    
#    print(result, end=' ')
#
#print('done')

#a = int(input())
#b = int(input())
#c = int(input())
#
#while a < b:
#    print(a)
#    
#    if a > c:
#        break
#    
#    a += 5


#stop = int(input())
#
#for a in range(5):
#    result = 0
#    
#    for b in range(3):
#        result += a + b
#    
#    print(result)
#    
#    if result > stop:
#        break


stop = int(input())
result = 0

for a in range(5):
    print(a + 1, end=': ')
    
    for b in range(3):
        result += a + 1
        
        if result > stop:
            print('_', end=' ')
            continue
        
        print(result, end=' ')
    
    print()