# Функция get_matrix с тремя параметрами n, m и value, которая создает матрицу
# (вложенный список) размерами n строк и m столбцов, заполненную значениями value
# и возвращает эту матрицу в качестве результата работы
def get_matrix(n, m, value):
    matrix = list()
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(j)
            matrix[i][j] = value
    return matrix

result1 = get_matrix(2, 2, 10)
print(result1)
result2 = get_matrix(3, 5, 42)
print(result2)
result3 = get_matrix(2, 4, 13)
print(result3)