
def rol(value, n):
    print("Original number:", format(value, '08b'))

    for i in range(n):
        msb = (value >> 7) & 1
        value = ((value << 1) | msb) & 255
        print("Step", i + 1, ":", format(value, '08b'))

    print("Final result:", format(value, '08b'))
    print()

def rcl(value, carry, n):
    print("Original number:", format(value, '08b'))
    print("Initial carry:", carry)

    for i in range(n):
        msb = (value >> 7) & 1
        value = ((value << 1) | carry) & 255
        carry = msb
        print("Step", i + 1, ":", format(value, '08b'),
              "Carry:", carry)

    print("Final result:", format(value, '08b'))
    print("Final carry:", carry)

value = int('10110110', 2)

print("a) Rotate Left Without Carry (ROL)")
rol(value, 2)

print("b) Rotate Left With Carry (RCL)")
rcl(value, 0, 2)
