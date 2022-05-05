def graph_1(f):
    for i in range(0, 11):
        print(f'f({i}) = {f(i)}', end=' ')


f1 = lambda x: x ** 2
graph_1(f1)


def f2(x):
    return x ** 2


graph_1(f2)


def graph_2(f, n=10):
    for i in range(0, n + 1):
        print(f'f({i}) = {f(i)}', end=' ')


def graph_3(f, m=0, n=10):
    for i in range(m, n + 1):
        print(f'f({i}) = {f(i)}', end=' ')

f = lambda x: x ** 2
graph_3(f, )

def eat(*x):
    flag = False
    for part in x:
        if part % 2 == 0:
            flag = True
            break
    if flag:
        print('ok')
    else:
        print('I like evens')


def repeat(**x):
    ans = [elem.split() * x[elem] for elem in x]
    print([i for j in ans for i in j])
