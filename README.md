# Semestrálne zadanie

Táto vetva obsahuje zdrojové kódy ku semestrálnemu zadaniu z PPDS. Zadanie je vyvíjané v Pythone a testované s interpreterom `3.12`. Na implementáciu CUDY používam simulátor pretože môj notebook nemá grafickú kartu NVIDIA.

## semestralne_zadanie.py

Tento kód implementuje *Úlohu 5 - Zber úrody pšenice na planéte SOL III*.

Problémom úlohy je vytvorenie paralelného algoritmu pre výpočet obshahu viacerých obdĺžnikov (*vyzbieranej úrody na planéte SOL III*). Výpočet musí počítať s možným prekrývaním obdĺžnikov. Ak 2 (a viac) obdĺžnikov pokrýva rovnakú plochu program túto plochu započíta len jeden krát. Obdĺžníky sú inicializované v textovom súbore ako súradnice `x1, y1, x2, y2` kde `x1, y1` je ľavý dolný okraj obdĺžnika a `x2, y2` je pravý horný okraj obdĺžnika.

Paralelizácia je dosiahnutá hlavne prostredníctvom kernelu CUDA vo funkcii `update_grid_kernel` a redukcie CUDA vo funkcii `sum_reduce`. Kernelová funkcia je vykonávaná paralelne viacerými vláknami na GPU, pričom každé vlákno spracúva jeden obdĺžnik. Redukčná operácia potom spája výsledky všetkých vlákien na výpočet celkovej plochy pokrytej obdĺžnikmi.

Testovanie pre rôzne vstupy (čas vypočítaný na základe viacerých meraní):

| **Vstup** | **Veľkosť blokov** | **Čas vykonávania (v sekundách)** |**Výsledok**|
|-------|----------------|-----------------|-------|
| in-edges.txt  | 64           | 0.0069             |68|
| in-assignment.txt  | 128           | 0.0079            |42|
|in-big.txt|      256   |   55.52              |3669213|

Ukážka výstupu do konzoly:

![](/img/vystup.png)

Časové grafy pre každý vstup:

in-assignment.txt:

Solarized dark             |  Solarized Ocean
:-------------------------:|:-------------------------:
![](/img/in_ass_graf.png)  |  ![](/img/in_edges_graf.png)

in-edges.txt:

![](/img/in_edges_graf.png)

in-big.txt:

![](/img/in_big_graf.png)


## Zdroje

*[Markdown Guide](https://www.markdownguide.org)*

*[ChatGPT](https://chat.openai.com/)*

*[Numba Cuda Introduction](https://nyu-cds.github.io/python-numba/05-cuda/)*

*[Zadanie úlohy](https://elearn.elf.stuba.sk/moodle/pluginfile.php/77429/mod_resource/content/1/PPDS_2024_semestralne_zadanie-v2.pdf)*
