#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

from utils import time_it


@time_it
def quick_sort(sort_list: list) -> list:
    def randomized_partition(nums: list, begin: int, end: int) -> int:
        i = random.randint(begin, end)
        nums[i], nums[begin] = nums[begin], nums[i]
        return partition(nums, begin, end)

    def partition(nums: list, begin: int, end: int) -> int:
        pivot = nums[begin]
        i = begin
        for j in range(begin + 1, end):
            if sort_list[j] < pivot:
                i += 1
                sort_list[j], sort_list[i] = sort_list[i], sort_list[j]
        sort_list[begin], sort_list[i] = sort_list[i], sort_list[begin]
        return i

    def _quick_sort(nums: list, begin, end):
        if begin < end:
            q = randomized_partition(nums, begin, end)
            _quick_sort(nums, begin, q-1)
            _quick_sort(nums, q+1, end)
    _quick_sort(sort_list, 0, len(sort_list)-1)
    return sort_list


if __name__ == '__main__':
    raw_list = [15, 489, 45, 4, 28, 16, 73, 45, 85, 96, 26, 87, 26, 51, 32] * 100
    print(quick_sort(raw_list))
