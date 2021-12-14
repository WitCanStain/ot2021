# Arkkitehtuurikuvaus

## Rakenne

Ohjelma on jaettu seuraaviin pakkauksiin:
- assets-pakkauksessa on pelin sisältöön tarvittavia tiedostoja - GameSprite-olioiden kuvat sekä äänet.
- game_utils-pakkauksessa on pelin pelilogiikkaan liittymättömiä toimintoja, kuten pelien tallentaminen ja lataaminen sekä asetukset.
- game_logic-pakkauksessa on peliin sitä pelatessa vaikuttavia toimintoja - GameLoop, Level, sekä Physics-moduuli.
- sprites-pakkauksessa on pelin spritet ja niiden toiminnallisuuksiin liittyviä metodeja. Kaikki pelin spritet perivät GameSprite-luokan, joka taas perii pygame.sprite.Sprite-luokan. Ne spritet, jotka pystyvät vaikuttamaan toisiinsa, perivät GameSprite-luokan ActionSprite-luokan kautta.

Luokkien väliset riippuvuudet on kuvattu alla olevassa luokkakaaviossa.

![UML graph](https://github.com/WitCanStain/ot2021/blob/master/documentation/kuvat/uml.png)

![WebSequence](https://github.com/WitCanStain/ot2021/blob/master/documentation/Moving%20the%20player%20character.png)

## Sovelluslogiikka

Luokka Level vastaa sovelluslogiikan eri komponenttien kokoamisesta yhteen. 

Physics-moduuli sisältää spritejen liikuttamiseen ja pelin fysiikkaan tarvittavia toimintoja.


