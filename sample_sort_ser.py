import time
import numpy as np

def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

def sample_sort_serialized(A, threshold):
    n = len(A)
    stack = [(0, n)]  # Initialize stack with the entire array as the initial subproblem

    while stack:
        start, end = stack.pop()  # Pop the subproblem from the stack
        if end - start <= threshold:  # If subproblem size is less than or equal to threshold, sort it
            A[start:end] = sorted(A[start:end])
        else:  # Otherwise, push subproblems onto the stack
            split_index = (start + end) // 2

            stack.append((start, split_index))
            stack.append((split_index, end))

    # Merge sorted subarrays
    for i in range(2, n + 1):
        for j in range(0, n, i * 2):
            left = A[j:j + i // 2]
            right = A[j + i // 2:j + i]
            A[j:j + i] = merge(left, right)

    return A

# Test the implementation
A = np.random.randint(0, 10000, size=10000)
threshold = 10

print("Original array:", A)
start_time = time.time()  # Record start time
sorted_A = sample_sort_serialized(A, threshold)
end_time = time.time()  # Record end time
print("Time taken for sorting:", end_time - start_time, "seconds")
print("Sorted array:", sorted_A)
