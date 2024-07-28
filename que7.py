import math

# Function to calculate the area of a triangle using Heron's formula
def calculate_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Function to calculate percentage contribution of each triangle
def calculate_percentage(part, total):
    return (part / total) * 100

# Main function
def main():
    # Input: Reading the sides of the first triangle
    a1 = float(input("Enter the first side of the first triangle: "))
    b1 = float(input("Enter the second side of the first triangle: "))
    c1 = float(input("Enter the third side of the first triangle: "))

    # Calculating the area of the first triangle
    area1 = calculate_area(a1, b1, c1)
    print(f"Area of the first triangle: {area1:.2f}")

    # Input: Reading the sides of the second triangle
    a2 = float(input("Enter the first side of the second triangle: "))
    b2 = float(input("Enter the second side of the second triangle: "))
    c2 = float(input("Enter the third side of the second triangle: "))

    # Calculating the area of the second triangle
    area2 = calculate_area(a2, b2, c2)
    print(f"Area of the second triangle: {area2:.2f}")

    # Calculating the total area
    total_area = area1 + area2
    print(f"Total area enclosed by both triangles: {total_area:.2f}")

    # Calculating each triangle's contribution percentage
    percentage1 = calculate_percentage(area1, total_area)
    percentage2 = calculate_percentage(area2, total_area)

    print(f"Contribution of the first triangle: {percentage1:.2f}%")
    print(f"Contribution of the second triangle: {percentage2:.2f}%")

# Run the main function
if __name__ == "__main__":
    main()
