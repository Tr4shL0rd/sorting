"""Bubble Sort"""
from typing import List
def bubble_sort(lst:list) -> List:
    """Bubble sort algorithm"""
    for i in range(len(lst)):
        for j in range(len(lst) - i -1):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
    return lst
