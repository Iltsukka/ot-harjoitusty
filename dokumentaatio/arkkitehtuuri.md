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
