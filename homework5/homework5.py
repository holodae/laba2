def get_number():
    for num in range(30):
        if num % 2 != 0:
            yield num

odd_numbers = list(get_number())

print("Первое нечетное число:", odd_numbers[0])
print("Пятое нечетное число:", odd_numbers[4])
print("Последнее нечетное число:", odd_numbers[-1])
