def longestCommonPrefix(strs) -> str:
    smol = min(strs)

    common = 0
    for s in range(len(smol)):
        for str in strs:
            if str[s] != smol[s]:
                return smol[:common]

        common += 1

    return smol[:common]
