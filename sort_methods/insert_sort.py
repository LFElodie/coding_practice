#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import time_it, assert_sort


@assert_sort
@time_it
def insert_sort(sort_list: list) -> list:
    """
    插入排序
    :param sort_list:
    :return: sorted list
    """
    for i in range(1, len(sort_list)):
        for j in range(i, 0, -1):
            if sort_list[j] < sort_list[j-1]:
                sort_list[j], sort_list[j-1] = sort_list[j-1], sort_list[j]
    return sort_list


if __name__ == '__main__':
    raw_list = [15, 489, 45, 4, 28, 16, 73, 45, 85, 96, 26, 87, 26, 51, 32] * 100
    print(insert_sort(raw_list))
