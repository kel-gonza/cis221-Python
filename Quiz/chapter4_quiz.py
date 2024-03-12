score = 65
group = ''
if score <= 60:
    group = group + 'A'
if score <= 70:
    group = group + 'B'
if score <= 80:
    group = group + 'C'
else:
    group = group + 'D'
print(group)

grade = 75

if grade < 50:
     print("F")


elif grade < 60:
     print("D")


elif grade < 75:
     print("C")


elif grade < 85:
     print("B")


elif grade <= 100:
     print("A")


else:
     print("Invalid grade")

x = 2
y = 3
z = 10

print(x + y < y - z * 2)

day = 23
if day % 10 == 1:
    ending = "st"
elif day % 10 == 2:
    ending = "nd"
elif day % 10 == 3:
    ending = "rd"
else:
    ending = "th"
print(str(day) + ending)

a = 12
test_val = 6
if a * 2 == test_val:
    a = a + 7
else:
    test_val = 2 * a


test_val = a + 1

print(test_val)

x = 17
if x * 2 <= 34:
    x = 0
else:
    x = x + 1
 
x = x + 1

print(x)