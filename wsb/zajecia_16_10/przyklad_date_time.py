import datetime
import time

#wyciągnięcie daty
today = datetime.date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("date1 =", d1)

# tekstowo miesiac, potem dzień i rok
d2 = today.strftime("%B %d, %Y")
print("date2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("date3 =", d3)

# tekstowo skrócony miesiac, potem dzień i rok
d4 = today.strftime("%b-%d-%Y")
print("date4 =", d4)

#wyciągnięcie godziny i daty
now = datetime.datetime.now()
timer = now.strftime('%H:%M:%S')
date = now.strftime('year = %Y,    month = %m,   day = %d')
print('Time now is : ', timer)
print('Date now is :', date)


#zadanie z różnymi nazwami
file = 'report.txt'

for i in range (4):
    now = datetime.datetime.now()
    timer = now.strftime('%H%M%S')
    file_name = file[:6] + timer + file[6:]
    print(file_name)
    time.sleep(1)
