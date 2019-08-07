#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils import time_it


@time_it
def bubble_sort(sort_list: list) -> list:
    """
    冒泡排序
    两层循环：
    当某轮循环中没有发生交换证明已经排序完毕，停止循环
    :param sort_list:
    :return: sorted list
    """
    for i in range(len(sort_list)):
        change = False
        for j in range(len(sort_list) - 1 - i):
            if sort_list[j] > sort_list[j + 1]:
                change = True
                sort_list[j + 1], sort_list[j] = sort_list[j], sort_list[j + 1]
        if not change:
            break
    return sort_list


if __name__ == '__main__':
    raw_list = [15, 489, 45, 4, 28, 16, 73, 45, 85, 96, 26, 87, 26, 51, 32] * 20
    print(bubble_sort(raw_list))
