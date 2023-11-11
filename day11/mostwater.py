def maxArea(height) -> int:
    """
    YOOO I ONE SHOT THE THING LOL 95% btw
    two pointers, one at start one at end
    max = 0
    while start < end:
        if height[end] > height[start]
            vol = height[start] * end - start
            if vol > max:
                max = vol
            start += 1
        else:
            vol = height[end] * end - start
            if vol > max:
                max = vol
            end -= 1

    return max

    """
    m, start, end = 0, 0, len(height)-1

    while start < end:
        if height[end] > height[start]:
            vol = height[start] * (end - start)
            if vol > m:
                m = vol
            start += 1

        else:
            vol = height[end] * (end - start)
            if vol > m:
                m = vol
            end -= 1

    return m
