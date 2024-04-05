import numpy as np
from mpi4py import MPI
import matplotlib.pyplot as plt


NRA = 10  # number of rows in matrix A
NCA = 3   # number of columns in matrix A
NCB = 7   # number of columns in matrix B
a = 0

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nproc = comm.Get_size()

def custom_matrix_multiply(A, B):
    # Custom matrix multiplication logic
    nrows, ncols = A.shape[0], B.shape[1]
    C = np.zeros((nrows, ncols), dtype=int)
    for i in range(nrows):
        for j in range(ncols):
            for k in range(NCA):
                C[i][j] += A[i][k] * B[k][j]
    return C

start_time = MPI.Wtime()
times = []

for _ in range(50):  # Run the code 50 times
    start_time = MPI.Wtime()

    rows_per_proc = NRA // nproc
    extra_rows = NRA % nproc

    A_loc = np.zeros((rows_per_proc + (1 if rank < extra_rows else 0), NCA), dtype=int)

    # Scatter matrix A
    comm.Scatter(
        [None if rank != 0 else np.array([i + j for j in range(NRA) for i in range(NCA)]).reshape(NRA, NCA), MPI.INT],
        [A_loc, MPI.INT])

    B = comm.bcast(None if rank != 0 else np.array([i + j for j in range(NCA) for i in range(NCB)]).reshape(NCA, NCB),
                   root=0)

    print("Nasobenie matíc..")
    C_loc = custom_matrix_multiply(A_loc, B)

    # Gather the results
    C = comm.gather(C_loc, root=0)
    end_time = MPI.Wtime()

    times.append(end_time - start_time)

if a == 0:
    a = 1
    print(times)
    plt.hist(times, bins=10)
    plt.xlabel('Execution Time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Histogram of Execution Times')
    plt.show()
else:
    pass
