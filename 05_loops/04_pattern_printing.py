"""
LESSON 21: Pattern Printing Practice

This file contains various pattern printing exercises using loops.
Great practice for understanding nested loops!

Instructions:
1. Study each pattern
2. Understand the logic
3. Try modifying the patterns
"""


def print_section(title):
    """Print section header"""
    print("\n" + "=" * 40)
    print(f"  {title}")
    print("=" * 40 + "\n")


# ============================================
# PATTERN 1: Right Triangle (Stars)
# ============================================
print_section("PATTERN 1: Right Triangle")

n = 5
for i in range(1, n + 1):
    print("* " * i)


# ============================================
# PATTERN 2: Inverted Right Triangle
# ============================================
print_section("PATTERN 2: Inverted Right Triangle")

n = 5
for i in range(n, 0, -1):
    print("* " * i)


# ============================================
# PATTERN 3: Left-Aligned Triangle
# ============================================
print_section("PATTERN 3: Left-Aligned Triangle")

n = 5
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "* " * i
    print(spaces + stars)


# ============================================
# PATTERN 4: Pyramid
# ============================================
print_section("PATTERN 4: Pyramid")

n = 5
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "* " * i
    print(spaces + stars)


# ============================================
# PATTERN 5: Inverted Pyramid
# ============================================
print_section("PATTERN 5: Inverted Pyramid")

n = 5
for i in range(n, 0, -1):
    spaces = " " * (n - i)
    stars = "* " * i
    print(spaces + stars)


# ============================================
# PATTERN 6: Diamond
# ============================================
print_section("PATTERN 6: Diamond")

n = 5
# Upper half
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "* " * i
    print(spaces + stars)

# Lower half
for i in range(n - 1, 0, -1):
    spaces = " " * (n - i)
    stars = "* " * i
    print(spaces + stars)


# ============================================
# PATTERN 7: Number Triangle
# ============================================
print_section("PATTERN 7: Number Triangle")

n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# ============================================
# PATTERN 8: Repeating Number Triangle
# ============================================
print_section("PATTERN 8: Repeating Number Triangle")

n = 5
for i in range(1, n + 1):
    print(f"{i} " * i)


# ============================================
# PATTERN 9: Floyd's Triangle
# ============================================
print_section("PATTERN 9: Floyd's Triangle")

n = 5
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(f"{num:2}", end=" ")
        num += 1
    print()


# ============================================
# PATTERN 10: Pascal's Triangle (Simplified)
# ============================================
print_section("PATTERN 10: Pascal's Triangle")

n = 6
for i in range(n):
    # Print spaces for alignment
    print(" " * (n - i), end="")
    
    # Calculate and print values
    value = 1
    for j in range(i + 1):
        print(f"{value:3}", end=" ")
        value = value * (i - j) // (j + 1)
    print()


# ============================================
# PATTERN 11: Hollow Square
# ============================================
print_section("PATTERN 11: Hollow Square")

n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# ============================================
# PATTERN 12: Hollow Triangle
# ============================================
print_section("PATTERN 12: Hollow Triangle")

n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i == n or j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# ============================================
# PATTERN 13: Alphabet Triangle
# ============================================
print_section("PATTERN 13: Alphabet Triangle")

n = 5
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()


# ============================================
# PATTERN 14: Reverse Alphabet Triangle
# ============================================
print_section("PATTERN 14: Reverse Alphabet Triangle")

n = 5
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + i), end=" ")
    print()


# ============================================
# PATTERN 15: Butterfly
# ============================================
print_section("PATTERN 15: Butterfly Pattern")

n = 4

# Upper half
for i in range(1, n + 1):
    print("*" * i, end="")
    print(" " * (2 * (n - i)), end="")
    print("*" * i)

# Lower half
for i in range(n, 0, -1):
    print("*" * i, end="")
    print(" " * (2 * (n - i)), end="")
    print("*" * i)


# ============================================
# PATTERN 16: Sandglass
# ============================================
print_section("PATTERN 16: Sandglass Pattern")

n = 5

# Upper half
for i in range(n, 0, -1):
    spaces = " " * (n - i)
    stars = "* " * i
    print(spaces + stars)

# Lower half
for i in range(2, n + 1):
    spaces = " " * (n - i)
    stars = "* " * i
    print(spaces + stars)


# ============================================
# PATTERN 17: Multiplication Table
# ============================================
print_section("PATTERN 17: Multiplication Table (1-10)")

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end="")
    print()


# ============================================
# PATTERN 18: Checkerboard
# ============================================
print_section("PATTERN 18: Checkerboard")

n = 8
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print("■", end=" ")
        else:
            print("□", end=" ")
    print()


# ============================================
# PATTERN 19: Spiral Numbers (Simple)
# ============================================
print_section("PATTERN 19: Number Box")

n = 4
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{(i - 1) * n + j:3}", end="")
    print()


# ============================================
# PATTERN 20: Heart (ASCII Art)
# ============================================
print_section("PATTERN 20: Heart Pattern")

heart = [
    "  **   **  ",
    " **** **** ",
    "***********",
    " ********* ",
    "  *******  ",
    "   *****   ",
    "    ***    ",
    "     *     ",
]

for line in heart:
    print(line)


# ============================================
# PRACTICE CHALLENGES
# ============================================
print_section("PRACTICE CHALLENGES")

print("""
Try creating these patterns yourself:

1. Right triangle with numbers (1, 12, 123, ...)
2. Pyramid with numbers
3. Hollow diamond
4. Zigzag pattern
5. Arrow pointing right

Tips:
- Start with the outer loop (rows)
- Figure out what changes in each row
- Use inner loops for repetition
- Test with small n first
""")


# ============================================
# FUNCTION TEMPLATES
# ============================================
print_section("FUNCTION TEMPLATES")


def print_right_triangle(n, char="*"):
    """Print right triangle pattern"""
    for i in range(1, n + 1):
        print((char + " ") * i)


def print_pyramid(n, char="*"):
    """Print pyramid pattern"""
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        symbols = (char + " ") * i
        print(spaces + symbols)


def print_diamond(n, char="*"):
    """Print diamond pattern"""
    # Upper half
    for i in range(1, n + 1):
        print(" " * (n - i) + (char + " ") * i)
    # Lower half
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + (char + " ") * i)


# Demonstrate functions
print("Using print_right_triangle(4, '#'):")
print_right_triangle(4, "#")

print("\nUsing print_pyramid(4, '@'):")
print_pyramid(4, "@")

print("\nUsing print_diamond(3, '+'):")
print_diamond(3, "+")


print("\n" + "=" * 40)
print("  END OF PATTERN PRACTICE")
print("=" * 40)
