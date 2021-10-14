for i in range(5):
    row = input()
    if "1" in row:
        row_num = i + 1
        column_num = row.index("1")/2+1
        break
print(int(abs(row_num - 3) + abs(column_num - 3)))

