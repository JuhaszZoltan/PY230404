nevek:list[str] = ['Richárd', 'Borbála', 'Zsuzsa', 'Balázs', 'Judit']

print('nevek:')
for nev in nevek:
    print(f'\t- {nev}')

magassagok:list[int] = []
for nev in nevek:
    m:int = int(input(f'{nev} magassága (cm): '))
    magassagok.append(m)

osszeg:int = 0
for mag in magassagok:
    osszeg += mag
atlag:float = round(osszeg / len(magassagok), 2)
print(f'átlagmagasság: {atlag} cm')



