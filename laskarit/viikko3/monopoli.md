```mermaid
 classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli
    Ruutu "1" -- "1" Ruudun tyyppi
    Monopolipeli "1" -- "1" Aloitusruutu
    Monopolipeli "1" -- "1" Vankila
    Ruudun tyyppi "1" -- "1" Vankila
    Ruudun tyyppi "1" -- "1" Aloitusruutu
    Ruudun tyyppi "1" -- "*" Sattuma ja yhteismaa
    Ruudun tyyppi "1" -- "*" Asemat ja laitokset
    Ruudun tyyppi "1" -- "*" Normaalit kadut
    Ruutu "1" -- "1" Toiminto
    Normaalit kadut "1" -- "1" Nimi
    Sattuma ja yhteismaa "1" -- "*" toiminto
    Pelaaja "2...8" -- "*" Rahaa
    Normaalit kadut "1" -- "1..4" Talo
    Normaalit kadut "1" -- "0...1" Hotelli
    Pelaaja "1" -- "*" Normaalit kadut
```
