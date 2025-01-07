def bubble(list):
    n = len(list)

    for i in range(n-1):

        swapped = False

        for j in range(0, n-1-i):
            print(f'{i}:{list[j]}:{list[j+1]}')
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                swapped = True
        print(f'Iteration: {i+1} = {list}')
        if swapped == False:
            break
    

def main():
    user_input = input("Enter a list: ")
    num_list = [int(x) for x in user_input.split(' ')]
    print(type(num_list))
    print(num_list)

    bubble(num_list)

if __name__ == "__main__":
    main()