# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their nodes
# contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def listToListNode(li:list[int]) -> ListNode:
    ret = None
    ptr = None
    for l in li:
        if ptr:
            ptr.next = ListNode(val=l)
            ptr = ptr.next
        else:
            ptr = ListNode(val=l)
            ret = ptr
    return ret

# Example 1
ie_l1_1 = listToListNode([2,4,3])
ie_l2_1 = listToListNode([5,6,4])
ie_s1 = listToListNode([7,0,8])

# Example 2
ie_l1_2 = listToListNode([0])
ie_l2_2 = listToListNode([0])
ie_s2 = listToListNode([0])

# Example 3
ie_l1_3 = listToListNode([9,9,9,9,9,9,9])
ie_l2_3 = listToListNode([9,9,9,9])
ie_s3 = listToListNode([8,9,9,9,0,0,0,1])

def solution_checker(solutions, outputs):
    for i in range(len(solutions)):
        s_checker = solutions[i]
        o_checker = outputs[i]
        while s_checker:
            if s_checker.val != o_checker.val: return False
            s_checker = s_checker.next
            o_checker = o_checker.next
    return True

def addTwoNumbers(l1:ListNode, l2:ListNode) -> ListNode:
    head_ptr = None
    digit = None
    carry = 0
    while l1 or l2 or carry:
        val = carry
        if l1:
            val += l1.val
            l1 = l1.next
        if l2:
            val += l2.val
            l2 = l2.next
        carry = val // 10
        if digit == None:
            digit = ListNode(val=val%10)
            head_ptr = digit
        else:
            digit.next = ListNode(val=val%10)
            digit = digit.next
    return head_ptr

inputs1 = [ie_l1_1, ie_l1_2, ie_l1_3]
inputs2 = [ie_l2_1, ie_l2_2, ie_l2_3]
solutions = [ie_s1, ie_s2, ie_s3]
outputs = [addTwoNumbers(inputs1[i], inputs2[i]) for i in range(len(inputs1))]
print(f"This code works!\t{solution_checker(solutions, outputs)}")
