import random
import time

start_time = time.time()  # Record start time


def sample_sort(A, k, threshold):

    n = len(A)

    # Step 1
    if n / k < threshold:
        return sorted(A)

    S = random.sample(A, k * (p - 1))
    S.sort()
    splitters = [-float('inf')] + [S[i * k] for i in range(1, p - 1)] + [float('inf')]

    # Step 2
    buckets = [[] for _ in range(k)]
    for a in A:
        for j in range(len(splitters) - 1):
            if splitters[j] < a <= splitters[j + 1]:
                buckets[j].append(a)
                break

    # Step 3 and concatenation
    sorted_buckets = [sample_sort(bucket, k, threshold) for bucket in buckets]
    sorted_A = [item for sublist in sorted_buckets for item in sublist]


    return sorted_A


# Test the implementation
A = [3, 6, 8, 10, 1, 2, 1, 5, 9, 4, 7]
k = 3  # Number of buckets
p = 2  # Number of partitions
threshold = 10  # Threshold for switching to a different sorting method

print("Original array:", A)
sorted_A = sample_sort(A, k, threshold)
print("Sorted array:", sorted_A)

end_time = time.time()  # Record end time
print("Time taken for sorting:", end_time - start_time, "seconds")