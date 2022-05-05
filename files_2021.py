def file_2021_1(name1):
    with open(name1, mode="r", encoding="utf-8") as f:
        lines_counter, words_counter, letters_counter = 0, 0, 0
        while True:
            line = f.readline()
            if line == "":
                break
            lines_counter += 1
            words_counter += len(line.split(' '))
            letters_counter += len(line) - line.count(' ')
        average_length = letters_counter / words_counter
        return "количество строк: " + str(lines_counter) + "\nколичество слов: " + str(
            words_counter) + "\n" + f"средняя длина слова: {average_length:.2f}"


def file_2021_2_1(name2):
    with open(name2, mode="r", encoding="utf-8") as f:
        ans = []
        all_lines = f.readlines()
        ans = [word for all_line in all_lines for word in (all_line.strip()).split(' ')]
    return ans


def file_2021_2_2(name21):
    with open(name21, mode='r', encoding="utf-8") as f:
        ans = []
        while True:
            line = f.readline()
            if line == "":
                break
            line = line.strip()
            ans.append(line.split(' '))
    return ans


def file_2021_4(namefrom, nameto):
    with open(namefrom, mode='r', encoding="utf-8") as g, open(nameto, mode="w", encoding="utf-8") as f:
        while True:
            line = g.read(1)
            if line == "":
                break
            f.write(line + line)


def file_2021_3(name3):
    with open(name3, mode="rb") as f:
        all_bytes = f.read()
        counted = {}
        for number in all_bytes:
            if number in counted:
                counted[number] += 1
            else:
                counted[number] = 1
        return counted[max(counted)]

