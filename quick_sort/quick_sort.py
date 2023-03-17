"""Quick sort"""
from typing import List
def quick_sort(lst:list, left=0, right = None) -> List:
    """Quick sort algorithm"""
    if right is None:
        right = len(lst) -1
    pivot_point = partition(lst,left,right)
    lst = quick_sort(lst,left,pivot_point-1)
    lst = quick_sort(lst,pivot_point+1,right)

    return lst

def partition(lst:list,left,right):
    pivot_point = lst[right]
    partition_index = left

    for i in range(left,right):
        if lst[i] < pivot_point:
            swap(lst,i,partition_index)
            partition_index+=1

    return swap(lst,right,partition_index)

def swap(lst:list, first_index, second_index):
    temp = lst[first_index]
    lst[first_index] = lst[second_index]
    lst[second_index] = temp
    return swap

