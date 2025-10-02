def classify_triangle(a, b, c):
    """
    Classifies a triangle based on side lengths.

    Returns:
        - Equilateral
        - Isosceles
        - Scalene
        - Adds 'Right' if it is a right triangle
        - Returns 'Not a triangle' if invalid
    """
    # Validate triangle
    if a <= 0 or b <= 0 or c <= 0:
        return "Not a triangle"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"

    # Determine type
    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    # Check for right triangle
    sides = sorted([a, b, c])
    if abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-6:
        triangle_type += " Right"

    return triangle_type


# Example usage
if __name__ == "__main__":
    examples = [
        (3, 3, 3),
        (5, 5, 8),
        (4, 5, 6),
        (3, 4, 5),
        (1, 1, 2**0.5),
        (1, 2, 3),
        (-1, 2, 2)
    ]
    
    for sides in examples:
        print(f"Sides: {sides} -> {classify_triangle(*sides)}")

# triangle.py
with open("output.txt", "w") as f:
    examples = [
        (3, 3, 3),
        (5, 5, 8),
        (4, 5, 6),
        (3, 4, 5),
        (1, 1, 2**0.5),
        (1, 2, 3),
        (-1, 2, 2)
    ]
    
    for sides in examples:
        result = classify_triangle(*sides)
        f.write(f"Sides: {sides} -> {result}\n")
