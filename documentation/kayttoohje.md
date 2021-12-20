# Käyttöohje

## Käynnistäminen

Kun pelin koodi on ladattu koneelle, täytyy asentaa riippuvuudet komennolla `poetry install`. 

Pelin voi käynnistää ajamalla komennon `poetry run invoke start`. Jos haluaa ladata aiemmin tallentamansa pelin, voi käyttää lisäksi vipua `--file`: `poetry run invoke start --file=savegame`. 

## Pelaaminen

Käyttäjä voi pelin aloitettuaan liikkua oikealle ja vasemmalle nuolinäppäimillä, ja hypätä yläuolinäppäimellä. Painamalla ESC tulee näkyviin pelin valikko, jonka 
nappuloita painamalla voi jatkaa peliä, uudelleenkäynnistää tason, tallentaa pelin tai lopettaa pelin. Tavoitteena on kerätä kaikki tason kolikot, jolloin peli loppuu.

Peli loppuu myös, jos pelaaja koskettaa vihreään viholliseen. Pelin voi väliaikaisesti pysäyttää painamalla P-näppäintä. 
Halutessaan pelin tasoa voi muuttaa editoimalla tiedoston settings.py listaa `LEVEL_MAP`. Näin voi vaikka muuttaa maailman rakennetta tai lisätä vihollisia tai kolikoita!
