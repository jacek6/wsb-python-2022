while True:  # pętla będzie się wykonywać,
    password = input('Wpisz haslo: ')  # aż do polecenia „break”
    if password == '123abc':
        print('Haslo przyjete')
        break
    else:
        print('Zle haslo, jeszcze raz')
