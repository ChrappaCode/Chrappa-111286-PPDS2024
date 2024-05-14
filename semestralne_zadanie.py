__author__ = "Jakub Chrappa"
__email__ = "xchrappaj@stuba.sk"
__ID__ = "111286"

from numba import cuda
import numpy as np
import time


class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    OKYELLOW = '\033[93m'


@cuda.jit
def calculate_area_kernel(rectangles_to_process, areas, covered_points):
    idx = cuda.grid(1)

    if idx < rectangles_to_process.shape[0]:
        rect = rectangles_to_process[idx]
        x1, y1, x2, y2 = rect
        area = 0

        for x in range(x1, x2):
            for y in range(y1, y2):
                if not covered_points[x, y]:
                    area += 1
                    covered_points[x, y] = 1
                    #cuda.atomic.add(covered_points, (x, y), 1)

        areas[idx] = area

def calculate_total_area_parallel(rectangles_to_process):
    min_x = min(rectangles_to_process, key=lambda x: x[0])[0]
    min_y = min(rectangles_to_process, key=lambda x: x[1])[1]
    max_x = max(rectangles_to_process, key=lambda x: x[2])[2]
    max_y = max(rectangles_to_process, key=lambda x: x[3])[3]

    width = max_x - min_x + 1
    height = max_y - min_y + 1

    # Create and initialize the covered points array
    covered_points = np.zeros((width, height), dtype=np.int32)

    # Adjust coordinates of rectangles based on minimum coordinates
    adjusted_rectangles = [(x1 - min_x, y1 - min_y, x2 - min_x, y2 - min_y) for x1, y1, x2, y2 in rectangles_to_process]

    # Copy data to the device
    rectangles_device = cuda.to_device(np.array(adjusted_rectangles, dtype=np.int64))
    areas_device = cuda.to_device(np.zeros(len(rectangles_to_process), dtype=np.int64))
    covered_points_device = cuda.to_device(covered_points)

    # Set up grid and block dimensions
    block_dim = 256  # Adjust block dimension
    grid_dim = (len(rectangles_to_process) + block_dim - 1) // block_dim

    # Launch the kernel
    calculate_area_kernel[grid_dim, block_dim](rectangles_device, areas_device, covered_points_device)

    # Copy the result back to host
    cuda.synchronize()
    areas_host = areas_device.copy_to_host()

    # Sum up the areas
    total_area = np.sum(areas_host)
    return total_area



if __name__ == '__main__':
    file_path = "in-big.txt"

    rectangles = []

    with open(file_path, "r") as file:
        for line in file:
            rectangle = tuple(map(int, line.strip().split(',')))
            rectangles.append(rectangle)

    print("rectangles =", rectangles)

    start_time = time.time()  # Get current time
    total_area_parallel = calculate_total_area_parallel(rectangles)
    end_time = time.time()

    print(Color.OKBLUE + "Tákúto plochu pšenice pokradli mimozemštania z planéty SOL III:" + Color.ENDC,
          Color.OKGREEN + Color.BOLD + f"{total_area_parallel}" + Color.ENDC)

    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")
