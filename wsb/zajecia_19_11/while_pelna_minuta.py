import datetime
import time

while datetime.datetime.now().second < 50:
    print('Czekam na pełną mitutę')
    time.sleep(2)

print('Pełna minuta jest zaraz...')