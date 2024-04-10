from numba import cuda, types
import numpy as np
import random
import time

start_time = time.time()  # Record start time

@cuda.jit
def sample_sort_kernel(A, S, splitters, k):
    i = cuda.grid(1)

    if i < len(A):
        # Step 1: Place each element of A into a bucket
        for j in range(len(splitters) - 1):
            if splitters[j] < A[i] <= splitters[j + 1]:
                S[i] = A[i]
                break

        # Synchronize threads before sorting the bucket
        cuda.syncthreads()

        # Step 3: Sort the bucket using insertion sort
        for j in range(1, k):
            key = S[i]
            l = i - 1
            while l >= 0 and S[l] > key:
                S[l + 1] = S[l]
                l -= 1
            S[l + 1] = key


@cuda.jit
def find_splitters_kernel(S, splitters, p, k):
    i = cuda.grid(1)

    if i < p - 1:
        splitters[i] = S[(i + 1) * k]
    elif i == p - 1:
        splitters[i] = np.inf


def sample_sort(A, k, p, threshold):
    n = len(A)

    # Step 1: Check threshold
    if n / k < threshold:
        return sorted(A)

    # Allocate memory on device
    d_A = cuda.to_device(np.array(A))
    d_S = cuda.device_array_like(d_A)
    d_splitters = cuda.device_array(p, dtype=A.dtype)

    # Step 2: Create buckets
    sample_sort_kernel[n // 256 + 1, 256](d_A, d_S, d_splitters, k)

    # Step 3: Sort buckets and concatenate
    sorted_A = d_S.copy_to_host()

    return sorted_A


# Test the implementation
A = [3, 6, 8, 10, 1, 2, 1, 5, 9, 4, 7]
k = 3  # Number of buckets
p = 2  # Number of partitions
threshold = 10  # Threshold for switching to a different sorting method

print("Original array:", A)
sorted_A = sample_sort(A, k, p, threshold)
print("Sorted array:", sorted_A)

end_time = time.time()  # Record end time
print("Time taken for sorting:", end_time - start_time, "seconds")