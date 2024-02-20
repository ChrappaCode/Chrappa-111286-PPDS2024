"""Tento modul implementuje kód pre zadanie 01 z použitím 1 semafora."""

__author__ = "Jakub Chrappa"
__email__ = "xchrappaj@stuba.sk"

from fei.ppds import Thread, Semaphore, print
from time import sleep

class Shared:
    """Táto trieda reprezentuje zdielané dáta"""
    def __init__(self, j):
        """Inicializácia zdielaných dát"""
        self.semafor = Semaphore(j)  # Semaphore, na začiatku blokovaný čaká na signál (0)

def spi(osoba):
    """
    Táto funkcia simuluje spánok Jana a Fera
    :param osoba: Id vlákna na určenie či ide o Jana alebo Fera
    """
    if osoba == "Jano" or osoba == "jano" or osoba == 1:
        print("Janko spinká (naraz)")
        sleep(2)  # simuluje dlhšie trvanie úkonu

    if osoba == "Fero" or osoba == "fero" or osoba == 2:
        print("Ferko spinká (naraz)")
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
    :param shared: Zdielané data o semafore
    """
    spi(1)
    umyva_sa(1)
    ranajkuje(1)  # Jano sa naje
    print("Janko volá Ferkovi nech začne chalovať")
    sleep(1)  # simuluje dlhšie trvanie úkonu
    shared.semafor.signal()  # Signal pre Fera aby išiel jesť


def fero(shared):
    """
    Táto funkcia simuluje Ferove ráno
    :param object shared: Zdielané data o semafore
    """
    spi(2)  # Fero spí
    umyva_sa(2)  # Fero sa umýva
    shared.semafor.wait()  # Čaká na Jana nech sa prvý naje
    print("Ferko prijal hovor a ide na chálku")
    sleep(1)  # simuluje dlhšie trvanie úkonu
    ranajkuje(2)  # Fero sa naje

def main():
    """Táto funkcia vytvára zdielaný objekt a vlákna pre Jana a Fera"""

    shared = Shared(0)  # inicializácia semaforu

    jano_vlakno = Thread(jano, shared)  # vlákno 1 reprezentuje Jana
    fero_vlakno = Thread(fero, shared)  # vlákno 2 reprezentuje Fera

    jano_vlakno.join()
    fero_vlakno.join()

if __name__ == "__main__":
    main()
