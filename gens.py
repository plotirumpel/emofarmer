import string


def gens_1(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b


def gens_2(name):
    with open(name, mode='r', encode='utf8') as f:
        while True:
            symb = f.read(1)
            yield symb


def gens_3(text):
    words = text.split()
    ans = [i.strip(string.punctuation) for i in words]
    for i in range(len(ans)):
        yield ans[i]


def gens_4(var1, var2):
    for i in range(len(var1)):
        yield (var1[i], var2[i])


def gens_5(n):
    for i in range(1, n):
        for j in range(0, i):
            yield i
