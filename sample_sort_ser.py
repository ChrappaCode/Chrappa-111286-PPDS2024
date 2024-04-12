import random
import time
import numpy as np

def sample_sort(A, k, p, threshold):
    n = len(A)

    # If average bucket size is below the threshold, switch to another sorting algorithm
    if n / k < threshold:
        A.sort()  # Use another sorting algorithm, e.g., quicksort
        return A

    # Step 1: Select samples and sort them
    if k >= n:
        S = sorted(A)
    else:
        S = [random.sample(A, k) for _ in range(p)]  # Randomly select k samples for each set
        S = [item for sublist in S for item in sublist]  # Flatten the list of samples
        S.sort()  # Sort the samples

    # Generate splitters
    splitters = [float('-inf')] + [S[i * k] for i in range(1, p)] + [float('inf')]

    # Step 2: Place elements in buckets
    buckets = [[] for _ in range(p)]
    for a in A:
        for j in range(1, len(splitters)):
            if splitters[j - 1] < a <= splitters[j]:
                buckets[j - 1].append(a)
                break

    # Step 3 and concatenation using a stack
    stack = [(bucket, k, p, threshold) for bucket in buckets]
    sorted_buckets = []
    while stack:
        bucket, k, p, threshold = stack.pop()
        if len(bucket) > 1:
            # Divide the bucket further
            S = sample_sort(bucket, k, p, threshold)
            sorted_buckets.extend(S)
        else:
            # Sort the bucket
            sorted_buckets.extend(sorted(bucket))

    return sorted_buckets


# Example usage
A = np.random.randint(0, 10000, size=10000)
n = 10
k = 5
threshold = 10000  # Set threshold to a smaller value

print("Original array:", A)
start_time = time.time()  # Record start time
sorted_A = sample_sort(A,n,k, threshold)
end_time = time.time()  # Record end time
print("Time taken for sorting:", end_time - start_time, "seconds")
print("Sorted array:", sorted_A)

