import random

def find_multiples():
    try:
        x = int(input("Введите число X: "))
        if x == 0:
            return "Ошибка: X не может быть равен 0."
        
        numbers = [random.randint(0, 200) for _ in range(10)]

        multiples = list(filter(lambda num: num % x == 0, numbers))
        
        print("Сгенерированный список чисел:", numbers)
        print("Числа, кратные", x, ":", multiples)
    
    except ValueError:
        return "Ошибка: Введено некорректное значение, пожалуйста, введите целое число."

find_multiples()
