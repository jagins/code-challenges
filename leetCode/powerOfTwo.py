def isPowerOfTwo(n: int) -> bool:
    exponent = 0
    sum = 0

    while n > sum:
        if 2 ** exponent == n:
            return True
        else:
            sum = 2 ** exponent
            exponent += 1
    return False