n = int(input("Enter number of rows: "))
for i in range(1, n + 1):      #nos in one row
    for j in range(1, i + 1):  # nos in the row
        print(j, end=" ")
    print()
