
def binary(n):
    return format(n & 255, '08b')

def signed(n):
    return n if n < 128 else n - 256

def calculate(a, b, op):
    if op == '+':
        result = a + b
    else:
        result = a - b

    print("Operand 1:", binary(a))
    print("Operand 2:", binary(b))
    print("Operation:", op)
    print("Result in binary:", binary(result))
    print("Result in decimal:", signed(result))

    if result < -128 or result > 127:
        print("Arithmetic Overflow: Yes")
    else:
        print("Arithmetic Overflow: No")

    print()

print("a) 34 + (+27)")
calculate(34, 27, '+')

print("b) (-34) - (-27)")
calculate(-34, -27, '-')
