import numpy as np
from mpi4py import MPI
import matplotlib.pyplot as plt

NRA = 10  # number of rows in matrix A
NCA = 3   # number of columns in matrix A
NCB = 7   # number of columns in matrix B

MASTER = 1
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nproc = comm.Get_size()

times = []

for _ in range(50):  # Run the code 50 times
    if rank == MASTER:
        start_time = MPI.Wtime()

    # Initialization
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
                C[ind:ind + len(C_loc)] = C_loc
                ind += len(C_loc)
                continue
            C_recv = comm.recv(source=proc)
            row_start = ind
            row_end = ind + len(C_recv)
            C[row_start:row_end] = C_recv
            ind = row_end

        print("Vysledok nasobenia:")
        print(C)
        end_time = MPI.Wtime()
        print("Čas:", end_time - start_time, "sekúnd")
        end_time = MPI.Wtime()
        times.append(end_time - start_time)

if rank == MASTER:
    print(times)
    plt.hist(times, bins=10)
    plt.xlabel('Execution Time (seconds)')
    plt.ylabel('Frequency')
    plt.title('Histogram of Execution Times')
    plt.show()
