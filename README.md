# Ohjelmistotekniikka, harjoitustyo
## Book management app
Ohjelma, jonka avulla ylläpidetään lukulistaa, jolta voi lisätä, poistaa ja suodattaa kirjoja.

## Dokumentaatio:

[Vaatimusmäärittely](https://github.com/Iltsukka/ot-harjoitusty/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/Iltsukka/ot-harjoitusty/blob/main/dokumentaatio/tuntikirjanpito.md)

[Changelog -tiedosto](https://github.com/Iltsukka/ot-harjoitusty/blob/main/dokumentaatio/changelog.md)

[Arkkitehtuurikuvaus](https://github.com/Iltsukka/ot-harjoitusty/blob/main/dokumentaatio/arkkitehtuuri.md)

## Alustustoimenpiteet:
Suorita projektin juurihakemistossa komento `poetry install`, jotta sovelluksen suoritusympäristö päivittyy
## Komentorivitoiminnot:

### Sovelluksen käynnistys:
Komento `poetry run invoke start` käynnistää ohjelman

### Testaaminen:
Komento `poetry run invoke test` suorittaa testit

### Testikattavuusraportti:
Komento `poetry run invoke coverage-report` suorittaa testit ja muodostaa testikattavuusraportin, joka avautuu suoraan oletusselaimeen (Vain Linux -käyttöjärjestelmällä)
