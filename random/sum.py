
def sum(x,y):
    return x + y

def main():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid number")
    
    print(sum(num1,num2))

if __name__ == '__main__':
    main()

