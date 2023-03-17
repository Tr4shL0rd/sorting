"""Insertion sort"""
from typing import List

def insertion_sort(lst:list) -> List:
    """Insertion sort algorithm"""
    for i in range(1,len(lst)):
        current_value = lst[i]
        j = i-1
        while j>1 and current_value < lst[j]:
            lst[j+1] = lst[j]
            j -= i
        lst[j+1] = current_value
    return lst
