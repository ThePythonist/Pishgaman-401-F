lst = [1, 2, 3, [4, 5], 6, 7, [8, 9]]

for i in lst:
    try:
        for j in i:
            print(j)
    except TypeError:
        print(i)
