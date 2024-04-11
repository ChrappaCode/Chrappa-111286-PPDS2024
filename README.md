# Zadanie 05

Táto vetva obsahuje zdrojové kódy ku zadaniu 5 z PPDS. Zadanie je vyvíjané v Pythone a testované s interpreterom `3.12`. Na implementáciu CUDY používam simulátor pretože môj notebook nemá grafickú kartu NVIDIA.

## sample_sort_serial.py

Tento kód implementuje algoritmus nazvaný "*sample sort*" na triedenie polí. Ide o algoritmus, ktorý je podobný quicksortu. Ide o sériové riešenie tohto problému.

Výstup pre malý vstup (array size 10):

![](/img/vystup_serial_maly_vstup.png)

Výstup pre priemerný vstup (array size 10000):

![](/img/vystup_serial_mriemerny_vstup.png)

Výstup pre veľký vstup (array size 100000000):

![](/img/vystup_serial_velky_vstup.png)


## cuda_riesenie.py

Tento kód implementuje paralelný triediaci algoritmus nazvaný "*sample sort*" pomocou technológie `CUDA` s pomocou knižnice `numba`.

**Veľkosť bloku:** Definujeme veľkosť bloku pre CUDA jadrá. Táto hodnota ovplyvňuje, koľko vlákien bude spustených na jednom multiprocesore na GPU. Zmenou premennej `BLOCK_SIZE` na požadovaný počet vlákien na blok a CUDA jadro počas vykonávania použije túto hodnotu.

**CUDA funkcia insertion_sort:** Toto je implementácia algoritmu insertion sort pomocou Numba CUDA. Každé vlákno na GPU sa stará o triedenie časti poľa pomocou tohto algoritmu.

**Funkcia sample_sort:** Táto funkcia riadi celý algoritmus vzorkového triedenia. Najprv prebieha fáza vzorkovania a triedenia na CPU, kde sa vyberú vzorky a zoradia sa. Potom sa vyberú pivoty a prvky sa rozdelia do podmnožín. Potom je každá podmnožina triedená paralelne pomocou insertion sort na GPU. Nakoniec sú zoradené podmnožiny spojené do konečného zoradeného poľa.

Rozdelenie do subsetov:

![](/img/rozdelovanie.png)

Výstup pre malý vstup (array size 10):

![](/img/vystup_cuda_maly_vstup.png)

Výstup pre priemerný vstup (array size 10000):

![](/img/vystup_cuda_mriemerný_vstup.png)

Výstup pre veľký vstup (array size 10000000):

![](/img/vystup_cuda_velky_vstup2.png)

Bohužial výsledky pre CUDA riešenie nie sú ideálne práve aj kvôli tomu, že používam len pomalý CUDA simulátor.


## Zdroje

*[Markdown Guide](https://www.markdownguide.org)*

*Seminár 8 PDF*

*Seminár 8 kódy z GitHub*

*[ChatGPT](https://chat.openai.com/)*

*[Numba Cuda Introduction](https://nyu-cds.github.io/python-numba/05-cuda/)*
