def print_as_matrix(matrix):
    for i in range(len(matrix)):
        print("[ ", end="")
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
        print("]")
    print("\n")


m = [
    [float("inf"), 5, 4, 6, 6],
    [8, float("inf"), 5, 3, 4],
    [4, 3, float("inf"), 3, 1],
    [8, 2, 5, float("inf"), 6],
    [2, 2, 7, 0, float("inf")],
]
