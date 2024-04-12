import time
import numpy as np

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def sample_sort(arr):
    # Determine the number of samples
    num_samples = int(len(arr) ** 0.5)

    # Step 1: Sample the data
    samples = sorted([arr[i] for i in range(0, len(arr), len(arr) // num_samples)])

    # Step 2: Broadcast the samples to all processes
    samples = [samples[i * len(samples) // num_samples] for i in range(num_samples)]

    # Step 3: Each process partitions its data based on the sample points
    partitions = [[] for _ in range(num_samples + 1)]
    for num in arr:
        for i in range(num_samples):
            if num < samples[i]:
                partitions[i].append(num)
                break
        else:
            partitions[num_samples].append(num)

    # Step 4: Sort each partition individually
    sorted_partitions = []
    for part in partitions:
        insertion_sort(part)
        sorted_partitions.extend(part)

    return sorted_partitions


# Example usage:
arr = np.random.randint(0, 10000, size=10)
print("Original array:", arr)

start_time = time.time()  # Record start time
sorted_arr = sample_sort(arr)
end_time = time.time()  # Record end time
print("Time taken for sorting:", end_time - start_time, "seconds")

#print("Sorted array:", sorted_arr)
