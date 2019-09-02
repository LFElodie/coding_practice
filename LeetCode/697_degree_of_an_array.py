#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left = {}
        right = {}
        count = {}
        for index, num in enumerate(nums):
            if num not in left:
                left[num] = index
            right[num] = index
            count[num] = count.get(num, 0) + 1
        degree = max(count.values())
        res = len(nums)
        for num in right:
            if degree == count[num]:
                res = min(res, right[num] - left[num] + 1)
        return res


if __name__ == '__main__':
    nums = [1, 2, 2, 3, 1]
    solution = Solution()
    result = solution.findShortestSubArray(nums)
    print(result)
