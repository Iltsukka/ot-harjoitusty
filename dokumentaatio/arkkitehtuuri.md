# Arkkitehtuurikuvaus sovellukselle

## Luokkakaavio rakenteelle

```mermaid
classDiagram
  UI "1" --"*" Eri_Nakymat
  MainView "1" -- "*" Eri_Nakymat
  MainView "1" -- "1" BookService
  BookService "1" -- "1" BookRepository
  BookService "1" -- "1" BookEntity
  BookEntity "1" -- "1" BookRepository
```

### Rakenteen kuvailu:

Sovellus käyttää Repository -suunnittelumallia, jossa Repository -luokka vastaa tietojen pysyväistallennuksesta, Service -luokka pääasiallisesti sovelluslogiikasta ja UI -luokka eri käyttäjälle näytettävistä graafisista komponenteista.

## Päätoiminnallisuudet:

Kuvataan sovelluksen eri toimintoja sekvenssimallin avulla.

### Kirjojen näyttäminen:

Kun sovellus käynnistetään, päänäkymästä vastaava MainView kutsuu BookService luokan metodia, joka noutaa tietokannasta kaikki kirjat ja MainView näyttää ne käyttäjälle.

```mermaid
sequenceDiagram
    Actor User
    User->>MainView: User launches the app
    MainView->>BookService: all_books()
    BookService->>BookRepository: find_all()
    BookRepository->>BookEntity: Create Book -objects
    BookEntity-->>BookRepository: Books as objects
    BookRepository-->> BookService: Books
    BookService-->>MainView: Books
    MainView-->>User: User sees the books if there are any
```

### Kirjan lisääminen:

Lisääminen tapahtuu vastaavalla tavalla, ja MainView saa kirja-olion, jonka se lisää kirjojen listanäkymään.

```mermaid
sequenceDiagram
    Actor User
    User->>MainView: User creates a book
    MainView->>BookService: create_book('title', 'author')
    BookService->>BookRepository: add_book('title', 'author')
    BookRepository->>BookEntity: Create book -object
    BookEntity-->>BookRepository: Book
    BookRepository-->>BookService: Book
    BookService-->>MainView: Book
    MainView-->>User: Book is shown to the user
```

