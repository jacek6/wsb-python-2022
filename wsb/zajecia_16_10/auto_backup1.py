import datetime
import time

scizka = 'C:\\Users\\hp\\PycharmProjects\\pythonProject1\\wsb\\zajecia_16_10\\dane\\dane.txt'


sciezka_do_pliku = 'C:\\Users\\hp\\PycharmProjects\\pythonProject1\\wsb\\zajecia_16_10\\dane\dane.txt'

def odczytaj_plik():
    with open(sciezka_do_pliku, 'r') as fp:
        return fp.read()

def aktualny_timestamp():
    now = datetime.datetime.now()
    timer = now.strftime('%H%M%S')
    return timer

def wykonaj_kopie_zapasowa():
    nazwa_pliku_z_kopia = sciezka_do_pliku + aktualny_timestamp() + '.txt'
    print('wykonam kopie zapasowa ', nazwa_pliku_z_kopia)
    with open(nazwa_pliku_z_kopia, 'w') as fp:
        fp.write(odczytaj_plik())
    print('kopia zapasowa gotowa')

aktualna_zawartosc_pliku = odczytaj_plik()
print('aktualna_zawartosc_pliku = ', aktualna_zawartosc_pliku)
for i in range(100):
    najnowsza_zawartosc_pliku = odczytaj_plik()
    if najnowsza_zawartosc_pliku != aktualna_zawartosc_pliku:
        print('zauwazylem ze trzeba wykonac kopie zapasowa')
        wykonaj_kopie_zapasowa()
        aktualna_zawartosc_pliku = najnowsza_zawartosc_pliku
    time.sleep(2)