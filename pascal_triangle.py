def pascals_triangle(n):
    if n == 1:
        return [1]

    line = [1]
    prev_line = pascals_triangle(n-1)
    for i in range(len(prev_line) - 1):
        line.append(prev_line[i] + prev_line[i + 1])

    line.append(1)

    return line


print(pascals_triangle(5))
