def sort(items):
    # items.sort()
    # return items[::-1]
    items.sort(reverse=True)
    return items

lst = [11, 2, 3, 4, 5, 1, 12, 15]
print(sort(lst))
