*.py linguist-detectable=true

def binerysearch(array, choise):
    low = 0
    high = len(array) - 1

    while True:
        main = (low + high) // 2

        if choise == array[main]:
            print(main)
            break

        elif choise > array[main]:
            low = main + 1

        elif choise < array[main]:
            high = main - 1


array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

while True:
    try:
        choice = int(input("Enter the number: "))
        break

    except (ValueError ,TypeError):
        print("Invalid input ,you can just enter integer")
    except Exception:
        print("try again")

binerysearch(array, choice)
