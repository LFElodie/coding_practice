#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import time_it


@time_it
def merge_sort(sort_list: list) -> list:
    """
    归并排序
    1、divide: 拆分为两部分
    2、conquer: 对每一部分进行排序，调用自己
    3、combine: 将排序好的两部分，merge到一起
    :param sort_list:
    :return: sorted list
    """
    if len(sort_list) < 2:
        return sort_list
    left_list = sort_list[:len(sort_list)//2]
    right_list = sort_list[len(sort_list)//2:]
    sorted_list = []
    sorted_left = merge_sort(left_list)
    sorted_right = merge_sort(right_list)
    while len(sorted_left) and len(sorted_right):
        if sorted_left[0] <= sorted_right[0]:
            sorted_list.append(sorted_left.pop(0))
        else:
            sorted_list.append(sorted_right.pop(0))
    if not len(sorted_left):
        sorted_list.extend(sorted_right)
    if not len(sorted_right):
        sorted_list.extend(sorted_left)
    return sorted_list


if __name__ == '__main__':
    raw_list = [15, 489, 45, 4, 28, 16, 73, 45, 85, 96, 26, 87, 26, 51, 32] * 100
    print(merge_sort(raw_list))
