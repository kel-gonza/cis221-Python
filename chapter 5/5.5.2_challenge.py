num_in = int(input())
number_list = []
for i in range(num_in):
    number_list.append(int(input()))

print(f'List has {num_in} elements:')

output=""
for number in number_list:
    new_num = f'({number})'
    output += new_num
print(output)
