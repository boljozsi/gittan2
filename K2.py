import random

#1.Feladat:
print("1.feladat:")
dobas_db=int(input("Add meg a dobások számát:"))
#print(dobas_db)

#2.Feladat:
print("2.feladat:")
dobasok=[]
for i in range(0, dobas_db):
    dobas=random.randint(1,6)
    dobasok.append(dobas)
print("A dobások: ", dobasok)

#3. feladat:
print("3.feladat:")
osszeg=0
for i in dobasok:
    osszeg+=i
atlag=osszeg/dobas_db  #len(dobasok)
print(f'A játékos átlagosan {atlag:.2f} mezőt, összesen {osszeg} mezőt haladt előre.')

#4. feladat:
print("4.feladat:")
vanE=0
for i in dobasok:
    if i==6:
       vanE+=1
if vanE>0:
    print("Van benne hatos! Darabszáma:", vanE)
else:
    print("A játékos sajnos egy alkalommal sem dobott hatost.")

if 6  not in dobasok:
    print("A játékos sajnos egy alkalommal sem dobott hatost.")
else:
    vanE=0
    for i in dobasok:
        if i==6:
          vanE+=1
    print("Van benne hatos!", vanE) 

#5. feladat:
print("5.feladat:")
paros=0
for i in dobasok:
    if i%2==0:
        paros+=1
print(f"A játékos {paros} alkalommal dobott páros számot.")

#6. feladat:
print("6.feladat:")
kisebb=0
for i in range(0, len(dobasok)-1):
    if dobasok[i]>dobasok[i+1]:
        kisebb+=1

print(f"A játékos {kisebb} alkalommal dobott kevesebbet, mint előző körben")