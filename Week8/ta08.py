cols_and_rows = int(input('How many columns and rows do you want in your multiplication table? '))
for row in range(1, cols_and_rows + 1):
   for column in range(1, cols_and_rows + 1):
      if ((cols_and_rows * cols_and_rows) >= 100):
        print(f"{(row*column):3}", end=" ")
      else:
        print(f"{(row*column):2}", end=" ")
   print()
   
   