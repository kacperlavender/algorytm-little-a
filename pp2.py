from copy import deepcopy
from m import m, print_as_matrix
from redukcja import redukcja

def zabronienie(macierz, i_star, j_star):
    # kopia macierzy, żeby nie zepsuć oryginału
    m_p2 = deepcopy(macierz)

    # zabronienie łuku <i*, j*>
    m_p2[i_star][j_star] = float('inf')

    # wywołanie redukcji
    wzrost_lb = redukcja(m_p2)

    print(f"\nmacierz po zabronieniu <{i_star}, {j_star}> i redukcji:")
    print_as_matrix(m_p2)
    print(f"wzrost LB (koszt redukcji): {wzrost_lb}")
    
    return m_p2, wzrost_lb

if __name__ == '__main__':
    print_as_matrix(m)

    nowa_macierz, koszt = zabronienie(m, 0, 1)