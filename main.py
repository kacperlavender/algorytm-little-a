import heapq
from copy import deepcopy

from krok4 import czyKZ1, czyKZ2, czyKZ3
from m import m, print_as_matrix
from pp2 import zabronienie
from pp_first import podzial_P_na_PP
from redukcja import redukcja
from wycznaczanie import krok_2


def zbuduj_trase(luki, n):
    nast = {a: b for a, b in luki}
    x = 0
    trasa = [x]
    for _ in range(n - 1):
        x = nast[x]
        trasa.append(x)
    trasa.append(trasa[0])
    return trasa


def koszt_z_lukow(luki, macierz):
    return sum(macierz[a][b] for a, b in luki)


def tworzy_podcykl(luki, nowy, n):
    wszystkie = luki + [nowy]
    nast, poprz = {}, {}
    for a, b in wszystkie:
        if a in nast or b in poprz:
            return True
        nast[a] = b
        poprz[b] = a
    start, cel = nowy
    x, dl = cel, 1
    while x in nast:
        x = nast[x]
        dl += 1
        if x == start:
            return dl < n
    return False


def usun_wiersz_kolumne(macierz, akt_w, akt_k, i_star, j_star):
    ii = akt_w.index(i_star)
    jj = akt_k.index(j_star)
    nowa = [
        [macierz[i][j] for j in range(len(akt_k)) if j != jj]
        for i in range(len(akt_w))
        if i != ii
    ]
    return nowa, [r for r in akt_w if r != i_star], [c for c in akt_k if c != j_star]


def little(macierz_wejsciowa):
    n = len(macierz_wejsciowa)
    m0, lb0 = redukcja(deepcopy(macierz_wejsciowa))

    print("Macierz po redukcji startowej:")
    print_as_matrix(m0)
    print(f"LB startowe = {lb0}\n")

    najlepsza_luki, najlepszy_koszt = None, float("inf")
    licznik = 0
    kolejka = [(lb0, licznik, m0, list(range(n)), list(range(n)), [])]

    while kolejka:
        lb, _, macierz, akt_w, akt_k, wybrane = heapq.heappop(kolejka)

        if czyKZ2(lb, najlepszy_koszt):
            print("KZ2 - odciecie przez ograniczenie")
            continue

        if czyKZ1(macierz):
            print("KZ1 - podproblem niedopuszczalny")
            continue
        # kompletna trasa
        if czyKZ3(wybrane, n):
            wszystkie = wybrane + [(akt_w[0], akt_k[0])]
            koszt = koszt_z_lukow(wszystkie, macierz_wejsciowa)

            if koszt < najlepszy_koszt:
                najlepszy_koszt = koszt
                najlepsza_luki = wszystkie
                print(
                    f"Nowa najlepsza trasa (koszt={koszt}): {zbuduj_trase(wszystkie, n)}"
                )
            continue

        idx_i, idx_j = krok_2(macierz)
        i_star, j_star = akt_w[idx_i], akt_k[idx_j]
        print(f"Wybrano łuk ({i_star}→{j_star})  |  LB={lb}  |  wybrane={wybrane}")

        # P+ – włącz łuk
        if not tworzy_podcykl(wybrane, (i_star, j_star), n):
            m_plus, _ = podzial_P_na_PP(macierz, idx_i, idx_j, wybrane_luki=[])
            m_plus, nowe_w, nowe_k = usun_wiersz_kolumne(
                m_plus, akt_w, akt_k, i_star, j_star
            )
            if j_star in nowe_w and i_star in nowe_k:
                m_plus[nowe_w.index(j_star)][nowe_k.index(i_star)] = float("inf")
            m_plus, red = redukcja(m_plus)
            lb_plus = lb + red
            if lb_plus < najlepszy_koszt:
                licznik += 1
                heapq.heappush(
                    kolejka,
                    (
                        lb_plus,
                        licznik,
                        m_plus,
                        nowe_w,
                        nowe_k,
                        wybrane + [(i_star, j_star)],
                    ),
                )

        # P− – zabroń łuk
        m_minus, wynik = zabronienie(macierz, idx_i, idx_j)
        red = wynik[1] if isinstance(wynik, tuple) else wynik
        lb_minus = lb + red
        if lb_minus < najlepszy_koszt:
            licznik += 1
            heapq.heappush(
                kolejka, (lb_minus, licznik, m_minus, akt_w[:], akt_k[:], wybrane[:])
            )

    return najlepsza_luki, najlepszy_koszt


if __name__ == "__main__":
    print("=== Algorytm Little'a ===\n")
    print_as_matrix(m)
    print()

    luki, koszt = little(m)

    print("\n=== WYNIK ===")
    if luki:
        n = len(m)
        print(f"Optymalny koszt : {koszt}")
        print(f"Łuki            : {sorted(luki)}")
        print(f"Trasa           : {' → '.join(str(v) for v in zbuduj_trase(luki, n))}")
    else:
        print("Nie znaleziono trasy.")
