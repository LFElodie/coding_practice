#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time


def time_it(func):
    """
    用于打印执行用时的装饰器，若存在递归，只打印最外层调用的时间
    :param func:
    :return:
    """
    cur_evaluating = set()

    def wrap(*args, **kwargs):
        if func not in cur_evaluating:
            cur_evaluating.add(func)
            start = time.time()
            result = func(*args, **kwargs)
            print('{}: {:.10f}'.format(func.__name__, time.time() - start))
            cur_evaluating.remove(func)
        else:
            result = func(*args, **kwargs)
        return result
    return wrap
