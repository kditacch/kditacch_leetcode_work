# 69. Sqrt(x)
# Given a non-negative integer x, compute and return the square root of x.
# Since the return type is an integer, the decimal digits are truncated,
# and only the integer part of the result is returned.
# Note: You are not allowed to use any built-in exponent function or operator,
# such as pow(x, 0.5) or x ** 0.5.

# Example 1:
ie_x_1 = 4
ie_s_1 = 2

# Example 2:
ie_x_2 = 8
ie_s_2 = 2

# Example 2:
ie_x_3 = 108
ie_s_3 = 10

# Example 1:
ie_x_4 = 273529
ie_s_4 = 523

# Example 2:
ie_x_5 = 1234567890
ie_s_5 = 35136

def solution_checker(ie_s, op_s) -> bool:
    for i in range(len(ie_s)):
        if ie_s[i] != op_s[i]:
            return False
    return True


def getSmallSqrt(smallnum: int) -> int:
    lo = 0
    hi = int(smallnum/4)
    while lo*lo <= smallnum:
        if smallnum > 16:
            if hi*hi <= smallnum:
                return hi
            mid = int((hi-lo)/2)
            midsqrd = mid*mid
            if midsqrd == smallnum:
                return mid
            elif smallnum - midsqrd < 0:
                hi = mid
            else:
                lo = mid
        lo += 1
        hi -= 1
    return lo-1

def getNextActor(curdigits: int, curchunk: int) -> (int, int):
    firstDigits = curdigits*2
    lastDigits = 1
    while int(f"{firstDigits}{lastDigits}")*lastDigits <= curchunk:
        lastDigits += 1
    lastDigits -= 1
    return int(f"{firstDigits}{lastDigits}")*lastDigits, lastDigits

def mySqrt(x: int) -> int:
    xstr = str(x)
    xstrlen = len(str(x))
    if xstrlen < 8:
        # intuitive averages algorithm
        return getSmallSqrt(x)
    else:
        # long division like algorithm
        chunk = int(xstr[0] if xstrlen%2 == 1 else xstr[:2])
        i = len(str(chunk))
        actor = getSmallSqrt(chunk)
        digitbuilder = str(actor)
        chunk = int(f"{chunk - (actor*actor)}{xstr[i:i+2]}")
        i += 2
        while i <= xstrlen:
            actor, digit = getNextActor(int(digitbuilder), chunk)
            digitbuilder = f"{digitbuilder}{digit}"
            chunk = int(f"{chunk-actor}{xstr[i:i+2]}")
            i += 2
        return int(digitbuilder)

input = [ie_x_1, ie_x_2, ie_x_3, ie_x_4, ie_x_5]
solutions = [ie_s_1, ie_s_2, ie_s_3, ie_s_4, ie_s_5]
outputs = [mySqrt(input[i]) for i in range(len(input))]
print(f"This code works!\t{solution_checker(solutions, outputs)}")
