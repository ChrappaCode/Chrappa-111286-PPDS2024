# Semestrálne zadanie

Táto vetva obsahuje zdrojové kódy ku semestrálnemu zadaniu z PPDS. Zadanie je vyvíjané v Pythone a testované s interpreterom `3.12`. Na implementáciu CUDY používam simulátor pretože môj notebook nemá grafickú kartu NVIDIA.

## semestralne_zadanie.py

Tento kód implementuje *úlohu 5 - Zber úrody pšenice na planéte SOL III*. Problémom úlohy je vytvorenie paralelného algoritmu pre výpočet obshahu viacerých obdĺžnikov (*vyzbieranej úrody na planéte SOL III*). Výpočet musí počítať s možným prekrývaním obdĺžnikov. Ak 2 (a viac) obdĺžnikov pokrýva rovnakú plochu program túto plochu započíta len jeden krát. Obdĺžníky sú inicializované v textovom súbore ako súradnice `x1, y1, x2, y2` kde `x1, y1` je ľavý dolný okraj obdĺžnika a `x2, y2` je pravý horný okraj obdĺžnika.
 
![](/img/vystup_cuda_mriemerný_vstup.png)

## Zdroje

*[Markdown Guide](https://www.markdownguide.org)*

*[ChatGPT](https://chat.openai.com/)*

*[Numba Cuda Introduction](https://nyu-cds.github.io/python-numba/05-cuda/)*
