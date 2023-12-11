def find_saddle_point(matrix):
    for i, row in enumerate(matrix):
        max_in_row = max(row)
        max_index = row.index(max_in_row)
        column = [matrix[j][max_index] for j in range(len(matrix))]
        if max_in_row == min(column):
            return (i, max_index)
    return "none"

def main():
    rows, columns = map(int, input().split())
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)

    result = find_saddle_point(matrix)
    if result == "none":
        print(result)
    else:
        print(f"Saddle point found at coordinates: {result}")

if __name__ == "__main__":
    main()