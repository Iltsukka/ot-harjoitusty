## Käyttöohje:

### Konfiguraatio:

Jos et vielä tehnyt niin, katso README.md -tiedostosta sovelluksen alustustoimenpiteet ja toimi niiden mukaan.

### Komentorivikomennot:

#### Sovelluksen käynnistys:
Komento `poetry run invoke start` käynnistää ohjelman

#### Testaaminen:
Komento `poetry run invoke test` suorittaa testit

#### Testikattavuusraportti:
Komento `poetry run invoke coverage-report` suorittaa testit ja muodostaa testikattavuusraportin, joka avautuu suoraan oletusselaimeen (Vain Linux -käyttöjärjestelmällä)

#### Staattinen analyysi:
Komento `poetry run invoke lint` suorittaa .pylintrc -tiedostossa määrätyillä asetuksilla koodin staattisen analyysin ja antaa palautetta koodin laadusta. Testi- ja käyttöliittymähakemistot on jätetty analyysin ulkopuolelle.

### Kirjautuminen ja käyttäjän luominen:

Sovellus käynnistyy kirjautumisnäkymään

![](./kuvat/login_page.png)

Painamalla `click here to register` pääset luomaan uutta käyttäjää.

Aukeaa rekisteröitymisnäkymä:

![](./kuvat/register_page.png)

Syötä tarvittavat tiedot eli käyttäjänimi, salasana ja salasanan varmennus ja paina `register` niin sovellus luo uuden käyttäjän ja avaa päänäkymän.

![](./kuvat/main_page.png)

### Sovelluksen toimintoja:

#### Kirjan lisäys:

Täyttämällä kentät `title` ja `author` ja painamalla `submit` kirja lisätään kyseiselle käyttäjälle ja se ilmestyy alhaalla olevaan laatikkoon.

#### Kirjan poisto:

Valitsemalla kirjojen listasta kirja ja painamalla `delete` painiketta kirja kysytään vielä vahvistus poistosta, ja sitten kirja poistetaan.

#### Suodattaminen:

Näytettävien kirjojen listaa voi suodattaa painamalla `sort by` painiketta ja valitsemalla haluamasi tapa suodattaa kirjat.
