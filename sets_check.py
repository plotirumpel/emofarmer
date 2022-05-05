import string

def correct_words(name):
    with open(name, mode="r", encoding="utf-8") as f:
        correct_words_set = set(f.read().split())
    return correct_words_set

def wrong_words(name_dict, name_text, name_write):
    with open(name_dict, mode='r', encoding = "utf-8") as f_dict, open(name_write, mode="w", encoding="utf-8") as f_write, open(name_text, mode='r', encoding = "utf-8") as f_text:
        correct_words_set = set(f_dict.read().split())
        text_list = [i.strip(string.punctuation) for i in f_text.read().split()]
        for i in text_list:
            if not i.lower() in correct_words_set:
                f_write.write(i+'\n')
                print(i)

def delete_letter(word):
    ans = (set())
    for letter in word:
        word_new = word.replace(letter, '',1)
        ans.add(word_new)
    return ans

def add_letter(word):
    ans = (set())
    for i in range(len(word)):
        for alpha in string.ascii_lowercase:
            word_new = f'{word[:i]}{alpha}{word[i:]}'
            ans.add(word_new)
    return ans

def replace_letter(word):
    ans = (set())
    for i in range(0, len(word)-1):
        word_new = f'{word[:i]}{word[i+1]}{word[i]}{word[i+2:]}'
        ans.add(word_new)
    return ans

def mnvo_slov (word, name_dict):
    with open(name_dict, mode='r', encoding="utf-8") as f_dict:
        dictionary = f_dict.read().split()
        dictionary = (set(dictionary))
    new_words = (set())
    new_words = new_words|delete_letter(word)|add_letter(word)|replace_letter(word)
    return new_words & dictionary

def proverka (name_dict, name_text, name_write):
    with open(name_dict, mode='r', encoding = "utf-8") as f_dict, open(name_write, mode="w", encoding="utf-8") as f_write, open(name_text, mode='r', encoding = "utf-8") as f_text:
        correct_words_set = set(f_dict.read().split())
        text_list = [i.strip(string.punctuation) for i in f_text.read().split()]
        for i in text_list:
            if not i.lower() in correct_words_set:
                f_write.write(f'! {i} {mnvo_slov(i,name_dict)}\n')
                print(f'! {i} {mnvo_slov(i,name_dict)}')
            else:
                f_write.write(i + '\n')
                print(i)

#proverka('words_alpha.txt','text1.txt','text2.txt')
