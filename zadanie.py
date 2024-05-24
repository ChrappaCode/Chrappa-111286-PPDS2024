__author__ = "Jakub Chrappa"
__email__ = "xchrappaj@stuba.sk"
__ID__ = "111286"

import aiohttp                 # Na asynchrónne HTTP požiadavky
import asyncio                 # Na asynchrónne spracovanie
import os                      # Na prácu so súbormi a cestami k súborom
from tqdm.asyncio import tqdm  # Na zobrazenie progress baru počas asynchrónnych operácií


async def download_file(session, url, destination):
    """
    Stiahne súbor z danej URL a uloží ho do cieľového umiestnenia.

    :param session: Asynchrónna HTTP session
    :param url: URL adresa súboru na stiahnutie
    :param destination: Cieľové umiestnenie na disku, kde sa súbor uloží
    """
    async with session.get(url) as response:
        # Získaj veľkosť súboru z hlavičky odpovede
        total_size = int(response.headers.get('content-length', 0))

        with open(destination, 'wb') as file, tqdm(
                desc=url,
                total=total_size,
                unit='B',
                unit_scale=True,
                unit_divisor=1024,
        ) as bar:
            async for data in response.content.iter_chunked(1024):
                file.write(data)
                bar.update(len(data))


async def main(urls):
    """
    Vytvorí asynchrónnu HTTP session a spustí sťahovanie súborov z daných URL.

    :param urls: Zoznam URL adries súborov na stiahnutie
    """
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            # Získaj názov súboru z URL adresy
            filename = os.path.basename(url)
            # Urči cieľové umiestnenie na disku
            destination = os.path.join(os.getcwd(), filename)
            # Pridaj úlohu na stiahnutie súboru do zoznamu úloh
            tasks.append(download_file(session, url, destination))
        # Spusti všetky úlohy súčasne a čakaj na ich dokončenie
        await asyncio.gather(*tasks)


if __name__ == "__main__":
    # Zoznam URL adries súborov na stiahnutie
    urls = [
        'https://ploszek.com/ppds/2024-05.2.Paralelne_vypocty_2.pdf',
        'https://ploszek.com/ppds/2024-08.cuda.pdf'
    ]
    # Spusti hlavnú asynchrónnu funkciu
    asyncio.run(main(urls))
