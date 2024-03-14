
#colors = ['tan', 'cyan', 'pink', 'grey']
#for color in colors:
#    print(color)

#word = 'Stack'
#for char in word:
#    print(char, end='/')
#print()

cities = {
    'Rome': 3435,
    'Toronto': 584,
    'Austin': 438,
    'Nairobi': 982,
}

best = ''
distance = 0
for city in cities:
    if cities[city] > distance:
        best = city
        distance = cities[city]
print(best, distance)