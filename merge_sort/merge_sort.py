"""Merge sort"""
from typing import List
#pylint: disable=redefined-builtin,consider-using-enumerate,invalid-name
def splice(lst:list, idx) -> List:
    """splice"""
    return lst[0:idx:-1]

def merge_sort(lst:list) -> List:
    """Merge sort algorithm"""
    MID = len(lst) // 2
    if len(lst) < 2:
        return lst
    LEFT = splice(lst, MID)

    return merge(merge_sort(LEFT), merge_sort(lst))

def merge(left:list,right:list):
    """MERGE"""
    lst = []
    while len(left) and len(right):
        if left[0] < right[0]:
            lst.append(left.pop(0))
        else:
            lst.append(right.pop(0))

    return zip(lst,left,right)
