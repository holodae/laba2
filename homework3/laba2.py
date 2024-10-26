from datetime import datetime

def calculate_age(birthdate_str):
    
    try:
        birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")
        today = datetime.today()
        
    
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age

    except ValueError:
        return "Ошибка: Неверный формат даты. Пожалуйста, введите дату в формате дд/мм/гггг."

birthdate_input = input("Введите вашу дату рождения (дд/мм/гггг): ")
age = calculate_age(birthdate_input)
print(f"Ваш возраст: {age}")
