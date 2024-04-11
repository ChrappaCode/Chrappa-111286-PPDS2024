import time
import numpy as np


def sample_sort_serialized(A, threshold):
    n = len(A)
    # Step 1
    if n < threshold:
        return sorted(A)

    # Step 2
    split_index = n // 2
    splitter = A[split_index]

    # Step 3
    left_bucket = [x for x in A if x <= splitter]
    right_bucket = [x for x in A if x > splitter]

    # Step 4 and concatenation
    sorted_left = sample_sort_serialized(left_bucket, threshold)
    sorted_right = sample_sort_serialized(right_bucket, threshold)
    sorted_A = sorted_left + sorted_right

    return sorted_A


# Test the implementation
A = np.random.randint(0, 10000, size=10)
threshold = 10

print("Original array:", A)
start_time = time.time()  # Record start time
sorted_A = sample_sort_serialized(A, threshold)
end_time = time.time()  # Record end time
print("Time taken for sorting:", end_time - start_time, "seconds")
print("Sorted array:", sorted_A)
