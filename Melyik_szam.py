
import random

print('Egy számot kell kitalálnod 1 és az általad megadott felső határéték között.')
felso_hatar = int(input('Add meg a határértéket! '))
szam = random.randint(1, felso_hatar)
#print(szam)


tipp = int(input('\nMelyik számra gondoltam? '))
szamlalo = 1
while tipp != szam:
    if tipp == -1:
        break
    elif tipp < szam:
        print('Sajnos nem talált!')
        print('Nagyobb számra gondoltam! ')
    else:
        print('Sajnos nem talált!')
        print('Kisebb számra gondoltam! ')
    tipp = int(input('\nMelyik számra gondoltam? (kilépés: -1) '))
    szamlalo = szamlalo + 1

if tipp == -1:
    print(f'Sajnálom! A kitalálandó szám a {szam} volt.')
else:
    print(f'Eltaláltad {szamlalo} próbálkozásból!')