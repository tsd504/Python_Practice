def increment_by(value,increment):
    return value + increment

def main():
    while True:
        try:
            value = float(input('Enter the value to increment: '))
            break
        except ValueError:
            print('Invalid value')
    
    print(increment_by(value,1))

if __name__ == "__main__":
    main()