
def maxVowels(s: str, k: int) -> int:
    uh = 0
    vowels = set('aeiou')

    for i in range(k):
        if s[i] in vowels:
            uh += 1

    m = uh
    for i in range(len(s)):
        if s[i-k] in vowels:
            uh -= 1
        if s[i] in vowels:
            uh += 1
        m = max(m, uh)

    return m
