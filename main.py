'''
from mpi4py import MPI
from random import randint, seed


#print("Hello world! I'm process", rank, "out of", size)

DARTS = 10000
ROUNDS = 10
MASTER = 0

def board(darts):
    score = 0
    for i in range(darts):
        x, y = [randint(0, 65535)/65536*2-1 for _ in range(2)]
        if x**2 + y**2 <= 1.0:
            score += 1

    return 4 * score / darts


def main():
    seed(0)

    comm = MPI.COMM_WORLD
    nprocs = comm.Get_size()
    rank = comm.Get_rank()

    avepi = 0
    for i in range(ROUNDS):
        pi = board(DARTS)

        if rank != MASTER:
            comm.send(pi, dest=MASTER)
        else:
            sum_pi = comm.reduce(pi , op=MPI.SUM, root=MASTER)
            for _ in range(nprocs-1):
                pi = comm.recv()
                sum_pi += pi
            pi = sum_pi / nprocs
            avepi = ((avepi * i) + pi) / (i+1)
            print(f"Odhad po {DARTS*(i+1)*nprocs:6d} hodoch je: {avepi:10f}")
    #print("referenčná hodnota pi je : 3.14159265358979328")

if __name__ == "__main__":
    main()
'''


from mpi4py import MPI
from random import randint, seed


#print("Hello world! I'm process", rank, "out of", size)

DARTS = 10000
ROUNDS = 10
MASTER = 0

def board(darts):
    score = 0
    for i in range(darts):
        x, y = [randint(0, 65535)/65536*2-1 for _ in range(2)]
        if x**2 + y**2 <= 1.0:
            score += 1

    return 4 * score / darts


def main():
    seed(0)

    comm = MPI.COMM_WORLD
    nprocs = comm.Get_size()
    rank = comm.Get_rank()

    avepi = 0
    for i in range(ROUNDS):
        pi = board(DARTS)

        sum_pi = comm.reduce(pi , op=MPI.SUM, root=MASTER)
        if rank == MASTER:
            pi = sum_pi / nprocs
            avepi = ((avepi * i) + pi) / (i+1)
            print(f"Odhad po {DARTS*(i+1)*nprocs:6d} hodoch je: {avepi:10f}")
    #print("referenčná hodnota pi je : 3.14159265358979328")

if __name__ == "__main__":
    main()