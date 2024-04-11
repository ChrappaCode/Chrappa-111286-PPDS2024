import numpy as np
import time
from numba import cuda, types

BLOCK_SIZE = 128

@cuda.jit
def insertion_sort(arr):
    """
    Perform insertion sort on the given array using CUDA.
    """
    tid = cuda.threadIdx.x + cuda.blockIdx.x * cuda.blockDim.x
    stride = cuda.blockDim.x * cuda.gridDim.x

    for i in range(tid + 1, arr.shape[0], stride):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def sample_sort(arr):
    num_subsets = len(arr) // BLOCK_SIZE + 1
    sorted_subsets = np.empty_like(arr)

    for i in range(num_subsets):
        subset = arr[i * BLOCK_SIZE: (i + 1) * BLOCK_SIZE]
        insertion_sort[1, BLOCK_SIZE](subset)
        sorted_subsets[i * BLOCK_SIZE: (i + 1) * BLOCK_SIZE] = subset

    #cuda.synchronize()
    final_sorted_array = np.sort(sorted_subsets)

    return final_sorted_array

arr = np.random.randint(0, 10000, size=10000)
print("Original array: ", arr)
start_time = time.time()
sorted_arr = sample_sort(arr)
end_time = time.time()
print("Time taken for sorting:", end_time - start_time, "seconds")
print("Sorted array:", sorted_arr)