## Testausdokumentti

Sovellusta on testattu automatisoiduilla yksikkötesteillä sekä hieman laajemmilla integraatiotesteillä SQLITE -tietokannan suhteen.

### Testauskattavuus:

![](/kuvat/coverage-report.png)

### Yksikkö- ja integraatiotestit:

BookService luokassa on sovelluksen pääasiallinen sovelluslogiikka ja sitä on testattu tiedostossa `book_service_test.py`. Luokalle on injektoitu `FakeBookRepository`, joka toimii vastaavasti kuin `BookRepository` käyttämättä kuitenkaan tietokantaa.

UserService luokka ei varsinaisesti tarjoa mitään toiminnallisuutta, joten sitä ei ole testattu.

#### Repository -luokat:

Sekä `UserRepository` että `BookRepository` luokat on testattu käyttäen testitietokantaa, joka on konfiguroitu `.env.test` tiedostossa. Konfiguroinnista lisätietoja `README.md` -tiedostossa.

### Järjestelmätestaus:

Kaikki vaatimusmäärittelyssä mainittu perustoiminnallisuus on mekaanisesti testattu ja todettu toimivaksi. Syötekentille on yritetty syöttäää virheellisiä tai puutteellisia tietoja, mutta sovellus vastaa niihin järkevin virheilmoituksin.
