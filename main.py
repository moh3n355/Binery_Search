def binary_search(array, choice):
    low = 0
    high = len(array) - 1
    step = 0

    while low <= high:
        main = (low + high) // 2
        step += 1
        print(f"try{step}: check {array[main]} in the {array[low:high+1]}" )

        if choice == array[main]:
            return f"In the {step} try, found {choice} at index {main}.\n"

        elif choice > array[main]:
            print('failed \n')
            low = main + 1

        else:
            print('failed \n')
            high = main - 1

    return f"{choice} not found!\n"


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

while True:
    try:
        choice = int(input("Enter the number (or enter 00 to quit): "))
        if choice == 0:
            break
        else:
            print(binary_search(array, choice))

    except (ValueError, TypeError):
        print("Invalid input, please enter an integer.\n")
        
    except Exception:
        print("Try again.\n")
