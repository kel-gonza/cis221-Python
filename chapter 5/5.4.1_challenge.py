#n = 1
#while n <= 6:
#    print(n - 2)
#    n = n + 1

#n = 4
#while n > 0:
#    print(n - 2)
#    n = n - 1

#target = int(input())
#n = int(input())
#while n <= target:
#    print(n * 2)
#    n += 1

target = int(input())
n = int(input())
step = 2
while n >= target:
    print(n * 2)
    n -= step