
#Feladat 1
print('1. feladat')
fordulok_szama = int(input('Fordulók száma: ')) #fardulók számának a bekérése
#print(fordulok_szama+fordulok_szama)
#print(type(fordulok_szama))


print('\n2. feladat')
golkulonbsegek = []
for fordulo in range(0, fordulok_szama):
    aktualis_ertek = int(input(f'{fordulo+1}. fordulóban a gólkülönbség: '))
    golkulonbsegek.append(aktualis_ertek)


print('\n3. feladat')
gyozelmek = 0
veresegek = 0
dontelenek = 0
for golkulonbseg in golkulonbsegek:
    if golkulonbseg > 0:
        gyozelmek = gyozelmek + 1
    elif golkulonbseg < 0:
        veresegek = veresegek + 1
    else:
        dontelenek = dontelenek + 1
print('A szezonban a csapatnak',gyozelmek, 'győzelme,', veresegek, 'veresége', dontelenek, 'döntetlene volt.')


print('\n4. feladat')
osszpont=gyozelmek * 3 + dontelenek
print('A csapatnak a szezonban összesen:', osszpont, 'pontja lett!')


print('\n5. feladat')
if gyozelmek > dontelenek + veresegek:
    print('A csapatnak több győztes mérkőzése volt, mint veresége és döntelene együttvéve.')
else:
    print('A csapatnak nem volt több győztes mérközése, mint veresége és döntelene együttvéve.')

print('\n6. feladat')
sikerult = 0
for index in range(fordulok_szama-1):
    if 0 < golkulonbsegek[index]< golkulonbsegek[index + 1]: #0 < golkulonbsegek[index] and golkulonbsegek[index] < golkulonbsegek[index + 1]: 
        sikerult += 1
if sikerult:
    print(f'A kitűzött célt {sikerult} alkalommal sikerült elérnie a csapatnak.')
else:
    print('A kitűzött célt sajnos egyetlen alaklommal sem sikerült elérnie a csapatnak.')
    
