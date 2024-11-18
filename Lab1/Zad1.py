#Zdanie z paczkami
def podziel(wagi,max_waga):
    for waga in wagi:
        if waga>max_waga:
            raise ValueError[f"Paczka o wadze {waga} przekracza dozwoloną wage kursu {max_waga}kg"]
            #raise ValueError to wyswietlenie błedu na stosie

    wagi_sorted = sorted(wagi,reverse=True)
    kursy=[]
    for waga in wagi_sorted:
        dodano = False
        for kurs in kursy:
            if sum(kurs)+ waga <= max_waga:
                kurs.append(waga)
                dodano= True
                break
        if not dodano:
            kursy.append([waga])

    return len(kursy), kursy

wagi=[10,15,20,8,5,7]
max_waga=25
liczba_kursow, kursy = podziel(wagi,max_waga)
print(f'Liczba kursów: {liczba_kursow}')
for i, kurs in enumerate (kursy,1 ):
    print(f'Kurs {i} {kurs} - suma wag: {sum(kurs)} kg')


