def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def main():
    import sys
    if len(sys.argv) != 3:
        print(f"Multiply Usage : {sys.argv[0]} <num1> <num2>", file=sys.stderr)
        sys.exit(0)
    
    num1, num2 = map(float, sys.argv[1:])
    print(f"The product of {num1} and {num2} is {multiply(num1, num2)}")

if __name__ == "__main__":
    main()

