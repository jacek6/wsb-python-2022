

## Powtórka

Program lista rzeczy do zrobienia. Program ma oferować opcje:
 - Dodaj rzecz do zrobienia
 - Oznacz rzecz jako zrobioną
 - Pokaż rzeczy do zrobienia i zrobione
 - Usuń rzecz do zrobienia
 - Ustaw konkretną rzecz na początek
 - Wyjdź z programu

Można bazować na szkielecie programu:
plik(`powrtork_szkielet.py`)

Działająca prosta wersja:
plik(`program_bez_klasy`)

### Przerabianie na klasę
Jak wygląda zwykła funkcja:
```python
def oznacz_rzecz_jako_zrobiona(lista, zbior_rzeczy_zrobionych):
    for i, element in enumerate(lista):
        print(f'{i+1}. {element}')
    indeks_do_oznaczenia = int(input('Ktory element oznaczyć: ')) - 1
    zbior_rzeczy_zrobionych.add(lista[indeks_do_oznaczenia])
```

Jak wygląda funkcja w klasie:
```python
    def oznacz_rzecz_jako_zrobiona(self):
        for i, element in enumerate(self.lista):
            print(f'{i+1}. {element}')
        indeks_do_oznaczenia = int(input('Ktory element oznaczyć: ')) - 1
        self.zbior_rzeczy_zrobionych.add(self.lista[indeks_do_oznaczenia])
```

Wersja przerobiona na używanie klasy:
plik(`program_z_prosta_klasa.py`)

Dodanie do init argumentu:
plik(`program_z_prosta_klasa2`)

Dwie instacje klasy:
plik(`program_z_prosta_klasa3`)

Zdanie:
 - po zmienie koloru listy napisz na jaki kolor lista została zmieniona
 - pozwól na pisanie czerwona lista z małej litery przy wyborze

Dwa kody które robią to samo:

```python
odp = str.lower(input('Na którą listę chcesz zmienić? ([N]iebieska, Czerwona): '))

odp = (input('Na której liście chcesz operować? ([N]iebieska, Czerwona):').lower())

```




plik(`jak_jest_podawany_self`)

plik(`program_z_prosta_klasa4`)

zadanie: 

stwórz klasę TrojkatnaListaRzeczy do zrobienia, która jest klasą dziecko naczej początkowej klasy

lista niebieska ma być instacją tej klasy

zadanie:
do klasy zakazane rzeczy do zrobienia, zmień działanie dodaj rzeczy do zrobienia, aby dodana rzeczy do zrobienia miała sufix " - ale nie wolno", wykorzystując super wywołanie

plik(`program_z_prosta_klasa5`)


plik(`przyklad_pygame1`)
plik(`przyklad_pygame2`)
plik(`przyklad_pygame3.py`)
plik(`przyklad_pygame4`)
plik(`przyklad_pygame5`)
plik(`przyklad_pygame5_z_klasa`)

