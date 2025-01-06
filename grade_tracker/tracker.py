def main():
    grades = input('Enter grades separated by spaces: ').split()
    grades = [int(grade) for grade in grades]

    print('Menu:')
    print('1. Add grades')
    print('2. Remove grades')
    print('3. View grades and statistics')
    print('4. Exit')

    while True:
        choice = input('Enter your choice: ')

        if choice in ('1','2','3'):
            if choice == '1':
                new_grades = input('Enter new grades separated by spaces: ').split()
                grades.extend([int(grade) for grade in new_grades])
                print(f'Updated grades: {grades}')
            if choice == '2':
                remove_grade = input('Enter the grade to remove: ')
                try:
                    grades.remove(int(remove_grade))
                except ValueError:
                    print('Value not in list.')
            if choice == '3':
                if grades:
                    print(f'Current grades: {grades}')
                    print(f'Highest grade: {max(grades)}')
                    print(f'Lowest grade: {min(grades)}')
                    print(f'Average grade: {sum(grades)/len(grades)}')
                else:
                    print('List is empty.')
        elif choice == '4':
            break
        else:
            print('Invalid input')

main()