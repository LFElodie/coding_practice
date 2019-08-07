#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

from sort_methods.bubble_sort import bubble_sort
from sort_methods.insert_sort import insert_sort
from sort_methods.merge_sort import merge_sort
from sort_methods.quick_sort import quick_sort

import sys
# sys.setrecursionlimit(100000)

if __name__ == '__main__':
    raw_list = list(np.random.rand(10000))
    print(len(raw_list))
    bubble_sort(raw_list)
    insert_sort(raw_list)
    merge_sort(raw_list)
    quick_sort(raw_list)

