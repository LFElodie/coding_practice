#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    # 暴力解法：超时
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        while k > 0:
            for i in range(len(nums)-1, 0, -1):
                nums[i], nums[i-1] = nums[i-1], nums[i]
            k -= 1
        print(nums)


class Solution2:
    # 使用额外的空间，python中使用切片合并
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        print(nums)


class Solution3:
    # 环装替换
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        count = 0
        start = 0
        while count < len(nums):
            current = start
            while True:
                next = (current + k) % len(nums)
                nums[start], nums[next] = nums[next], nums[start]
                current = next
                count += 1
                if current == start:
                    start += 1
                    break
        print(nums)


class Solution4:
    # 使用反转
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums: List[int], start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        k %= len(nums)
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)
        print(nums)


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    solution = Solution()
    solution.rotate(nums, k)

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    solution = Solution2()
    solution.rotate(nums, k)

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    solution = Solution3()
    solution.rotate(nums, k)

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    solution = Solution4()
    solution.rotate(nums, k)

