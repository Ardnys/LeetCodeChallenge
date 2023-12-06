def reverseVowels(s: str) -> str:
    eh = list(s)
    l = len(s) - 1
    i = 0
    them = "aeiouAEIOU"

    for i in range(l):
        if eh[i] in them:
            while l > i and l > 0:
                if eh[l] in them:
                    hold = eh[i]
                    eh[i] = eh[l]
                    eh[l] = hold
                    l -= 1
                    break
                l -= 1

    return "".join(eh)
