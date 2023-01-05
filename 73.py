def f(x, y):
    # Sharte payan
    if y == 1:
        return x + 1
    # Sharte edame
    else:
        return 1 + f(x, y - 1)


print(f(2, 4))
