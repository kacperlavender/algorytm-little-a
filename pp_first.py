from copy import deepcopy

def _zabron_podcyklu(macierz_pp, aktywne_wiersze, aktywne_kolumny, wybrane_luki, n_calkowite):
    nastepnik = {a: b for a, b in wybrane_luki}
    poprzednik = {b: a for a, b in wybrane_luki}

    odwiedzone_starty = set()

    for start in nastepnik:
        if start in odwiedzone_starty:
            continue

        x = start
        droga = [x]

        while x in nastepnik:
            x = nastepnik[x]
            if x in droga:
                break
            droga.append(x)

        for v in droga:
            odwiedzone_starty.add(v)

        if droga[0] in poprzednik:
            continue

        koniec = droga[-1]
        dlugosc_drogi = len(droga)

        if dlugosc_drogi < n_calkowite and koniec in aktywne_wiersze and droga[0] in aktywne_kolumny:
            i = aktywne_wiersze.index(koniec)
            j = aktywne_kolumny.index(droga[0])
            macierz_pp[i][j] = float('inf')


def podzial_P_na_PP(macierz_P, i_gwiazdka, j_gwiazdka, LB_P=0):
    
    wybrane_luki = []
    aktywne_wiersze = list(range(len(macierz_P)))
    aktywne_kolumny = list(range(len(macierz_P[0])))


    macierz_pp = deepcopy(macierz_P)

    idx_wiersz = aktywne_wiersze.index(i_gwiazdka)
    idx_kol = aktywne_kolumny.index(j_gwiazdka)

    for j in range(len(macierz_pp[idx_wiersz])):
        macierz_pp[idx_wiersz][j] = float('inf')
    for i in range(len(macierz_pp)):
        macierz_pp[i][idx_kol] = float('inf')

    aktywne_wiersze_pp = aktywne_wiersze[:]
    aktywne_kolumny_pp = aktywne_kolumny[:]

    wybrane_luki_pp = wybrane_luki + [(i_gwiazdka, j_gwiazdka)]

    _zabron_podcyklu(
        macierz_pp,
        aktywne_wiersze_pp,
        aktywne_kolumny_pp,
        wybrane_luki_pp,
        n_calkowite=len(aktywne_wiersze),
    )

    return  macierz_pp, wybrane_luki_pp


if __name__ == "__main__":
    macierz = [
        [float('inf'), 5, 4, 6, 6],
        [8, float('inf'), 5, 3, 4],
        [4, 3, float('inf'), 3, 1],
        [8, 2, 5, float('inf'), 6],
        [2, 2, 7, 0, float('inf')],
    ]

    macierz_po, wybrane_luki = podzial_P_na_PP(macierz_P=macierz,i_gwiazdka=2,j_gwiazdka=4)
    print("Wybrane luki:", wybrane_luki)
    print("Macierz PP:")
    for w in macierz_po:
        print(w)