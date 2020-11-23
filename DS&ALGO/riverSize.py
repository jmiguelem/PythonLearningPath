def riverSizes(matrix):
    marked = set()
    riversLength = []

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 1 and (row,col) not in marked:
                currentLen = 1
                marked.add((row,col))
                stack = [(row,col)]

                while stack:
                    current = stack.pop()
                    neighbors = get_neighbours(current,matrix)
                    for n in neighbors:
                        y,x = n
                        if matrix[y][x] == 1 and (y,x) not in marked:
                            marked.add((y,x))
                            currentLen += 1
                            stack.append((y,x))
                riversLength.append(currentLen)

    return riversLength

def get_neighbours(pos, matrix):
    y, x = pos
    ns = []
    if x >= 1:
        ns.append((y,x-1))
    if x < len(matrix[0]) - 1:
        ns.append((y,x+1))
    if y < len(matrix) -1:
        ns.append((y+1,x))
    if y >= 1:
        ns.append((y,x+1))

    return ns

matrix =[
    [1,0,0,0,0,0,1],
    [0,1,0,0,0,1,0],
    [0,0,1,0,1,0,0],
    [0,0,1,0,1,0,0],
    [0,0,1,1,0,0,0]
    ]
expected = riverSizes(matrix)
print(expected)