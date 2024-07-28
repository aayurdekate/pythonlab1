def alphabet_pyramid(n):
    for i in range(1, n + 1):
        line = "".join(chr(65 + j) for j in range(i))
        print(line)

def star_pyramid(n):
    for i in range(1, n + 1):
        print("*" * i)

def main():
    n = 5  
    print("Alphabet Pyramid:")
    alphabet_pyramid(n) 
    print("\nStar Pyramid:")
    star_pyramid(n)

if __name__ == "__main__":
    main()
