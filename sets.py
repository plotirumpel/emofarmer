import string


def sets_1(strin):
    return {i for i in strin}


def sets_2(string, sett):
    ans = [i for i in string if not (i in sett)]
    return ('').join(ans)


def sets_3(strin):
    predans = strin.split()
    ans = [i.strip(string.punctuation) for i in predans]
    return ans


def sets_4_1(strin1, strin2):
    words1 = sets_3(strin1)
    words2 = sets_3(strin2)
    set_ans = set(words1) & set(words2)
    return set_ans


def sets_4_2(strin1, strin2):
    words1, words2 = sets_3(strin1), sets_3(strin2)
    words1, words2 = [word.lower() for word in words1], [word.lower() for word in words2]
    set_ans = set(set(words1) & set(words2))
    return set_ans
