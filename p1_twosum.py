# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# You can return the answer in any order.

# Example 1
ie_n_1 = [2,7,11,15]
ie_t_1 = 9
ie_s_1 = [[0,1], [1,0]]

# Example 2
ie_n_2 = [3,2,4]
ie_t_2 = 6
ie_s_2 = [[1,2], [2,1]]

# Example 3
ie_n_3 = [3,3]
ie_t_3 = 6
ie_s_3 = [[0,1], [1,0]]

# Example 4
ie_n_4 = [1,1,2,3,5,8]
ie_t_4 = 10
ie_s_4 = [[2,5], [5,2]]

def solution_checker(solutions, outputs) -> bool:
    for i in range(len(solutions)):
        if not (outputs[i] in solutions[i]):
            return False
    return True

def twoSum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i in range(len(nums)):
        if target-nums[i] in seen.keys():
            return [seen[target-nums[i]], i]
        else:
            seen[nums[i]] = i
    return []

inputs1 = [ie_n_1, ie_n_2, ie_n_3, ie_n_4]
inputs2 = [ie_t_1, ie_t_2, ie_t_3, ie_t_4]
solutions = [ie_s_1, ie_s_2, ie_s_3, ie_s_4]
outputs = [twoSum(inputs1[i], inputs2[i]) for i in range(len(inputs1))]
print(f"This code works!\t{solution_checker(solutions, outputs)}")
