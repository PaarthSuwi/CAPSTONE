import math

def generate_pascals_triangle(n):
    triangle = []
    for row in range(n):
        current_row = [math.comb(row, col) for col in range(row + 1)]
        triangle.append(current_row)
    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)).center(len(triangle[-1]) * 3))

n = int(input("Enter the number of rows: "))
pascals_triangle = generate_pascals_triangle(n)
print_pascals_triangle(pascals_triangle)


n = 5
for i in range(n):
    row = []
    prev = row
    if i > 0:
        for j in range(1, i):
            row.append(prev[j-i-1]+prev[j])
        row.append(1)
    print(row)
    

                
                