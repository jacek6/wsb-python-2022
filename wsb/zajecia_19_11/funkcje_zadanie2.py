
def czy_mozna_uzywac_programu(nazwa_uztkownika: str, nr_licencji) -> bool:
    if not nazwa_uztkownika.endswith('@wsb.pl'):
        return False
    return nr_licencji % 3 == 0
    # if nr_licencji % 3 == 0:
    #     return True
    # else:
    #     return False

print(f"{czy_mozna_uzywac_programu('jacek@gmail.com', 3) = }")
print(f"{czy_mozna_uzywac_programu('jacek@wsb.pl', 3) = }")
print(f"{czy_mozna_uzywac_programu('jacek@wsb.pl', 31) = }")