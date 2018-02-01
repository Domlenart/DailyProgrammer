def make_pascal_triangle(rows, *coordinates):
    triangle = [[1], [1, 1]]
    for row in range(rows+1):
        new_row = []
        if row > 2:
            for i in range(row):
                if i == 0 or i == row-1:
                    new_row.append(1)
                else:
                    new_row.append(triangle[row-2][i-1] + triangle[row-2][i])
            triangle.append(new_row)
    x, y = coordinates
    print(triangle[x-1][y-1])
    print(triangle)

make_pascal_triangle(15, 5, 3)


