def subtract(a, b):
    """Subtract two numbers."""
    return a - b

def main():
    import sys
    if len(sys.argv) != 3:
        print(f"Subtract Usage: {sys.argv[0]} <num1> <num2>", file=sys.stderr)
        sys.exit(0)
    
    num1, num2 = map(float, sys.argv[1:])
    print(f"The subtraction of {num1} from {num2} is {subtract(num1, num2)}")

if __name__ == "__main__":
    main()

