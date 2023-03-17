"""ddwa"""
import time
import random
from bubble_sort.bubble_sort import bubble_sort
from insertion_sort.insertion_sort import insertion_sort
from selection_sort.selection_sort import selection_sort
import sys

def main(data):
    data_sample = ''.join(str(data[:10])).replace("]",", ...]")
    print(f"dataset sample: {data_sample}")
    print(f"dataset size: {len(data)}")

    # bubble
    print("Starting bubble_sort", end="\r")
    bubble_start_time = time.time()
    bubble_sort(data)
    bubble_stop_time = time.time() - bubble_start_time

    # insertion
    print("Starting insertion_sort", end="\r")
    insertion_start_time = time.time()
    insertion_sort(data)
    insertion_stop_time = time.time() - insertion_start_time



    # selection
    print("Starting selection_sort", end="\r")
    selection_start_time = time.time()
    selection_sort(data)
    selection_stop_time = time.time() - selection_start_time
    print(" " * 24)


    # print(f"{bubble_stop_time = }")
    # print(f"{insertion_stop_time = }")
    # print(f"{selection_stop_time = }")
    speed_times = [bubble_stop_time,insertion_stop_time,selection_stop_time]
    speeds = {
        str(bubble_stop_time): "bubble_sort",
        str(insertion_stop_time): "insertion_sort",
        str(selection_stop_time): "selection_sort",
    }
    fastest_algorithm = speeds[str(sorted(speed_times)[0])]
    #move(0,0)

    print("\nfastest to slowest")
    for speed in sorted(speed_times):
        print(f"{speeds[str(speed)]}: {speed}")

    print(f"fastest is {fastest_algorithm}")
    print("\n" * 3)

try:
    dataset_size = int(sys.argv[1])
    if dataset_size < 700:
        print("[WARNING] dataset sizes under 700 might result in the numbers being shown in scientific notaion")
except IndexError:
    dataset_size = 10000
big_data = random.sample(range(0,dataset_size*2), dataset_size)
main(big_data)
