M = [[1, 10, 2, 0, 0, 2, 2, 2, 2, 100],
     [100, 0, 0, 30, 2, 2, 2, 2, 2, 5],
     [0, 10, 4, 0, 2, 2, 2, 2, 2, 0],
     [1, 0, 2, 20, 0, 0, 0, 0, 0, 4]]

# M=[[1],[0]]

rows = len(M)
cols = len(M[0])


def pretty_print_2D(M):
    lens = [cols for i in range(0, cols)]
    fmt = ''.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in M]
    print('\n'.join(table))


print('Origanal Matrix:')
pretty_print_2D(M)

################################################################################################

for r in range(1, rows):  ## we skip first row (row 0)

    for c in range(cols):

        # case 1 -  we are in the middle, not on an edge, so we have 3 incoming paths from top row
        if (c > 0 and c < cols - 1):
            previous_max = max(M[r - 1][c], M[r - 1][c - 1], M[r - 1][c + 1])  ## for case 1
            M[r][c] = M[r][c] + previous_max

        # case 2 - we are in the right edge, so we have 2 incoming paths from top row
        elif (c == cols - 1):
            previous_max = max(M[r - 1][c], M[r - 1][c - 1])  ## for case 1
            M[r][c] = M[r][c] + previous_max

        # case 3 - we are in the left edge, so we have 2 incoming paths from top row
        elif (c == 0):
            previous_max = max(M[r - 1][c], M[r - 1][c + 1])  ## for case 1
            M[r][c] = M[r][c] + previous_max

print('Modified Matrix:')
pretty_print_2D(M)
print('Largest path sum is', max(M[len(M) - 1]))
