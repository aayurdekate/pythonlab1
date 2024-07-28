# (5) Write a Python program to print all the even numbers and their squares
# within the given range.
# (a) range(1,50)
# (b) range(1,100)

def print_even_squares(start, end):

  for num in range(start, end):
    if num % 2 == 0:
      square = num ** 2
      print(f"Even number: {num}, Square: {square}")


print("Range (1, 50):")
print_even_squares(1, 50)

print("\nRange (1, 100):")
print_even_squares(1, 100)
