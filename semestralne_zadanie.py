__author__ = "Jakub Chrappa"
__email__ = "xchrappaj@stuba.sk"
__ID__ = "111286"


from numba import cuda
import numpy as np
import time
#import matplotlib.pyplot as plt

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
    """
    Funckia kernelu CUDA
    Tento kernelový kód je zodpovedný za označenie buniek mriežky,
    ktoré pokrývajú každý obdĺžnik.
    @param rectangles_to_process: Pole obdĺžnikov na spracovanie
    @param grid: Mriežka na označenie
    @param min_x: Minimálna súradnica x mriežky
    @param min_y: Minimálna súradnica y mriežky
    """

    idx = cuda.grid(1)

    if idx < rectangles_to_process.shape[0]:
        rect = rectangles_to_process[idx]
        x1, y1, x2, y2 = rect
        for x in range(x1, x2):
            for y in range(y1, y2):
                grid[x - min_x, y - min_y] = 1


@cuda.reduce
def sum_reduce(a, b):
    """
    Operáciu redukcie na sčítanie hodnôt v poli
    @param a: Prvý operand
    @param b: Druhý operand
    """

    return a + b


def calculate_total_area_parallel(rectangles):
    """
    Táto funkcia inicializuje mriežku s nulami zodpovedajúcimi ohraničujúcemu obdĺžniku
    Skopíruje dáta (obdĺžniky a mriežku) na GPU
    Vráti celkovú plochu
    @param rectangles: zoznam obdĺžnikov
    """

    min_x = min(rectangles, key=lambda x: x[0])[0]
    min_y = min(rectangles, key=lambda x: x[1])[1]
    max_x = max(rectangles, key=lambda x: x[2])[2]
    max_y = max(rectangles, key=lambda x: x[3])[3]

    width = max_x - min_x + 1
    height = max_y - min_y + 1

    grid = np.zeros((width, height), dtype=np.int64)

    # Kopíruje dáta na device
    rectangles_device = cuda.to_device(np.array(rectangles, dtype=np.int64))
    grid_device = cuda.to_device(grid)

    block_dim = 128
    grid_dim = (len(rectangles) + block_dim - 1) // block_dim

    # Spustí kernel na aktualizáciu mriežky
    update_grid_kernel[grid_dim, block_dim](rectangles_device, grid_device, min_x, min_y)

    cuda.synchronize()

    # Spočítaj hodnoty pomocou paralelnej redukcie
    total_area = sum_reduce(grid_device.reshape(-1)).item()  # Zmeň na 1D pole pre redukciu
    return total_area


if __name__ == '__main__':
    file_path = "inputs/in-edges.txt"

    rectangles_from_file = []

    with open(file_path, "r") as file:
        for line in file:
            rectangle = tuple(map(int, line.strip().split(',')))
            rectangles_from_file.append(rectangle)

    #print("rectangles =", rectangles)

    #execution_times = []  # List to store execution times
    #for _ in range(5):  # Run the code 5 times
    #    start_time = time.time()
    #    total_area_parallel = calculate_total_area_parallel(rectangles_from_file)
    #    end_time = time.time()
    #    execution_time = end_time - start_time
    #    execution_times.append(execution_time)

    # Plotting
    #plt.plot(range(1, 6), execution_times, marker='o', color="green")  # Plot execution times
    #plt.xlabel('Iterácia')
    #plt.ylabel('Čas (sekundy)')
    #plt.title('Časový graf')
    #plt.grid(True)
    #plt.show()

    start_time = time.time()
    total_area_parallel = calculate_total_area_parallel(rectangles_from_file)
    end_time = time.time()

    print(Color.OKBLUE + "Tákúto plochu pšenice pokradli mimozemštania z planéty SOL III:" + Color.ENDC,
          Color.OKGREEN + Color.BOLD + f"{total_area_parallel}" + Color.ENDC)

    execution_time = end_time - start_time
    print("Čas:", execution_time, "sekúnd")
