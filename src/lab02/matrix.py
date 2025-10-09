def transpose(mat: list[list[float | int]]) -> list[list]:
    if mat == []: return []
    if any(len(mat[i])!=len(mat[0]) for i in range(len(mat))): return "ValueError"
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
# print(transpose([[1, 2, 3]]))
# print(transpose([[1], [2], [3]]))
# print(transpose([[1, 2], [3, 4]]))
# print(transpose([]))
# print(transpose([[1, 2], [3]]))
def row_sums(mat: list[list[float | int]]) -> list[list]:
    if any(len(mat[i])!=len(mat[0]) for i in range(len(mat))): return "ValueError"
    retlist = []
    for i in range(len(mat)):
        retlist.append(sum(mat[i]))
    return retlist
# print(row_sums([[1, 2, 3], [4, 5, 6]]))
# print(row_sums([[-1, 1], [10, -10]]))
# print(row_sums([[0, 0], [0, 0]]))
# print(row_sums([[1, 2], [3]]))
def col_sums(mat: list[list[float | int]]) -> list[list]:
    if any(len(mat[i])!=len(mat[0]) for i in range(len(mat))): return "ValueError"
    retlist = []
    for i in range(len(mat[0])):
        retlist.append(0)
        for j in range(len(mat)):
            retlist[i]+=mat[j][i]
    return retlist
# print(col_sums([[1, 2, 3], [4, 5, 6]]))
# print(col_sums([[-1, 1], [10, -10]]))
# print(col_sums([[0, 0], [0, 0]]))
# print(col_sums([[1, 2], [3]]))