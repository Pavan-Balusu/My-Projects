list = [1, 2, 3]
for x in int(list[-1]):
    for y in int(list[-2]):
        z = x + y
        list.append(z)
        print(list)
