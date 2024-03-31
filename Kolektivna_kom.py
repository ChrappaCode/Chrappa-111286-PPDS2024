import numpy as np
from mpi4py import MPI

NRA = 10  # number of rows in matrix A
NCA = 3   # number of columns in matrix A
NCB = 7   # number of columns in matrix B

MASTER = 0
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

if rank == MASTER:
    start_time = MPI.Wtime()

print("Paralelne násobenie matíc..")
print(f"Matrix sizes A[{NRA}][{NCA}], B[{NCA}][{NCB}], C[{NRA}][{NCB}]")

# Initialization
print("Inicializácia..")

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

print("Nasobenie matíc..")
C_loc = custom_matrix_multiply(A_loc, B)

# Gather the results
C = None
if rank == MASTER:
    C = np.zeros((NRA, NCB), dtype=int)
comm.Gather([C_loc, MPI.INT], [C, MPI.INT], root=MASTER)

# Print the result at MASTER
if rank == MASTER:
    print("Vysledok nasobenia:")
    print(C)
    end_time = MPI.Wtime()
    print("Čas:", end_time - start_time, "sekúnd")

print("HOTOVO")