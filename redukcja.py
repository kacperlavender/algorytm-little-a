"""def redukcja(macierz):
    suma_redukcji = 0

    # redukcja wierszy
    for i in range(len(macierz)):
        min_wiersz = min(macierz[i])
        suma_redukcji += min_wiersz

        for j in range(len(macierz[i])):
            macierz[i][j] -= min_wiersz

    # redukcja kolumn
    for j in range(len(macierz[0])):
        min_kol = min(macierz[i][j] for i in range(len(macierz)))
        suma_redukcji += min_kol

        for i in range(len(macierz)):
            macierz[i][j] -= min_kol

    return macierz, suma_redukcji"""

#Zmienilem bo cos z nan sie wypierdalalo

def redukcja(macierz):
    suma_redukcji = 0

    # redukcja wierszy
    for i in range(len(macierz)):
        min_wiersz = min((v for v in macierz[i] if v != float('inf')), default=float('inf'))
        if min_wiersz == float('inf'):
            return macierz, float('inf')
        suma_redukcji += min_wiersz
        for j in range(len(macierz[i])):
            if macierz[i][j] != float('inf'):
                macierz[i][j] -= min_wiersz

    # redukcja kolumn
    for j in range(len(macierz[0])):
        min_kol = min((macierz[i][j] for i in range(len(macierz)) if macierz[i][j] != float('inf')), default=float('inf'))
        if min_kol == float('inf'):
            return macierz, float('inf')
        suma_redukcji += min_kol
        for i in range(len(macierz)):
            if macierz[i][j] != float('inf'):
                macierz[i][j] -= min_kol

    return macierz, suma_redukcji