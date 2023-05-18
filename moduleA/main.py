def add(a, b):
    """Add two numbers."""
    return a + b

def main():
    import sys
    if len(sys.argv) != 3:
        print(f"Sum Usage :  {sys.argv[0]} <num1> <num2>", file=sys.stderr)
        sys.exit(0)
    
    num1, num2 = map(float, sys.argv[1:])
    print(f"The sum of {num1} and {num2} is {add(num1, num2)}")

if __name__ == "__main__":
    main()