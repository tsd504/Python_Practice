""" def selection_sort(list):
    n = len(list)
    sorted = []

    for i in range(n):
        sorted.append(min(list))
        list.pop(list.index(min(list)))
    return sorted

def main():
    user_input = input("Enter a list: ")
    num_list = [int(x) for x in user_input.split(" ")]
    print(selection_sort(num_list))

if __name__ == "__main__":
    main() """

def selection_sort(list):
    n = len(list)
    
    for i in range(n-1):
        min_index = i
        
        for j in range(i+1,n):
            print(f"Compare {list[j]} with {list[min_index]}")
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
        print(f'Iteration: {i+1}')
        print(f"List = {list}")
        
    return list

def main():
    user_input = input("Enter a list: ")
    num_list = [int(x) for x in user_input.split(" ")]
    print(selection_sort(num_list))

if __name__ == "__main__":
    main()