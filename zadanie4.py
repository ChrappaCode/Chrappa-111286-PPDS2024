import numpy as np
from mpi4py import MPI

NRA = 10  # number of rows in matrix A
NCA = 3   # number of columns in matrix A
NCB = 7   # number of columns in matrix B

MASTER = 0
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nproc = comm.Get_size()

print("Paralelne násobenie matíc..")
print(f"Matrix sizes A[{NRA}][{NCA}], B[{NCA}][{NCB}], C[{NRA}][{NCB}]")

# Initialization
print("Inicializácia..")

rows_per_proc = NRA // nproc
extra_rows = NRA % nproc

if rank != MASTER:
    A_loc = None
    B = None
else:
    A = np.array([i + j for j in range(NRA) for i in range(NCA)]).reshape(NRA, NCA)
    B = np.array([i + j for j in range(NCA) for i in range(NCB)]).reshape(NCA, NCB)
    C = np.zeros((NRA, NCB), dtype=int)

    ind = 0
    for proc in range(nproc):
        if proc == MASTER:
            A_loc = A[ind:ind+rows_per_proc + (1 if proc < extra_rows else 0)]
            ind += rows_per_proc + (1 if proc < extra_rows else 0)
            continue
        comm.send(A[ind:ind+rows_per_proc + (1 if proc < extra_rows else 0)], dest=proc)
        ind += rows_per_proc + (1 if proc < extra_rows else 0)

B = comm.bcast(B, root=MASTER)

print("Performing matrix multiplication..")
C_loc = np.zeros((rows_per_proc + (1 if rank < extra_rows else 0), NCB), dtype=int)

if rank != MASTER:
    C_loc = np.dot(comm.recv(), B)
else:
    for i in range(len(C_loc)):
        for j in range(NCB):
            for k in range(NCA):
                C_loc[i][j] += A_loc[i][k] * B[k][j]

if rank != MASTER:
    comm.send(C_loc, dest=MASTER)
else:
    ind = 0
    for proc in range(nproc):
        if proc == MASTER:
            C[ind:ind+rows_per_proc + (1 if proc < extra_rows else 0)] = C_loc
            ind += rows_per_proc + (1 if proc < extra_rows else 0)
            continue
        C_loc = comm.recv(source=proc)
        C[ind:ind + len(C_loc)] = C_loc
        ind += len(C_loc)

    print("Vysledok nasobenia:")
    print(C)

#print(A.dot(B))
print("HOTOVO")