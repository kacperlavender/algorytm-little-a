def krok_2(macierz_zredukowana):

    n = len(macierz_zredukowana)
    max_koszt = -1
    najlepszy_odcinek = None
    
    koszty_zer = {}

    for i in range(n):
        for j in range(n):
            if macierz_zredukowana[i][j] == 0:
                min_wiersz = float('inf')
                for k in range(n):
                    if k != j and macierz_zredukowana[i][k] < min_wiersz:
                        min_wiersz = macierz_zredukowana[i][k]
                        
                min_kolumna = float('inf')
                for l in range(n):
                    if l != i and macierz_zredukowana[l][j] < min_kolumna:
                        min_kolumna = macierz_zredukowana[l][j]
                        
                koszt = min_wiersz + min_kolumna
                koszty_zer[(i, j)] = koszt
                
                if koszt > max_koszt:
                    max_koszt = koszt
                    najlepszy_odcinek = (i, j)
                    
    return najlepszy_odcinek




inf = float('inf')

macierz_zredukowana = [
    [inf, 1,   0,   2,   2],  
    [3,   inf, 2,   0,   1],  
    [1,   2,   inf, 2,   0], 
    [4,   0,   3,   inf, 4],  
    [0,   2,   7,   0,   inf]  
]


