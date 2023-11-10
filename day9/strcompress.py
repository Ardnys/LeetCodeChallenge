def compress(chars) -> int:
    for char in chars:
        if char in map:
            map[char] += 1
        else:
            map[char] = 1

    compressed_str = ""
    for key, val in map.items():
        compressed_str += str(key)
        compressed_str += str(val)


    return len(compressed_str)


chars = ["a", "a", "b", "b", "c", "c", "c"]
l = compress(chars)
