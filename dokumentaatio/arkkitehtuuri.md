# Arkkitehtuurikuvaus sovellukselle

## Luokkakaavio rakenteelle

```mermaid
classDiagram
  LoginPage "1" -- "*" Eri_Nakymat
  RegisterPage "1" -- "*" Eri_Nakymat
  LoginPage "1" -- "1" UserService
  UserService "1" -- "1" UserRepository
  RegisterPage "1" -- "1" UserService
  UI "1" -- "*" Eri_Nakymat
  MainView "1" -- "*" Eri_Nakymat
  MainView "1" -- "1" BookService
  BookService "1" -- "1" BookRepository
  BookService "1" -- "1" BookEntity
  BookEntity "1" -- "1" BookRepository
```

### Rakenteen kuvailu:

Sovellus käyttää Repository -suunnittelumallia, jossa Repository -luokka vastaa tietojen pysyväistallennuksesta, Service -luokka pääasiallisesti sovelluslogiikasta ja UI -luokka eri käyttäjälle näytettävistä graafisista komponenteista. Käyttäjiin liittyvä sovelluslogiikka ja pysyväistallennus on UserService ja UserRepository luokissa, kun taas kirjoihin liittyvä BookService ja BookRepository luokissa.

## Päätoiminnallisuudet:

Kuvataan sovelluksen eri toimintoja sekvenssimallin avulla.

### Kirjojen näyttäminen:

Kun käyttäjä rekisteröityy tai kirjautuu, päänäkymästä vastaava MainView kutsuu BookService luokan metodia, joka noutaa tietokannasta kaikki käyttäjän kirjat ja MainView näyttää ne käyttäjälle.

```mermaid
sequenceDiagram
    Actor User
    User->>MainView: User launches the app
    MainView->>BookService: all_books('username')
    BookService->>BookRepository: find_all('username')
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

### Kirjautuminen ja rekisteröityminen

#### Käyttäjän luonti

```mermaid
sequenceDiagram
    RegisterPage ->> UserService: register_user('username', 'password')
    UserService ->> UserRepository: create_user('username', 'password')
    UserRepository -->> UserService: True if succeeds, else False
    UserService -->> RegisterPage: Response from UserRepository
```

#### Kirjautuminen
```mermaid
sequenceDiagram
    LoginPage ->> UserService: check_login_credentials('username', 'password')
    UserService ->> UserRepository: user_exists('username', 'password')
    UserRepository -->> UserService: True if succeeds, else False
    User -->> LoginPage: Response from UserRepository
```

### Tietojen pysyväistallennus:

Tiedon pysyväistallennuksesta vastaavat luokat `UserRepository` ja `BookRepository`. Ne käyttävät tietokantaa, joka luodaan `initialize_database` tiedostossa. Tietokannan nimi määritetään `.env` tiedostossa. Tarkemmat ohjeet löytyvät `README.md` tiedostosta.
