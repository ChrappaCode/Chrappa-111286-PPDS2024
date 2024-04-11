# Zadanie 05

Táto vetva obsahuje zdrojové kódy ku zadaniu 5 z PPDS. Zadanie je vyvíjané v Pythone a testované s interpreterom `3.12`. Na implementáciu CUDY používam simulátor pretože môj notebook nemá grafickú kartu NVIDIA.

## sample_sort_serial.py

Tento kód implementuje algoritmus nazvaný "sample sort" na triedenie polí. Ide o algoritmus, ktorý je podobný quicksortu. Ide o sériové riešenie tohto problému.

Výstup pre malý vstup (10):

![](/img/vystup_serial_maly_vstup.png)

Výstup pre priemerný vstup (10000):

![](/img/vystup_serial_mriemerny_vstup.png)

Výstup pre veľký vstup (10000000):

![](/img/vystup_serial_velky_vstup.png)


## sample_sort_cuda.py

Tento kód implementuje paralelný triediaci algoritmus nazvaný "sample sort" pomocou technológie `CUDA` s pomocou knižnice `Numba`.

Výstup pre malý vstup (10):

![](/img/vystup_cuda_maly_vstup.png)

Výstup pre priemerný vstup (10000):

![](/img/vystup_cuda_mriemerný_vstup.png)

Výstup pre veľký vstup (10000000):

![](/img/vystup_cuda_velky_vstup.png)


## Zdroje

*[Markdown Guide](https://www.markdownguide.org)*

*Seminár 8 PDF*

*Seminár 8 kódy z GitHub*

*[ChatGPT](https://chat.openai.com/)*

*[Numba Cuda Introduction](https://nyu-cds.github.io/python-numba/05-cuda/)*
