from redukcja import redukcja

def krok_2(macierz: list[list[float]]) -> tuple[int, int] | None:
    n = len(macierz)
    max_koszt = -1
    najlepszy_odcinek = None

    for i in range(n):
        for j in range(n):
            if macierz[i][j] == 0:
                
                min_wiersz = float('inf')
                for k in range(n):
                    if k != j and macierz[i][k] < min_wiersz:
                        min_wiersz = macierz[i][k]
                        
                min_kolumna = float('inf')
                for l in range(n):
                    if l != i and macierz[l][j] < min_kolumna:
                        min_kolumna = macierz[l][j]
                        
                koszt = min_wiersz + min_kolumna
                
                if koszt > max_koszt:
                    max_koszt = koszt
                    najlepszy_odcinek = (i, j)
                    
    return najlepszy_odcinek