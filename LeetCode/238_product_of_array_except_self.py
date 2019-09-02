#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import List


class Solution:
    # 排除条件：不许使用除法
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def product_all_nums(nums: List[int]):
            product = 1
            for num in nums:
                product *= num
            return product
        product_all = product_all_nums(nums)
        if product_all != 0:
            result = [product_all // num for num in nums]
            return result
        else:
            result = [0] * len(nums)
            product_left = product_all_nums(nums[:nums.index(0)])
            product_right = product_all_nums(nums[nums.index(0)+1:])
            result[nums.index(0)] = product_left * product_right
            return result


class Solution2:
    # 左积和右积
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_left = [1] * len(nums)
        for index in range(len(nums) - 1):
            product_left[index + 1] = product_left[index] * nums[index]
        product_right = [1] * len(nums)
        for index in range(len(nums) - 1, 0, -1):
            product_right[index - 1] = product_right[index] * nums[index]
        result = [product_left[index] * product_right[index] for index in range(len(product_left))]
        return result


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    solution = Solution()
    result = solution.productExceptSelf(nums)
    print(result)

    nums = [1, 2, 3, 4]
    solution = Solution2()
    result = solution.productExceptSelf(nums)
    print(result)