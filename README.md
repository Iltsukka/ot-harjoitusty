# Ohjelmistotekniikka, harjoitustyo
## Book management app
Ohjelma, jonka avulla ylläpidetään lukulistaa, jolta voi lisätä, poistaa ja suodattaa kirjoja. Ohjelman tarkoituksena on luoda alusta, jolla näitä toimintoja on helppo hallinnoida.

## Dokumentaatio:

[Vaatimusmäärittely](https://github.com/Iltsukka/ot-harjoitusty/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/Iltsukka/ot-harjoitusty/blob/main/dokumentaatio/tuntikirjanpito.md)

[Changelog -tiedosto](https://github.com/Iltsukka/ot-harjoitusty/blob/main/dokumentaatio/changelog.md)

[Arkkitehtuurikuvaus](https://github.com/Iltsukka/ot-harjoitusty/blob/main/dokumentaatio/arkkitehtuuri.md)

## Alustustoimenpiteet:

### Suoritusympäristön alustaminen:

Suorita projektin juurihakemistossa komento `poetry install`, jotta sovelluksen suoritusympäristö päivittyy

### Tietokannan alustaminen:

#### Varsinainen tietokanta:

Luo projektin juurihakemistoon tiedosto .env, jossa rivi `DATABASE_NAME=haluamasi_tietokannan_nimi.sqlite`, ESIMERKIKSI `DATABASE_NAME=database.sqlite`

#### Testitietokanta:

Luo myös juurihakemistoon tiedosto .env.test, jossa rivi `DATABASE_NAME=testitietokannan_nimi.sqlite`, ESIMERKIKSI `DATABASE_NAME=test-database.sqlite`

#### Build:

Suorita .env ja .env.test -tiedostojen luonnin jälkeen projektin juurihakemistossa komento `poetry run invoke build`, joka luo tietokannan /data hakemiston alle

## Komentorivitoiminnot:

### Sovelluksen käynnistys:
Komento `poetry run invoke start` käynnistää ohjelman

### Testaaminen:
Komento `poetry run invoke test` suorittaa testit

### Testikattavuusraportti:
Komento `poetry run invoke coverage-report` suorittaa testit ja muodostaa testikattavuusraportin, joka avautuu suoraan oletusselaimeen (Vain Linux -käyttöjärjestelmällä)

### Staattinen analyysi:
Komento `poetry run invoke lint` suorittaa .pylintrc -tiedostossa määrätyillä asetuksilla koodin staattisen analyysin ja antaa palautetta koodin laadusta. Testi- ja käyttöliittymähakemistot on jätetty analyysin ulkopuolelle.
