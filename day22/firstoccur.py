def strStr(haystack: str, needle: str) -> int:
    for i in range(len(haystack) - len(needle) + 1):
        print(f"now: {haystack[i]} ")
        flag = True
        for s in range(len(needle)):
            print(f"with: {needle[s]} ")
            if needle[s] != haystack[i + s]:
                flag = False
                break

        if flag:
            return i

    return -1

