
def czy_da_sie_mieszkac(metraz: float, wiek: float, typ_budunku: str) -> bool:
    if metraz < 20:
        return False
    if wiek > 100:
        return False
    if typ_budunku == 'rudera':
        return False
    return True

def ladne_wypisanie_czy_da_sie_mieszkac(metraz: float, wiek: float, typ_budunku: str):
    if czy_da_sie_mieszkac(metraz, wiek, typ_budunku):
        print('Stwierdzono, że da się mieszkać dla, metraz ', metraz, ', wiek ', wiek, ', typ_budunku ', typ_budunku)
    else:
        print('Stwierdzono, że NIE da się mieszkać dla, metraz ', metraz, ', wiek ', wiek, ', typ_budunku ', typ_budunku)

ladne_wypisanie_czy_da_sie_mieszkac(1, 6, 'blok')
ladne_wypisanie_czy_da_sie_mieszkac(100, 6, 'blok')

ladne_wypisanie_czy_da_sie_mieszkac(metraz=120, wiek=9, typ_budunku='blok')
ladne_wypisanie_czy_da_sie_mieszkac(metraz=120, wiek=9, typ_budunku='rudera')