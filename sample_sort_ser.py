import random
import time
import numpy as np

def sample_sort(A, k, p, threshold):
    n = len(A)

    if n / k < threshold:
        A.sort()
        return A

    if k >= n:
        S = sorted(A)
    else:
        S = [random.sample(A, k) for _ in range(p)]  # Randomly select k samples for each set
        S = [item for sublist in S for item in sublist]  # Flatten the list of samples
        S.sort()  # Sort the samples

    # Generate splitters
    splitters = [float('-inf')] + [S[i * k] for i in range(1, p)] + [float('inf')]

    buckets = [[] for _ in range(p)]
    for a in A:
        for j in range(1, len(splitters)):
            if splitters[j - 1] < a <= splitters[j]:
                buckets[j - 1].append(a)
                break

    stack = [(bucket, k, p, threshold) for bucket in buckets]
    sorted_buckets = []
    while stack:
        bucket, k, p, threshold = stack.pop()
        if len(bucket) > 1:
            S = sample_sort(bucket, k, p, threshold)
            sorted_buckets.extend(S)
        else:
            sorted_buckets.extend(sorted(bucket))

    return sorted_buckets


A = np.random.randint(0, 10000, size=10000)
n = 10
k = 5
threshold = 10000

print("Original array:", A)
start_time = time.time()  # Record start time
sorted_A = sample_sort(A,n,k, threshold)
end_time = time.time()  # Record end time
print("Time taken for sorting:", end_time - start_time, "seconds")
print("Sorted array:", sorted_A)

