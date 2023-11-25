def isPalindrome(s: str) -> bool:
    i = 0
    j = len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
            continue
        elif not s[j].isalnum():
            j -= 1
            continue
        elif s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1

    return True

    # a = []
    # for c in s:
    #     if c.isalnum():
    #         a.append(c.lower())
    #
    # i = 0
    # j = len(a) - 1
    #
    # while i < j:
    #     if a[i] != a[j]:
    #         return False
    #     i += 1
    #     j -= 1
    #
    # return True
    #


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
