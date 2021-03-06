# OT-platformer

Ohjelma on peli, jossa napataan kolikoita ja vältellään vihollisia. Pelihahmoa voi liikuttaa nuolinäppäimillä sivuille, ja sillä voi hypätä. Pelin voi sulkea painamalla ruksia ikkunan nurkassa, valitsemalla valikosta Quit-nappula tai painamalla CTRL+C komentolinjalla. Valikon saa avattua ESC-näppäimellä.

## Dokumentaatio

[Käyttöohje](https://github.com/WitCanStain/ot2021/blob/master/documentation/kayttoohje.md)

[Kirjanpito](https://github.com/WitCanStain/ot2021/blob/master/documentation/kirjanpito.md)

[Vaatimusmäärittely](https://github.com/WitCanStain/ot2021/blob/master/documentation/vaatimusmaarittely.md)

[Testaus](https://github.com/WitCanStain/ot2021/blob/master/documentation/testaus.md)

[Arkkitehtuuri](https://github.com/WitCanStain/ot2021/blob/master/documentation/architecture.md)

[Viikon 5 release](https://github.com/WitCanStain/ot2021/releases/tag/viikko5b)

[Loppurelease](https://github.com/WitCanStain/ot2021/releases/tag/v.1.0)

## Ohjelman suorittaminen

Projektin voi suorittaa ajamalla komento `poetry run invoke start`. 

Tallennetun pelin voi ladata vivulla `-s [tiedoston nimi saved_games kansiossa tai polku tiedostoon]`

Oman tasonsa voi ladata vivulla `-l [tiedoston nimi level_maps kansiossa tai polku tiedostoon]`

## Testaus

Testaus suoritetaan komennossa `poetry run invoke test`

## Testikattavuus

Testikattavuusreportti generoidaan komennolla `poetry run invoke coverage-report`

Tämä reportti luodaan htmlcov-hakemistoon.

## Pylint

Pylint-testin voi suorittaa komennolla `poetry run invoke lint`.



