"""
Module for classifying triangles based on side lengths.
"""


def classify_triangle(a, b, c):
    """
    Classify a triangle based on its side lengths.
    
    Args:
        a (float): First side length
        b (float): Second side length
        c (float): Third side length
    
    Returns:
        str: Triangle classification
    """
    # pylint: disable=invalid-name
    # Note: a, b, c are standard mathematical notation for triangle sides
    
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


def main():
    """
    Main function to demonstrate triangle classification with examples.
    """
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


def write_results_to_file():
    """
    Write triangle classification results to output.txt file.
    """
    examples = [
        (3, 3, 3),
        (5, 5, 8),
        (4, 5, 6),
        (3, 4, 5),
        (1, 1, 2**0.5),
        (1, 2, 3),
        (-1, 2, 2)
    ]
    
    with open("output.txt", "w", encoding="utf-8") as f:
        for sides in examples:
            result = classify_triangle(*sides)
            f.write(f"Sides: {sides} -> {result}\n")

# At the bottom of triangle.py, change:
if __name__ == "__main__":  # pragma: no cover
    main()
    write_results_to_file()    