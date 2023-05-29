def search_element(matrix, element):
    rows = len(matrix)
    cols = len(matrix[0])
    i = 0
    j = cols - 1

    while i < rows and j >= 0:
        if matrix[i][j] == element:
            return (i + 1, j + 1)
        elif matrix[i][j] < element:
            i += 1
        else:
            j -= 1

    return None


matrix = [[1, 3, 5],
          [7, 9, 11],
          [13, 15, 17]]
element = 3
result = search_element(matrix, element)
print('Место элемента', element, 'в матрице:', result)

