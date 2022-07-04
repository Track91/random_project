
def fibonacci_sequence():
    a = 0
    b = 1
    number = 0

    number_of_number = int(input('Combien de nombre à afficher ? : '))

    for i in range(number_of_number):
        print(number, end='; ')
        number = a + b
        b = a
        a = number


fibonacci_sequence()





