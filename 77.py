def myhash(x):
    if len(str(x)) == 1:
        return x
    else:
        # figures = [int(i) for i in str(x)]
        # x = sum(figures)
        x = sum([int(i) for i in str(x)])
        return myhash(x)


print(myhash(98124))
