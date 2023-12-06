def reverseWords(s: str) -> str:
    s = s.split()
    l = len(s) - 1

    for i in range(l):
        if i >= l:
            break
        if s[i] == "" or s[i] == " ":
            continue
        while s[l] == "" or s[l] == " ":
            l -= 1
        hold = s[i]
        s[i] = s[l]
        s[l] = hold
        l -= 1

    return " ".join(s)
