#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    # 使用hash表记录 dict(value) = index
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = {}
        for index, num in enumerate(nums):
            if target - num in index_dict:
                return [index_dict[target - num], index]
            else:
                index_dict[num] = index


if __name__ == '__main__':
    solution = Solution()
    result = solution.twoSum([2, 7, 11, 15], 9)
    print(result)
