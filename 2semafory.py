"""Tento modul implementuje kód pre zadanie 01 z použitím 2 semaforov pre Jana (vlakno 1) aj Fera (vlakno 2)."""

__author__ = "Jakub Chrappa"
__email__ = "xchrappaj@stuba.sk"

from fei.ppds import Thread, Semaphore, print
from time import sleep

class Shared:
    """Táto trieda reprezentuje zdielané dáta"""
    def __init__(self, j, f):
        """Inicializácia zdielaných dát (v našom zadaní semafórov)"""
        self.sem_fero = Semaphore(j)  # Semaphore pre Jana, na začiatku blokovaný čaká na signál (0)
        self.sem_jano = Semaphore(f)  # Semaphore pre Fera, na začiatku blokovaný čaká na signál (0)

def spi(osoba, shared):
    """
    Táto funkcia simuluje spánok Jana a Fera
    :param osoba: Id vlákna na určenie či ide o Jana alebo Fera
    :param shared: Zdielaný objekt s informáciou o semaforoch
    """
    if osoba == "Jano" or osoba == "jano" or osoba == 1:
        print("Janko spinká (naraz)")
        shared.sem_fero.signal()
        sleep(2)  # simuluje dlhšie trvanie úkonu

    if osoba == "Fero" or osoba == "fero" or osoba == 2:
        print("Ferko spinká (naraz)")
        shared.sem_jano.signal()
        sleep(2)  # simuluje dlhšie trvanie úkonu

def ranajkuje(osoba):
    """
    Táto funkcia simuluje raňajkovanie Jana a Fera
    :param osoba: Id vlákna na určenie či ide o Jana alebo Fera
    """
    if osoba == "Jano" or osoba == "jano" or osoba == 1:
        print("Janko papá raňajky")
        sleep(2)  # simuluje dlhšie trvanie úkonu

    if osoba == "Fero" or osoba == "fero" or osoba == 2:
        print("Ferko papá raňajky")
        sleep(2)  # simuluje dlhšie trvanie úkonu

def umyva_sa(osoba):
    """
    Táto funkcia simuluje rannú hygienu Jana a Fera
    :param osoba: Id vlákna na určenie či ide o Jana alebo Fera
    """
    if osoba == "Jano" or osoba == "jano" or osoba == 1:
        print("Janko sa umýva (naraz)")
        sleep(1)  # simuluje dlhšie trvanie úkonu


    if osoba == "Fero" or osoba == "fero" or osoba == 2:
        print("Ferko sa umýva (naraz)")
        sleep(1)  # simuluje dlhšie trvanie úkonu

def jano(shared):
    """
    Táto funkcia simuluje Janove ráno
    :param shared: Zdielané data o semaforoch
    """
    spi(1, shared)
    shared.sem_jano.wait()  # Z dôvodu aby začali umývanie spolu naraz (teoreticky nepotrebné ale pre vizualizáciu krajšie)
    umyva_sa(1)
    ranajkuje(1)  # Jano sa naje
    print("Janko volá Ferkovi nech začne chalovať")
    sleep(1)  # simuluje dlhšie trvanie úkonu
    shared.sem_fero.signal()  # Signal pre Fera aby išiel jesť

def fero(shared):
    """
    Táto funkcia simuluje Ferove ráno
    :param object shared: Zdielané data o semaforch
    """
    spi(2, shared)  # Fero spí
    shared.sem_fero.wait()  # Z dôvodu aby začali umývanie spolu naraz (teoreticky nepotrebné ale pre vizualizáciu krajšie)
    umyva_sa(2)  # Fero sa umýva
    shared.sem_fero.wait()  # Čaká na Jana nech sa prvý naje
    print("Ferko prijal hovor a ide na chálku")
    sleep(1)  # simuluje dlhšie trvanie úkonu
    ranajkuje(2)  # Fero sa naje

def main():
    """Táto funkcia vytvára zdielaný objekt a vlákna pre Jana a Fera"""

    shared = Shared(0, 0)  # inicializácia zdielaných semaforov

    jano_vlakno = Thread(jano, shared)  # vlákno 1 reprezentuje Jana
    fero_vlakno = Thread(fero, shared)  # vlákno 2 reprezentuje Fera

    jano_vlakno.join()
    fero_vlakno.join()

if __name__ == "__main__":
    main()
