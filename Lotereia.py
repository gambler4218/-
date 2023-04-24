from random import choice
nachalo = [54, 'q', 67, 32, 'f', 5, 7, 82, 't', 1, 89, 'b', 52, 45, 'e']
my_ticket = [89, 't', 52, 'f']
flag = 0
flag_1 = 0
konec = []
vigrish = []
c = 0
while c != 1:
    while flag < 4:
        vibor = choice(nachalo)
        konec.append(vibor)
        flag += 1

    for a in konec:
        if konec.count(a) > 1:
            break
        if a in my_ticket:
            vigrish.append(a)
        if len(vigrish) == 4:
            print('Pobeda')
            print(vigrish)
            c = 1

    vigrish = []
    konec = []
    flag_1 += 1
    flag = 0
print(flag_1)
print(my_ticket)
