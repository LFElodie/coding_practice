#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for index, num in enumerate(nums[:-2]):
            if num > 0:
                break
            if index > 0 and nums[index-1] == num:
                continue
            i = index + 1
            j = len(nums) - 1
            while i < j:
                if num + nums[i] + nums[j] == 0:
                    result = [num, nums[i], nums[j]]
                    if result not in results:
                        results.append(result)
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                elif num + nums[i] > 0:
                    break
                elif num + nums[i] + nums[j] < 0:
                    i += 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                else:
                    j -= 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
        return results


if __name__ == '__main__':
    solution = Solution()
    result = solution.threeSum([-1, 0, 1, 2, -1, -4])
    print(result)
