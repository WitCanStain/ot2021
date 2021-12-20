# Käyttöohje

## Käynnistäminen

Kun pelin koodi on ladattu koneelle, täytyy asentaa riippuvuudet komennolla `poetry install`. 

Pelin voi käynnistää ajamalla komennon `poetry run invoke start`. Jos haluaa ladata aiemmin tallentamansa pelin, voi käyttää lisäksi vipua `-s`: `poetry run invoke start -s [savegame]`, missä  `[savegame]` on joko polku johonkin tiedostoon tai sitten `saved_games`-kansiossa olevan tallennetun pelitiedoston nimi. Jos haluaa niin voi myös luoda tekstitiedostoon omia tasojaan `settings.py`:stä löytyvän mallin mukaisesti ja ladata sen peliin `-l`-vivulla: `poetry run invoke start -l [level_map]`. Tässä `[level_map]` on samoin kuin yllä, polku johonkin tiedostoon tai sitten `level_maps`-kansiosta löytyvän tiedoston nimi. Huomaa, että jos pelikartta ei sisällä yhtäkään kolikkoa niin peli päättyy välittömästi voittoon.

## Pelaaminen

Käyttäjä voi pelin aloitettuaan liikkua oikealle ja vasemmalle nuolinäppäimillä, ja hypätä yläuolinäppäimellä. Painamalla ESC tulee näkyviin pelin valikko, jonka 
nappuloita painamalla voi jatkaa peliä, uudelleenkäynnistää tason, tallentaa pelin tai lopettaa pelin. Tason uudelleenkäynnistäminen toimii myös R-näppäimen kautta, mistä on hyötyä pelin voittaessaan. Tavoitteena on kerätä kaikki tason kolikot, jolloin peli loppuu.

Peli loppuu myös, jos pelaaja koskettaa vihreään viholliseen tai jos pelaaja putoaa tason pohjan alle. Pelin voi väliaikaisesti pysäyttää painamalla P-näppäintä. 
Halutessaan pelin tasoa voi muuttaa editoimalla tiedoston settings.py listaa `LEVEL_MAP`, tai kuten yllä mainittu lataamalla tekstitiedostosta oman tasonsa. Näin voi vaikka muuttaa maailman rakennetta tai lisätä vihollisia tai kolikoita! Huomaa, että mikäli vihollisilla ei ole tiellään esteitä ne jatkavat matkaansa ikuisesti - varmista siis, että ne on jollain tavalla 'aidattu' pelitasoon.
