def lengthOfLastWord(s: str) -> int:
    last = len(s) - 1
    while last > 0:
        if s[last] != " ":
            break
        last -= 1
    l = last
    while last >= 0:
        if s[last] == " ":
            return l - last
        last -= 1
    return l - last

