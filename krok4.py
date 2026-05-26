from m import print_as_matrix


def __sprawdzWiersze(macierz):

    for row in macierz:
        czyINF = True
        for k in row:
            if k != float("inf"):
                czyINF = False
                break
        if czyINF:
            return True
    return False


def __transpose(macierz):
    r, c = len(macierz), len(macierz[0])
    transposed = [[0] * r for _ in range(c)]

    for i in range(r):
        for j in range(c):
            transposed[j][i] = macierz[i][j]

    return transposed


def czyKZ1(macierz):
    if __sprawdzWiersze(macierz):
        return True
    if __sprawdzWiersze(__transpose(macierz)):
        return True
    return False


def czyKZ2(lb_pp, v_star):
    return lb_pp >= v_star


def czyKZ3(wybrane_luki, n):
    return len(wybrane_luki) == n - 1


A = [
    [float("inf"), 5, 4, 6, 6],
    [8, float("inf"), 5, 3, 4],
    [4, 3, float("inf"), 3, 1],
    [8, 2, 5, float("inf"), 6],
    [2, 2, 7, 0, float("inf")],
]

if __name__ == "__main__":
    print_as_matrix(A)
    print(czyKZ1(A))
