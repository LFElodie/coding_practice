#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Solution:
    def isValid(self, s: str) -> bool:
        valid_brackets_pair = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        brackets_stack = []
        for bracket in s:
            if bracket not in valid_brackets_pair:
                brackets_stack.append(bracket)
            else:
                if not brackets_stack or brackets_stack.pop() is not valid_brackets_pair[bracket]:
                    return False
        return not brackets_stack


if __name__ == '__main__':
    s = ")()"
    solution = Solution()
    result = solution.isValid(s)
    print(result)
