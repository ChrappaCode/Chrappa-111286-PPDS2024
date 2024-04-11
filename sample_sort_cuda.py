from numba import cuda
import numpy as np
import time


@cuda.jit
def bucket_assignment_kernel(A, S, splitters):
    tid = cuda.threadIdx.x + cuda.blockIdx.x * cuda.blockDim.x
    if tid < len(A):
        for j in range(len(splitters) - 1):
            if splitters[j] < A[tid] <= splitters[j + 1]:
                S[tid] = A[tid]
                break


@cuda.jit
def insertion_sort_kernel(S):
    tid = cuda.threadIdx.x + cuda.blockIdx.x * cuda.blockDim.x
    # Insertion sort
    for j in range(1, len(S)):
        key = S[j]
        i = j - 1
        while i >= 0 and S[i] > key:
            S[i + 1] = S[i]
            i -= 1
        S[i + 1] = key


@cuda.jit
def find_splitters_kernel(S, splitters, k):
    tid = cuda.threadIdx.x + cuda.blockIdx.x * cuda.blockDim.x
    if tid < len(splitters) - 1:
        splitters[tid] = S[(tid + 1) * k]
    elif tid == len(splitters) - 1:
        splitters[tid] = np.inf


def sample_sort(A, k, p, threshold):
    n = len(A)

    if n / k < threshold:
        return sorted(A)

    d_A = cuda.to_device(np.array(A))
    d_S = cuda.device_array_like(d_A)
    d_splitters = cuda.device_array(p, dtype=A.dtype)

    grid_size = (n + 255) // 256
    block_size = 256

    bucket_assignment_kernel[grid_size, block_size](d_A, d_S, d_splitters)
    cuda.synchronize()

    insertion_sort_kernel[grid_size, block_size](d_S)
    cuda.synchronize()

    find_splitters_kernel[1, p](d_S, d_splitters, k)
    cuda.synchronize()

    sorted_A = d_S.copy_to_host()

    return sorted_A


# Test the implementation
A = np.random.randint(0, 10000, size=100000000)
k = 2
p = 3  # Changed to 4 partitions
threshold = 100000000

print("Original array:", A)
start_time = time.time()
sorted_A = sample_sort(A, k, p, threshold)
end_time = time.time()
print("Time taken for sorting:", end_time - start_time, "seconds")
print("Sorted array:", sorted_A)

