__authors__ = "Jakub Chrappa"
__email__ = "xchrappaj@stuba.sk"

from fei.ppds import Mutex, Thread, Semaphore, print
from time import sleep

N = 9
C = 5

class SimpleBarrier(object):
    """
    Jednoduchá bariéra
    """
    def __init__(self, n, shared):
        self.N = n
        self.cnt = 0
        self.mutex = Mutex()
        self.barrier = Semaphore(0)
        self.shared = shared


    def wait(self, is_nastup=False, is_vystup=False):
        self.mutex.lock()
        self.cnt += 1
        if self.cnt == self.N:
            self.cnt = 0

            if is_nastup:
                self.shared.nastupiliVsetci.signal()
            elif is_vystup:
                self.shared.vystupiliVsetci.signal()

            self.barrier.signal(self.N)
        self.mutex.unlock()
        self.barrier.wait()

class Shared(object):
    """
    Shared pre zdielané dáta
    """

    def __init__(self):
        self.nastupQueue = Semaphore(0)
        self.nastupBarier = SimpleBarrier(C, self)
        self.nastupiliVsetci = Semaphore(0)

        self.vystupQueue = Semaphore(0)
        self.vystupBarier = SimpleBarrier(C, self)
        self.vystupiliVsetci = Semaphore(0)


def pasazier(i, shared):
    """
    Táto funckia reprezentuje pasažiera a jeho úkony
    :param i: id pasažiera
    :param shared: zdielané dáta
    """
    while True:
        shared.nastupQueue.wait()
        nastup(i)
        shared.nastupBarier.wait(is_nastup=True)

        shared.vystupQueue.wait()
        vystup(i)
        shared.vystupBarier.wait(is_vystup=True)

def husenka(shared):
    """
    Táto funckia reprezentuje húsenku na dráhe
    :param shared: zdielané dáta
    """
    while True:
        napln()
        shared.nastupQueue.signal(C)
        shared.nastupiliVsetci.wait()

        jazda()
        vyprazdni()

        shared.vystupQueue.signal(C)
        shared.vystupiliVsetci.wait()

def nastup(i):
    print(f"Pasažier {i} nastúpil do húsenky!")
    sleep(0.7)

def vystup(i):
    print(f"Pasažier {i} vystúpil z húsenky!")
    sleep(0.7)

def napln():
    print("Husenková dráha je na mieste a čaká na nástup pasažierov!")
    sleep(1)
def jazda():
    print("Húsenková dráha ide weeee!")
    sleep(2)

def vyprazdni():
    print("Husenková dráha skončila jazdu pasažieri môžu vystúpiť!")
    sleep(1)

def main():
    """
    Vytváranie vlákien a volanie funkcií
    """
    shared = Shared()

    pasaziery = []

    for i in range(N):
        pasaziery.append(Thread(pasazier, i, shared))
    husenka_ = Thread(husenka, shared)

    for t in pasaziery + [husenka_]:
        t.join()


if __name__ == "__main__":
    main()
