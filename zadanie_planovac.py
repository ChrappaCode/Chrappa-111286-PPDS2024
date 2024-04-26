import queue
from random import randint

class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    OKYELLOW = '\033[93m'


class Planovac:
    def __init__(self):
        self.fronta = queue.Queue()

    def add_job(self, it):
        """
        Pridá "job" do fronty
        :param it - generátoroví iterátor
        """
        self.fronta.put(it)

    def start(self):
        """
        Spustí plánovač so všetkými podprogrammi, ktoré sú vo fronte
        Plánovač ide stále dokola pokiaľ sú vo fronte podprogrami
        """
        while not self.fronta.empty():
            it = self.fronta.get()
            try:
                next(it)
                it.send(randint(1, 10))  # Pošle random 1 až 10
                self.add_job(it)  # Dá iterátor späť do fronty
            except StopIteration:
                print(Color.FAIL + f"{it} skončil svoju pracovnú činnosť :)" + Color.ENDC)
                it.close()
            except Exception as e:
                print("Coroutine raised an exception:", e)


def is_prime(n):
    """
    Funckia na zistenie prvočísla
    :param n - číslo, ktoré testuje
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def koprogram_1():
    """
    Prvý koprogram, ktorý prijíma a vypisuje správu (číslo),
    ktorá je nepárna.
    Činnosť vykoná 200 krát
    """
    n = 0
    try:
        while n < 200:
            n += 1
            msg = yield
            if msg % 2:
                print(Color.OKBLUE + f"Podprogram 1 prijal nepárnu správu: {msg}" + Color.ENDC)
            else:
                print(Color.OKBLUE + f"Podprogram 1 nerobí nič (prijal párnu správu)" + Color.ENDC)
            yield
    except GeneratorExit:
        print("Generator Exit")


def koprogram_2():
    """
    Druhý koprogram, ktorý vypisuje prvočísla do 300
    """
    n = 0
    try:
        while n < 300:
            n += 1
            yield
            if is_prime(n):
                print(Color.OKGREEN + f"Podprogram 2 vypisuje prvočísla do 300: {n}" + Color.ENDC)
            else:
                print(Color.OKGREEN + "Podprogram 2 nerobí nič (n nie je prvočíslo)" + Color.ENDC)
            yield
    except GeneratorExit:
        print("Generator Exit")


def koprogram_3():
    """
    Tretí koprogram, ktorý vypisuje párne čísla do 1000
    """
    n = 0
    try:
        while n < 1000:
            n += 1
            yield
            if not (n % 2):
                print(Color.OKYELLOW + f"Podprogram 3 vypisuje párne čísla do tisíc: {n}" + Color.ENDC)
            else:
                print(Color.OKYELLOW + "Podprogram 3 nerobí nič (n nie je párne)" + Color.ENDC)
            yield
    except GeneratorExit:
        print("Generator Exit")


if __name__ == '__main__':

    planovac = Planovac()  # inicializácia plánovača

    it1 = koprogram_1()
    it2 = koprogram_2()
    it3 = koprogram_3()

    planovac.add_job(it1)
    planovac.add_job(it2)
    planovac.add_job(it3)

    planovac.start()  # štart plánovača

