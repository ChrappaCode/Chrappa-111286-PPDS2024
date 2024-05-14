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
def update_grid_kernel(rectangles_to_process, grid, min_x, min_y):
    idx = cuda.grid(1)

    if idx < rectangles_to_process.shape[0]:
        rect = rectangles_to_process[idx]
        x1, y1, x2, y2 = rect
        for x in range(x1, x2):
            for y in range(y1, y2):
                grid[x - min_x, y - min_y] = 1

@cuda.reduce
def sum_reduce(a, b):
    return a + b

def calculate_total_area_parallel(rectangles):
    min_x = min(rectangles, key=lambda x: x[0])[0]
    min_y = min(rectangles, key=lambda x: x[1])[1]
    max_x = max(rectangles, key=lambda x: x[2])[2]
    max_y = max(rectangles, key=lambda x: x[3])[3]

    width = max_x - min_x + 1
    height = max_y - min_y + 1

    grid = np.zeros((width, height), dtype=np.int32)

    # Copy data to the device
    rectangles_device = cuda.to_device(np.array(rectangles, dtype=np.int64))
    grid_device = cuda.to_device(grid)

    # Set up grid and block dimensions
    block_dim = 256
    grid_dim = (len(rectangles) + block_dim - 1) // block_dim

    # Launch the kernel to update the grid
    update_grid_kernel[grid_dim, block_dim](rectangles_device, grid_device, min_x, min_y)
    cuda.synchronize()

    # Sum up the values in the grid using parallel reduction
    total_area = sum_reduce(grid_device.reshape(-1)).item()  # Reshape to 1D array for reduction
    return total_area

if __name__ == '__main__':
    file_path = "inputs/in-big.txt"

    rectangles = []

    with open(file_path, "r") as file:
        for line in file:
            rectangle = tuple(map(int, line.strip().split(',')))
            rectangles.append(rectangle)

    print("rectangles =", rectangles)

    start_time = time.time()
    total_area_parallel = calculate_total_area_parallel(rectangles)
    end_time = time.time()

    print(Color.OKBLUE + "Tákúto plochu pšenice pokradli mimozemštania z planéty SOL III:" + Color.ENDC,
          Color.OKGREEN + Color.BOLD + f"{total_area_parallel}" + Color.ENDC)

    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")
