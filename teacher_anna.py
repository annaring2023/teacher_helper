import random
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)
from math_attention import math_attention

# головна функція


def operations():
    while True:
        try:
            operation = int(input(
                f"{Fore.WHITE}{Back.WHITE}\n1 - розподілити на команди\n2 - похвала для учня\n3 - хто йде до дошки?\n4 - створити похвалу для учня\n6 - вийти\nВаш вибір: "))
        except ValueError:
            print(f"{Fore.RED}Введіть число: ")
            continue

        if operation == 1:
            create_teams()
        elif operation == 2:
            create_congrats()
        elif operation == 3:
            single_students()
        elif operation == 4:
            new_note()
        elif operation == 7:
            while True:
                try:    
                    choice2 = int(input(
                    f"{Fore.WHITE}{Back.WHITE}\n1 - Додавання\n2 - Віднімання\n3 - Множення\n4 - Ділення\n5 - Повернутись\nВаш вибір: "))
                except ValueError:
                    print(f"{Fore.RED}Введіть число: ")
                    continue

                if choice2 == 1:
                    create_teams()
                elif choice2 == 2:
                    math_attention()
                elif choice2 == 3:
                    single_students()
                elif choice2 == 4:
                    new_note()
        
                elif operation == 5:
                    print("Завершення роботи...")
                    break
                else:
                    print(f"{Fore.RED}🆘 Недопустимий тип даних!")

# дістає одного студента


def single_students() -> None:
    stud_list = get_students()
    if not stud_list:
        print(f"{Fore.RED}🆘 Список учнів порожній, спочатку введіть список!")
        return
    single_student = random.choice(stud_list)
    print(f"{Fore.GREEN}{single_student}")

# конвертує файл похвали


def get_congrats() -> list:
    with open("C:/Users/Anna/Downloads/teacher_app/congrats.txt", "r", encoding="utf-8") as f:
        return [line.strip() for line in f]

# виводить одну похвалу


def create_congrats() -> None:
    cong_list = get_congrats()
    if not cong_list:
        print(f"{Fore.RED}🆘 Список похвали порожній, спочатку введіть список!")
        return
    congratul_message = random.choice(cong_list)
    print(f"{Fore.GREEN}{congratul_message}")

# конвертує файл студентів


def get_students() -> list:
    with open("C:/Users/Anna/Downloads/teacher_app/children.txt", "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

# розподіляє команди зі списку


def create_teams():
    stud_list = get_students()

    if not stud_list:
        print(f"{Fore.RED}🆘 Список учнів порожній, спочатку введіть список😡")
        return

    random.shuffle(stud_list)
    quantity_of_students = len(stud_list)
    try:
        team_quantity = int(input("Введіть кількість бажаних команд: "))
    except ValueError:
        print(f"{Fore.RED}Недопустимий тип даних!")
        return

    if team_quantity <= 0 or team_quantity > quantity_of_students:
        print(f"{Fore.RED}Недопустима кількість команд")

    teams = [[] for _ in range(team_quantity)]

    for i, student in enumerate(stud_list):
        teams[i % team_quantity].append(student)

    for i, team in enumerate(teams, 1):
        print(f"{Fore.GREEN}\nКоманда {i}:")
        for student in team:
            print(f"{Fore.GREEN} - {student}")

# створення похвали


def new_note() -> dict:
    notes = {}
    stud_list = get_students()
    print(f"{Fore.GREEN}\nУчні:")
    for i, student in enumerate(stud_list):
        print(f"{Fore.GREEN}{i + 1}. {student}")
    try:
        choice = int(input("Якому номеру учня ви хочете зробити замітку?"))
    except ValueError:
        print(f"{Fore.RED}🆘 Недопустимий тип даних!")
        return

    if choice > len(stud_list) or choice <= 0:
        print(f"{Fore.RED}🆘 Недопустиме число!")
        return
    student = stud_list[choice - 1]
    note = input(f"Введіть примітку для {student}: ")
    notes[student] = note
    save_notes(notes)
    print(f"{Fore.GREEN}✅ Примітку збережено!")
    return notes

# створення похвали в файлі


def save_notes(notes):
    with open("C:/Users/Anna/Downloads/teacher_helper/admire.txt", "a", encoding="utf-8") as f:
        for name, note in notes.items():
            f.write(f"{name}: {note}\n")


# запуск головної функції


if __name__ == "__main__":
    operations()
