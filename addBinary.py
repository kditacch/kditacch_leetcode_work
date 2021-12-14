# 67. Add Binary
# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
ie_a_1 = "11"
ie_b_1 = "1"
ie_s_1 = "100"

# Example 2:
ie_a_2 = "1010"
ie_b_2 = "1011"
ie_s_2 = "10101"

def solution_checker(ie_s, op_s) -> bool:
    for i in range(len(ie_s)):
        if ie_s[i] != op_s[i]:
            return False
    return True

def addBinary(a: str, b: str) -> str:
    a = a[::-1]
    b = b[::-1]
    x, y, z, r = 0, 0, 0, 0
    suma = ""
    i = 0
    len_a = len(a)
    len_b = len(b)
    maxab = max(len_a, len_b)
    while r or i < maxab:
        x = 0 if i >= len_a else int(a[i])
        y = 0 if i >= len_b else int(b[i])
        z = ((x + y)%2 + r)%2
        r = 1 if x + y + r > 1 else 0
        suma = f"{z}{suma}"
        i += 1
    if len(suma) > 1:
        while not int(suma[0]):
            suma = suma[1::]
    return suma


input1 = [ie_a_1, ie_a_2]
input2 = [ie_b_1, ie_b_2]
solutions = [ie_s_1, ie_s_2]
outputs = [addBinary(input1[i], input2[i]) for i in range(2)]
print(f"This code works!\t{solution_checker(solutions, outputs)}")
