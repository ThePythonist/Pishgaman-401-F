txt = "I love python programming"


def f1(text):
    lenghts = [len(i) for i in text.split()]
    maximum = max(lenghts)

    for i in text.split():
        if len(i) == maximum:
            return i


# print(f1(txt))

txt2 = "I am a backend engineer"


def f2(text):
    text = text.split()
    text.sort(key=len)
    return text[-1]


print(f2(txt2))
