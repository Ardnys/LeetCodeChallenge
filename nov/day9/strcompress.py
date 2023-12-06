def compress(chars) -> int:
    l = []
    count = 1
    for i in range(1, len(chars)):
        if chars[i] == chars[i-1]:
            count += 1
        else:
            l.append((chars[i-1], count))
            count = 1
    l.append((chars[-1], count))

    uh = 0
    for key, val in l:
        chars[uh] = key
        uh += 1
        if val > 1:
            for digit in str(val):
                chars[uh] = str(digit)
                uh += 1

    return uh


chars = ["a", "a", "b", "b", "c", "c", "c"]
l = compress(chars)
print(l)
