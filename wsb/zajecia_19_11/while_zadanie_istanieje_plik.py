import os
import time

while not os.path.exists('plik.txt'):
    print('plik nie instnieje')
    time.sleep(2)

print('Plik instnieje')