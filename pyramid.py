def increasing_left_pyramid(rows):
    for i in range(1, rows + 1):
        print("*" * i)

rows = int(input("Enter the number of rows: "))
increasing_left_pyramid(rows)
