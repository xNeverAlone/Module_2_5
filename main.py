def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        line = []
        for j in range(m):
            line.append(value)
        matrix.append(line)
    return matrix


a = get_matrix(3, 3, 888)
b = get_matrix(3, 3, 777)
c = get_matrix(3, 3, 666)
print(a)
print(b)
print(c)


