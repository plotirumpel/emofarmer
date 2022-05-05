def file_1(name):
    with open(name, mode="w", encoding="utf-8") as f:
        for i in range(1, 101):
            print(i, file=f)


def file_2(name):
    def cats(x):
        if x % 100 >= 11 and x % 100 <= 19:
            return str(x) + " котов"
        else:
            if x % 10 == 1:
                return str(x) + " кот"
            elif x % 10 >= 2 and x % 10 <= 4:
                return str(x) + " кота"
            elif x % 10 == 0 or (x % 10 >= 5 and x % 10 <= 9):
                return str(x) + " котов"

    with open(name, mode="w", encoding="utf-8") as f:
        for i in range(1, 1000):
            print(cats(i), file=f)


def file_3(name):
    def chislo(x):
        a = ["", "один", "два", "три", "четыр", "пят", "шест", "сем", "восем", "девят", "десять", "одиннадцать",
             "двенадцать"]
        b = ["сто", "двести", "триста", "четыреста"]
        if x // 100 > 0:
            z = x // 100
            if x % 100 == 0:
                if z < 5:
                    return b[z - 1]
                else:
                    return a[z] + "ьсот"
            else:
                return chislo(x - x % 100) + ' ' + chislo(x % 100)

        elif x / 10 >= 1:
            if x < 13:
                return a[x]
            elif x < 20:
                return a[x % 10] + "надцать"
            elif x % 10 == 0:
                z = x // 10
                if z < 4:
                    return a[z] + "дцать"
                elif z == 4:
                    return "сорок"
                elif z == 9:
                    return "девяносто"
                else:
                    return a[z] + "ьдесят"
            elif x % 10 != 0:
                return chislo(x - x % 10) + ' ' + chislo(x % 10)

        else:
            if x == 4:
                return a[x] + 'е'
            if x < 4:
                return a[x]
            if x > 4:
                return a[x] + 'ь'

    def cats(x):
        if x % 100 >= 11 and x % 100 <= 19:
            return "котов"
        else:
            if x % 10 == 1:
                return "кот"
            elif x % 10 >= 2 and x % 10 <= 4:
                return "кота"
            elif x % 10 == 0 or (x % 10 >= 5 and x % 10 <= 9):
                return "котов"

    with open(name, mode="w", encoding="utf-8") as f:
        for i in range(1, 1000):
            print(chislo(i), cats(i), file=f)


def file_4(name):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    with open(name, mode="r", encoding="utf-8") as f:
        counter = 0
        text = f.read()
        for i in range(0, len(text)):
            if text[i] in alphabet:
                counter += 1
    return counter
