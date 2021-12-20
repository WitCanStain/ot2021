# Arkkitehtuurikuvaus

## Rakenne

Ohjelma on jaettu seuraaviin pakkauksiin:
- assets-pakkauksessa on pelin sisältöön tarvittavia tiedostoja - GameSprite-olioiden kuvat sekä äänet.
- utils-pakkauksessa on pelin pelilogiikkaan liittymättömiä toimintoja, kuten pelien tallentaminen ja lataaminen sekä asetukset.
- gamelogic-pakkauksessa on peliin sitä pelatessa vaikuttavia toimintoja - GameLoop, Level, sekä Physics-moduuli.
- sprites-pakkauksessa on pelin spritet ja niiden toiminnallisuuksiin liittyviä metodeja. Kaikki pelin spritet perivät GameSprite-luokan, joka taas perii pygame.sprite.Sprite-luokan. Ne spritet, jotka pystyvät vaikuttamaan toisiinsa, perivät GameSprite-luokan ActionSprite-luokan kautta.

Luokkien väliset riippuvuudet on kuvattu alla olevassa luokkakaaviossa.

![UML graph](https://github.com/WitCanStain/ot2021/blob/master/documentation/kuvat/uml.png)

Pelaajan liikuttaminen oikean nuolinäppäimen avulla on kuvattu seuraavassa sekvenssikaaviossa:

![WebSequence](https://github.com/WitCanStain/ot2021/blob/master/documentation/kuvat/Moving%20the%20player%20character.png)

## Sovelluslogiikka

GameLoop-luokka luo ja käynnistää pelisilmukan, ja vastaa käyttäjän syötteiden välittämisen Level-luokalle.

Luokka Level vastaa pelin tasoon liittyvistä ominaisuuksista, kuten kolikkojen keräämisestä ja vihollisiin törmäämisestä.

Physics-moduuli sisältää spritejen liikuttamiseen ja pelin fysiikkaan tarvittavia toimintoja.

Sounds-moduuli luo pelin äänet.

GameFile-luokka hoitaa pelin tilan tallentamisen ja lataamisen.

Sprites-pakkauksen luokat hoitavat pelin eri visuaalisten komponenttien luomisen.

Assets-kansiossa on pelin komponenttien kuvat sekä äänet. Kuvat on tehty itse, äänet ovat ilmaiskäyttöön tarkoitettuja.

## Tietojen tallennus ja lataaminen

Pelissä voi tallentaa pelin tilan ja ladata sen myöhemmin. Tämä onnistuu luokan `GameFile` avulla. Tiedostot tallennetaan oletusarvoisesti projektin kansioon nimeltä `saved_games`. Pelin tietojen serialisointiin ja deserialisointiin käytetään Pythonin `Pickle`-kirjastoa. Tallennettujen pelitiedostojen nimet ovat muotoa 

`ot_platformer_2021_12_20_5_48_47`

eli

`ot_platformer_{vuosi}_{kuukausi}_{päivä}_{tunti}_{minuutti}`

Lisäksi peliin voi ladata ulkoisesti määriteltyjä tasotiedostoja, jotka samaten tulkitaan GameFile-luokassa. Pelitilan lataaminen tapahtuu `-s`-vivun avulla komentolinjalla, ja pelitason lataaminen taas `-l`-vivun avulla.

## Ohjelman rakenteeseen jääneet heikkoudet

Pelin luokkarakennetta voisi standardisoida enemmän. Jotkin toiminnallisuudet ovat eriytetty omiin luokkiinsa, kun taas toiset ovat yksittäisiä funktioita joita kutsutaan toisista luokista. Lisäksi `utils`-pakkaukseen on koottu vähän löyhästi toisiinsaliittyviä moduuleja, kuten vaikka `settings.py` sekä `sounds.py`. On mahdollista että näille olisi ollut parempi paikka joko toisissa pakkauksissa tai sitten paremmin nimetyssä pakkauksessa.
