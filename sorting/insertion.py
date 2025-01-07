""" def insertion_sort(list):
    n = len(list)

    for i in range(1,n):
        print(f"Iteration: {i}")
        correct_index = i
        for j in range(i-1,-1,-1):
            if list[i] < list[j]:
                correct_index = j
            else:
                break
        list.insert(correct_index, list[i])
        list.pop(i+1)
        print(f"{list}")

def main():
    user_input = input("Enter a list: ")
    num_list = [int(x) for x in user_input.split(" ")]
    insertion_sort(num_list)

if __name__ == "__main__":
    main() """


def insertion_sort(list):
    n = len(list)

    for i in range(1,n):
        current_value = list[i]
        j = i-1

        while j>=0 and list[j] > current_value:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = current_value
        print(list)

def main():
    user_input = input("Enter a list: ")
    num_list = [int(x) for x in user_input.split(" ")]
    insertion_sort(num_list)

if __name__ == "__main__":
    main()
    