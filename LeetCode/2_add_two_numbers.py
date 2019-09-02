#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        curr = dummy_head
        carry = 0
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            num_sum = x + y + carry
            curr.next = ListNode(num_sum % 10)
            carry = num_sum // 10
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            curr.next = ListNode(carry)
        return dummy_head.next


if __name__ == '__main__':
    solution = Solution()
    l1 = ListNode(3)
    l1.next = ListNode(4)
    l1.next.next = ListNode(2)
    l2 = ListNode(4)
    l2.next = ListNode(6)
    l2.next.next = ListNode(5)
    head = solution.addTwoNumbers(l1, l2)
    while head:
        print(head.val)
        head = head.next
