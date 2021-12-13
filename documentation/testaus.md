# Testausdokumentti

Ohjelman testaus on tapahtunut unittestin avulla, niin integraatio- ja yksikkötestein kuin myös järjestelmätestein.

## Yksikkö- ja integraatiotestaus

Ohjelman sovelluslogiikka on keskittynyt Level-luokkaan, joka hoitaa pelin tilan päivittämiseen liittyvät asiat. Level-luokkaa testataan TestLevel-luokalla, jossa on sekä integraatiotestejä että yksikkötestejä.
Ennen testejä luodaan uusi Level-olio joka alustetaan sopivalla testikäyttöön tarkoitetulla pelitasoa kuvaavalla kartalla joka on valmiiksi settings.py-moduulissa.
Lisäksi on valmiiksi luotu testikäyttöön tarkoitettu tallennettu pelitila, jota käytetään TestSaveGame-luokassa.

Ohjelman eri aspekteja testataan erillisillä testausluokilla. Physics-moduulia testataan yksikkö- ja integraatiotestein TestPhysics-luoka, a GameSprite-luokkaa TestGameSprite-luokalla, ja pelin tilan tallentamisen 
ja lataamiseen liittyväät toiminnallisuutta TestSaveGame-luokalla. 

## Testikattavuus

Alla näkyy testikoodin kattavuusreportti.

![coverage](https://github.com/WitCanStain/ot2021/blob/master/documentation/coverage.png)

Useimmat pelin toiminnoista on testattu joko yksikkö- tai integraatiotestein. Haarautumakattavuus on 91%.

## Järjestelmätestaus

Ohjelma on järjestelmätestattu manuaalisesti.


## Asennus

Käyttöohjeen mukaiset toimenpiteet on käyty läpi ja testattu, että niillä saadaan peli käyntiin.

## Tominnallisuus

Kaikki vaatimusmäärittelyssä listatus toteutetut ominaisuudet on käyty läpi ja testattu.

## Laatuongelmat

Sovellus ei tällä hetkellä tunnista, onko pelaaja tippunut tason alle. Ainoa keino aloittaa peli uudestaan tällaisessa tilanteessa on käynnistää se uudelleen tai painaa valikosta restart-nappia. Lisäksi pelin viholliset tarvitsevat seinä-blokin tiellensä tai ne jatkavat kulkemista yhteen suuntaan kunnes tippuvat tasolta.
