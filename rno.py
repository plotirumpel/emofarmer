def strings(s):
    counter = 0
    for i in range(0, len(s) - 1):
        if (s[i] == "A" and s[i + 1] == "B") or (s[i] == "B" and s[i + 1] == "A"):
            counter += 1
    return counter

def file_the_most_frequent_byte(name3):
    with open(name3, mode="rb") as f:
        all_bytes = f.read()
        counted = {}
        for number in all_bytes:
            if number in counted:
                counted[number] += 1
            else:
                counted[number] = 1
        return max(counted, key = counted.get)

#print (file_the_most_frequent_byte('text.txt'))

def dicts_2(string):
    ans = {}
    for char in string:
        if char in ans:
            ans[char] += 1
        else:
            ans[char] = 1
    return ans

#print (dicts_2('banana'))

import string
def dicts_3(text):
    words = text.split()
    removed_punct = [i.strip(string.punctuation) for i in words]
    ans = {}
    for word in removed_punct:
        if word in ans:
            ans[word]+=1
        else:
            ans[word]=1
    return ans

def dicts_4(name, name2):
    with open(name, mode="r", encoding="cp1251") as f, open(name2, mode="w", encoding="cp1251") as g:
        all_lines = f.read().lower()
        dictionary = dicts_3(all_lines)
        for word, counter in dictionary.items():
            strin = f'{word};{counter}'
            g.write(strin + '\n')

#print(dicts_4('text1.txt', 'text2.txt'))

def gens_3(name):
    with open(name, mode="r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if line == "":
                break
            words = line.split()
            ans = [word.strip(string.punctuation) for word in words]
            for i in range(len(ans)):
                yield ans[i]

#g = gens_3('text1.txt')
#for x in g:
#    print(x)

def gens_4(var1, var2):
    leng = min(len(var1),len(var2))
    for i in range(leng):
        yield (var1[i], var2[i])

'''
g = gens_4([10, 20, 30], "ab")
for x in g:
    print(x)
'''

def gens_5(n):
    counter = 0
    for i in range(1, n):
        for j in range(0, i):
            counter += 1
            if counter == n+1:
                return
            yield i
''' 
g = gens_5(10)
for x in g:
    print(x)
'''

def repeat(**x):
    ans = []
    for elem, count in x.items():
        for i in range (count):
            ans.append(elem)
    print(ans)

#repeat(hello=2, cat=3)

class Time:

    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def show(self):
        return(f'{self.hours}:{self.minutes}')

    def isDay(self):
        if 12 <= self.hours < 17:
            return True
        return False

    def isMorning(self):
        if 5 <= self.hours < 12:
            return True
        return False

    def isEvening(self):
        if 17 <= self.hours <= 23:
            return True
        return False

    def isNight(self):
        if 0 <= self.hours < 5:
            return True
        return False

    def say_hello(self):
        if self.isMorning():
            return 'Доброе утро'
        if self.isDay():
            return 'Добрый день'
        if self.isEvening():
            return 'Добрый вечер'
        if self.isNight:
            return "Доброй ночи"

    def add(self, add):
        added = self.minutes + add
        self.hours += added // 60
        self.minutes = added % 60
        return self.show()
'''
t1 = Time(19,53)
print (t1.say_hello())
print(t1.add(78))
'''