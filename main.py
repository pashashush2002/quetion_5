triangle = [list(map(int, x.split(','))) for x in input().strip("[[").strip("]]").split("],[")]  # Вводим треугольник в формате строки
triangle_end = [[triangle[0][0]]] # Массив для значений после перемещений
triangle_way = [[str([triangle[0][0]]).strip('[').strip(']')]] # Массив для записи пути треугольника
for i in range(len(triangle)-1):
    for j in range(len(triangle[i + 1])):
        if j == 0: # Слева
            triangle_end.append([triangle_end[i][j]+triangle[i + 1][j]])
            triangle_way.append([triangle_way[i][j] + "->" + str(triangle[i+1][j])])
        else:
            try:
                if triangle_end[i][j] < triangle_end[i][j - 1]: # Проверяем значения справа сверху и слева сверху. Выбираем наименьшее
                    trmin = triangle_end[i][j]
                    index = j
                else:
                    trmin = triangle_end[i][j - 1]
                    index = j - 1
                triangle_end[i + 1].append(triangle[i + 1][j]+trmin)
                triangle_way[i + 1].append(triangle_way[i][index] + "->" + str(triangle[i + 1][j]))
            except: # Справа
                triangle_end[i + 1].append(triangle[i + 1][j]+triangle_end[i][j - 1])
                triangle_way[i + 1].append(triangle_way[i][j - 1] + "->" + str(triangle[i + 1][j]))
for i in range(len(triangle_end[len(triangle_end) - 1])): # Ищем наименьшее
    if i == 0:
        min = triangle_end[len(triangle_end) - 1][0]
        index = 0
    else:
        if triangle_end[len(triangle_end) - 1][i] < min:
            min = triangle_end[len(triangle_end) - 1][i]
            index = i
print(f"Минимальный путь: {triangle_way[len(triangle_way) - 1][index]}")
print(f"Результат: {min}")
