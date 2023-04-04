#                      0          1          2        3          4
nevek:list[str] = ['Richárd', 'Borbála', 'Zsuzsa', 'Balázs', 'Judit']
#                      0          1         2          3        4
# magassagok    = [   192        172       151        182      163  ]

print('nevek:')
for nev in nevek:
    print(f'\t- {nev}')

magassagok:list[int] = []
for nev in nevek:
    m:int = int(input(f'{nev} magassága (cm): '))
    magassagok.append(m)

# osszeg:int = 0
# for mag in magassagok:
#     osszeg += mag
# atlag:float = round(osszeg / len(magassagok), 2)
# print(f'átlagmagasság: {atlag} cm')

atlag:float = sum(magassagok) / len(magassagok)
print(f'átlagmagasság: {atlag}')

# nevek.sort()

#                      0          1         2          3        4
# magassagok    = [   140        172       151        182      163  ]

# maxi = 3
# akti [, , , ]
maximum_index:int = 0
for index in range(1, len(nevek)):
    if magassagok[index] > magassagok[maximum_index]:
        maximum_index = index

print(f'a legmagasabb barátom {nevek[maximum_index]}')
print(f'ő {magassagok[maximum_index]} cm magas')

for i in range(0, len(nevek) - 1):
    for j in (range(i + 1, len(nevek))):
        if magassagok[j] < magassagok[i]:
            sm:int = magassagok[i]
            magassagok[i] = magassagok[j]
            magassagok[j] = sm
            sn:str = nevek[i]
            nevek[i] = nevek[j]
            nevek[j] = sn

print('magasság szerint növekvőbe: ')
for i in range(len(nevek)):
    print(f'{nevek[i]}: {magassagok[i]} cm')