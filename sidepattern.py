def decreasing_right_pyramid(rows):
    for i in range(rows, 0, -1):
        print(" " * (rows - i) + "*" * i)
rows = int(input("Enter the number of rows: "))
decreasing_right_pyramid(rows)