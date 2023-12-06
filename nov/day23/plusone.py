def plusOne(digits):
    digits[-1] += 1
    if digits[-1] == 10:
        digits[-1] = 0
        i = len(digits) - 2

        if i == -1:
            return [1, 0]

        while i > 0 and digits[i] == 9:
            digits[i] = 0
            i -= 1

        digits[i] += 1
        if digits[i] == 10:
            digits[i] = 0
            digits.insert(0, 1)

    return digits


digits = [1, 9, 9]
print(f"{digits} + 1 = {plusOne(digits)}")
