immutable_var = 'слово', 'буква', 'число', 'цифра', 1, 5, 25
print(immutable_var)
mutable_list = ['слово', 'буква', 'число', 'цифра', 1, 5, 25]
print(mutable_list)
print(mutable_list[2])
mutable_list[2] = 1000
print(mutable_list)
# в отличие от кортежа список можно изменять (число >> 1000)