#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import time_it


@time_it
def heap_sort(sort_list: list) -> list:
    def parent(index):
        return (index + 1) // 2 - 1

    def left(index):
        return 2 * index + 1

    def right(index):
        return 2 * index + 2

    def max_heapify(nums: list, index, heap_size_):
        l = left(index)
        r = right(index)
        if l < heap_size_ and nums[l] > nums[index]:
            largest = l
        else:
            largest = index
        if r < heap_size_ and nums[r] > nums[largest]:
            largest = r
        if largest != index:
            nums[index], nums[largest] = nums[largest], nums[index]
            max_heapify(nums, largest, heap_size_)

    def build_max_heap(nums, heap_size_):
        for i in range(len(nums)//2-1, -1, -1):
            max_heapify(nums, i, heap_size_)
    heap_size = len(sort_list)
    build_max_heap(sort_list, heap_size)
    for i in range(len(sort_list)-1, 1, -1):
        sort_list[0], sort_list[i] = sort_list[i], sort_list[0]
        heap_size -= 1
        max_heapify(sort_list, 0, heap_size)
    return sort_list


if __name__ == '__main__':
    raw_list = [15, 489, 45, 4, 28, 16, 73, 45, 85, 96, 26, 87, 26, 51, 32] * 100
    print(heap_sort(raw_list))
