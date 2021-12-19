# 3. Longest Substring Without Repeating Character
# Given a string s, find the length of the longest
# substring without repeating characters.

# Example 1
ie_i1 = "abcabcbb"
ie_s1 = 3

# Example 2
ie_i2 = "bbbbb"
ie_s2 = 1

# Example 3
ie_i3 = "pwwkew"
ie_s3 = 3

# Example 4
ie_i4 = ""
ie_s4 = 0

# Example 5
ie_i5 = "asdfghjklqwerty"
ie_s5 = 15

def solution_checker(solutions, outputs):
    for i in range(len(solutions)):
        if outputs[i] != solutions[i]: return False
    return True

def lengthOfLongestSubstring(s: str) -> int:
    if not s: return 0
    if len(set(s)) == 1: return 1
    len_s = len(s)
    if len(set(s)) == len_s: return len_s
    max_sub = 1
    view = ""

    for char in s:
        if char in view:
            view = view[view.index(char)+1:]
        view += char
        max_sub = max(max_sub, len(view))

    return max_sub

inputs = [ie_i1, ie_i2, ie_i3, ie_i4, ie_i5]
solutions = [ie_s1, ie_s2, ie_s3, ie_s4, ie_s5]
outputs = [lengthOfLongestSubstring(i) for i in inputs]
print(f"This code works!\t{solution_checker(solutions, outputs)}")
