#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import time_it, assert_sort


@assert_sort
@time_it
def radix_sort(sort_list: list) -> list:
    def counting_sort(sort_list: list, exp: int) -> list:
        k = 10
        counting_list = [0] * k
        result = [0] * len(sort_list)
        for num in sort_list:
            counting_list[(num // exp) % 10] += 1
        for i in range(1, k):
            counting_list[i] += counting_list[i - 1]
        for j in range(len(sort_list) - 1, -1, -1):
            result[counting_list[(sort_list[j] // exp) % 10] - 1] = sort_list[j]
            counting_list[(sort_list[j] // exp) % 10] -= 1
        return result
    max_num = max(sort_list)
    exp = 1
    while max_num//exp > 0:
        sort_list = counting_sort(sort_list, exp)
        exp *= 10
    return sort_list


if __name__ == '__main__':
    raw_list = [15, 489, 45, 4, 28, 16, 73, 45, 85, 96, 26, 87, 26, 51, 32] * 100
    print(radix_sort(raw_list))
