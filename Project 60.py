# Find rightmost set bit value
def rightmost_set_bit(n):
    return n & -n

# Find rightmost set bit position
def rightmost_set_bit_pos(n):
    position = 0
    while (n & 1) == 0:
        n >>= 1
        position += 1
    return position

# Test
n = int(input("Enter number: "))
print(f"Rightmost bit value: {rightmost_set_bit(n)}")
print(f"Rightmost bit position: {rightmost_set_bit_pos(n)}")