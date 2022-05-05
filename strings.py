def strings(s):
    counter = 0
    for i in range(0, len(s) - 1):
        if (s[i] == "A" and s[i + 1] == "B") or (s[i] == "B" and s[i + 1] == "A"):
            counter += 1
    return counter
