def isSubsequence(s: str, t: str) -> bool:
    if len(s) > len(t):
        return False
    elif len(s) == len(t):
        return s == t

    last_found_idx = 0
    yes = False
    for subchar in s:
        for char in range(last_found_idx, len(t)):
            if t[char] == subchar:
                last_found_idx = char+1
                yes = True
                break

        if not yes:
            return False
        else:
            yes = False

    return True


s = "abc"
t = 'ahkxcw'
print(isSubsequence(s, t))
