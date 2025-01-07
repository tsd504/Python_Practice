
def remainder(value, divisor):
    return value % divisor

def main():
    while True:
        try:
            num1 = float(input("Enter the first value: "))
            print(remainder(num1, float(input("Enter the second number: "))))
            break    
        except ValueError:
            print("Invalid value.")

if __name__ == "__main__":
    main()