import random

def rock_paper_scissors():
    choices = ["камень", "ножницы", "бумага"]
    
    user_choice = input("Выберите: камень, ножницы или бумага: ").lower()
    
    if user_choice not in choices:
        print("Неправильный выбор. Пожалуйста, выберите 'камень', 'ножницы' или 'бумага'.")
        return
    
   
    computer_choice = random.choice(choices)
    
    print(f"Вы выбрали: {user_choice}")
    print(f"Компьютер выбрал: {computer_choice}")
    
    
    if user_choice == computer_choice:
        print("Ничья!")
    elif (
        (user_choice == "камень" and computer_choice == "ножницы") or
        (user_choice == "ножницы" and computer_choice == "бумага") or
        (user_choice == "бумага" and computer_choice == "камень")
    ):
        print("Вы выиграли!")
    else:
        print("Компьютер выиграл!")


rock_paper_scissors()
