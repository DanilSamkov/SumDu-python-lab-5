# Функція для зчитування масиву з клавіатури
def input_array():
    while True:
        try:
            n = int(input("Введіть довжину масиву: "))
            if n <= 0:
                print("Довжина масиву повинна бути додатнім числом.")
                continue
            break
        except ValueError:
            print("Будь ласка, введіть ціле число.")

    array = []
    print("Введіть елементи масиву (достовірні дійсні числа):")
    for i in range(n):
        while True:
            try:
                element = int(input(f"Елемент {i + 1}: "))
                array.append(element)
                break
            except ValueError:
                print("Будь ласка, введіть дійсне число.")

    return array

# Функція для виведення початкового масиву
def print_array(array):
    print("Введений масив:", " ".join(map(str, array)))

# Функція для виведення додатніх елементів у зворотному порядку
def print_pos_elem_rev(array):
    positive_elements = [x for x in array if x > 0]
    positive_elements.reverse()

    if positive_elements:
        print("Додатні елементи у зворотному порядку:", " ".join(map(str, positive_elements)))
    else:
        print("У масиві немає додатніх елементів.")


def main():
    while True:
        array = input_array()
        print_array(array)
        print_pos_elem_rev(array)

        repeat = input("Бажаєте повторити? (y/n): ").strip().lower()
        if repeat != 'y':
            break

if __name__ == "__main__":
    main()