# Ініціалізація масиву 7x7 нулями
matrix = [[0] * 7 for _ in range(7)]

# Заповнення масиву
for i in range(7):
    for j in range(7 - i):
        matrix[6 - i][j + i] = 7 - j

# Виведення масиву на екран
for row in matrix:
    print(' '.join(map(str, row)))