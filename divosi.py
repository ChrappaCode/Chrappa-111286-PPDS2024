__authors__ = "Jakub Chrappa"
__email__ = "xchrappaj@stuba.sk"


from fei.ppds import Mutex, Thread, Semaphore, print
from time import sleep

N = 7   # konštanta počet divochov
H = 10  # konštanta počet porcii

class Shared(object):

    def __init__(self):

        self.kucharVar = Semaphore(0)
        self.kucharDovar = Semaphore(0)
        self.hrniec = H  # veľkosť hrnca
        self.mutex = Mutex()


        self.pocitadlo1 = 0
        self.pocitadlo2 = 0

        self.bariera1 = Semaphore(0)
        self.bariera2 = Semaphore(0)

        self.barierMutex = Mutex()
        self.barier2Mutex = Mutex()

def vypis_ze_su_tu_vsetci(i):
    if i == 0:
        print("Všetci divočáci sú tu ide sa jesť")

def divoch_je(i, shared):
    """
    Táto funkcia simuluje hodovanie divochov
    :param shared: Zdielané data
    :param i: id vlákna
    """

    while True:
        shared.barier2Mutex.lock()
        shared.pocitadlo2 += 1
        if shared.pocitadlo2 == N:
            shared.pocitadlo2 = 0
            shared.bariera2.signal(N)
        shared.barier2Mutex.unlock()
        shared.bariera2.wait()

        shared.barierMutex.lock()
        shared.pocitadlo1 += 1
        print(f"Divočák {i} prišiel a čaká na ostatných. Je nás tu: {shared.pocitadlo1}")
        sleep(0.2)
        if shared.pocitadlo1 == N:
            shared.pocitadlo1 = 0
            shared.bariera1.signal(N)
        shared.barierMutex.unlock()
        shared.bariera1.wait()
        vypis_ze_su_tu_vsetci(i)
        sleep(1)

        shared.mutex.lock()
        sleep(0.5)
        print(f"Divočák {i} si prišiel dať porciu")
        sleep(0.5)
        if shared.hrniec == 0:
            print(f"Divočák {i} hlásy kuchárovi, že došlo jedlo")
            shared.kucharVar.signal()
            shared.kucharDovar.wait()
        print(f"Divočák {i} si zobral porciu")
        sleep(0.5)
        shared.hrniec = shared.hrniec - 1
        print(f"V hrnci je ešte : {shared.hrniec} porcií")
        sleep(0.5)
        shared.mutex.unlock()

        print(f"Divočák {i} hoduje")
        sleep(1)
        print(f"Divočák {i} ide na lov")

def varenie(shared):
    """
    Táto funkcia simuluje kuchárovu činnosť: varenie jedla
    :param shared: Zdielané data
    """
    while True:
        shared.kucharVar.wait()  # kuchár čaká kým mu divoch dá signál že je hrniec prázdny
        print("Kuchar varí jedlo pre divočákov")
        sleep(2)  # simuluje dlhšie trvanie úkonu
        shared.hrniec = H  # navarí plný hrniec
        shared.kucharDovar.signal()  # kuchár dá signál že je navarené


def main():
    """Táto funkcia vytvára zdielaný objekt a vlákna pre divochov a kuchára"""

    shared = Shared()
    divoch = []

    for i in range(N):
        divoch.append(Thread(divoch_je, i, shared))
    kuchar = Thread(varenie, shared)

    for t in divoch + [kuchar]:
        t.join()


if __name__ == "__main__":
    main()
