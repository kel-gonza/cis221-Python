colors_set1 = {'ivory'}
colors_set2 = set()
colors_set2.add(input())
colors_set2.add(input())

colors_set1.update(colors_set2)
colors_set1.add(input())
colors_set1.pop()

print(f'colors_set1: {sorted(colors_set1)}')
print(f'colors_set2: {sorted(colors_set2)}')