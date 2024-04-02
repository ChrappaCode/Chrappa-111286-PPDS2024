import numpy as np
from mpi4py import MPI
import matplotlib.pyplot as plt

NRA = 10  # number of rows in matrix A
NCA = 3   # number of columns in matrix A
NCB = 7   # number of columns in matrix B

times = []

for _ in range(50):  # Run the code 50 times
    start_time = MPI.Wtime()

    print("Paralelne násobenie matíc..")
    print(f"Matrix sizes A[{NRA}][{NCA}], B[{NCA}][{NCB}], C[{NRA}][{NCB}]")

    A = np.array([i + j for j in range(NRA) for i in range(NCA)]).reshape(NRA, NCA)
    B = np.array([i + j for j in range(NCA) for i in range(NCB)]).reshape(NCA, NCB)

    print("Nasobenie matíc..")
    print(A.dot(B))

    print("Vysledok nasobenia:")
    end_time = MPI.Wtime()
    times.append(end_time - start_time)
    print("Čas:", end_time - start_time, "sekúnd")

plt.hist(times, bins=10)
print(times)
plt.xlabel('Execution Time (seconds)')
plt.ylabel('Frequency')
plt.title('Histogram of Execution Times')
plt.show()

print("HOTOVO")
