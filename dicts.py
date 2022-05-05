import string


def dicts_1(dictionary, string):
    ans = [dictionary.get(char) if dictionary.get(char) != None else char for char in string]
    return ('').join(ans)


def dicts_2(string):
    ans = {char: string.count(char) for char in string}
    return ans


def dicts_3(text):
    words = text.split()
    removed_punct = [i.strip(string.punctuation) for i in words]
    ans = {word: removed_punct.count(word) for word in removed_punct}
    return ans


def dicts_4(name, name2):
    with open(name, mode="r", encoding="cp1251") as f, open(name2, mode="w", encoding="cp1251") as g:
        all_lines = f.readlines()
        all_lines = [line.strip() for line in all_lines]
        dictt = dicts_3(str(all_lines))
        for word, counter in dictt.items():
            stri = f'{word};{counter}'
            g.write(stri + '\n')
