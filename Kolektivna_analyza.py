import numpy as np
from mpi4py import MPI
import matplotlib.pyplot as plt

NRA = 10  # number of rows in matrix A
NCA = 3   # number of columns in matrix A
NCB = 7   # number of columns in matrix B

MASTER = 0
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nproc = comm.Get_size()

times = []

def custom_matrix_multiply(A, B):
    # Custom matrix multiplication logic
    nrows, ncols = A.shape[0], B.shape[1]
    C = np.zeros((nrows, ncols), dtype=int)
    for i in range(nrows):
        for j in range(ncols):
            for k in range(NCA):
                C[i][j] += A[i][k] * B[k][j]
    return C

for _ in range(50):  # Run the code 50 times
    if rank == MASTER:
        start_time = MPI.Wtime()

    # Initialization
    rows_per_proc = NRA // nproc
    extra_rows = NRA % nproc

    if rank == MASTER:
        A = np.array([i + j for j in range(NRA) for i in range(NCA)]).reshape(NRA, NCA)
        B = np.array([i + j for j in range(NCA) for i in range(NCB)]).reshape(NCA, NCB)
        C = np.zeros((NRA, NCB), dtype=int)
    else:
        A = None
        B = None
        C = None

    A_loc = np.zeros((rows_per_proc + (1 if rank < extra_rows else 0), NCA), dtype=int)

    # Scatter matrix A
    comm.Scatter([A, MPI.INT], [A_loc, MPI.INT])

    # Broadcast matrix B
    B = comm.bcast(B, root=MASTER)

    C_loc = custom_matrix_multiply(A_loc, B)

    # Gather the results
    C = None
    if rank == MASTER:
        C = np.zeros((NRA, NCB), dtype=int)
    comm.Gather([C_loc, MPI.INT], [C, MPI.INT], root=MASTER)

    # Print the result at MASTER
    if rank == MASTER:
        end_time = MPI.Wtime()
        times.append(end_time - start_time)

if rank == MASTER:
    print(times)
    plt.hist(times, bins=10)
    plt.xlabel('Execution Time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Histogram of Execution Times')
    plt.show()
