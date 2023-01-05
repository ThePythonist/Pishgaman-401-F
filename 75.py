def f(x, y):
    # Sharte payan
    if y == 1:
        return x
    # Sharte edame
    else:
        return x + f(x, y - 1)


print(f(3, 6))
