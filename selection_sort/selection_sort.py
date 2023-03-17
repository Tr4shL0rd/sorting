"""Selection sort"""
from typing import List
#pylint: disable=redefined-builtin,consider-using-enumerate
def selection_sort(lst:list) -> List:
    """Selection sort algorithm"""
    for i in range(len(lst)):
        min = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min]:
                min = j
        if min != i:
            lst[i], lst[min] = lst[min], lst[i]
    return lst
