str = input()
c = 0

for char in str[:-1]:
    c += 1
    if c == 3:
        continue
    else:
        if char == 'c':  #английская c
            print('Найден символ c')
        else:
            print(char)