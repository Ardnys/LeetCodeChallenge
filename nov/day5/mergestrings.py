def mergeAlternately(word1: str, word2: str) -> str:
    l1, l2 = len(word1), len(word2)
    new_str = []
    ctr = 0
    for i in range(min(l1, l2) * 2):
        if i % 2 == 0:
            new_str.append(word1[ctr])
        else:
            new_str.append(word2[ctr])
            ctr += 1

    if l1 > l2:
        new_str += list(word1[l2:])
    elif l2 > l1:
        new_str += list(word2[l1:])

    return "".join(new_str)
