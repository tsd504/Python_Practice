def main():

    while True:
        
        print("Simple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Divide")
        print("4. Multiply")
        print("5. Exit")

        choice = input("What would you like to do? ")

        if choice in ('1','2','3','4'):

            while True:
                try:
                    num1 = float(input('Enter the 1st number: '))
                    num2 = float(input('Enter the 2nd number: '))
                    break
                except ValueError:
                    print('Please enter a numerical value.')
            
            if choice == '1':
                print(f'{num1} + {num2} = {num1 + num2}')
            if choice == '2':
                print(f'{num1} - {num2} = {num1 - num2}')
            if choice == '3':
                if num2 == 0:
                    print("Can't divide by zero")
                else:
                    print(f'{num1} / {num2} = {num1 / num2}')
            if choice == '4':
                print(f'{num1} * {num2} = {num1 * num2}')    
                
        elif choice == '5':
            break
        else:
            print('Invalid choice')
    

main()