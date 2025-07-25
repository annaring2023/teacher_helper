import random


def operations():
    while True:
        try:
            operation = int(input(
                "\n1 - Розподілити на команди\n2-похвала для учня\n3 - хто йде до дошки?\n5 - Вийти\nВаш вибір: "))
        except ValueError:
            print("Введіть число")
            continue

        if operation == 1:
            create_teams()
        elif operation == 2:
            create_congrats()
        elif operation == 3:
            single_students()
        elif operation == 5:
            print("Завершення роботи")
            break
        else:
            print("Ввели якусь фігню!")


def single_students() -> str:
    stud_list = get_students()

    if not stud_list:
        print("Список учнів порожній😶‍🌫️ Спочатку введіть список😡")
        return
    single_student = random.choice(stud_list)
    print(single_student)


def get_congrats():
    with open("C:/Users/Anna/Downloads/teacher_app/congrats.txt", "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def create_congrats():
    cong_list = get_congrats()
    if not cong_list:
        print("Список похвали порожній😶‍🌫️ Спочатку введіть список😡")
        return
    congratul_message = random.choice(cong_list)
    print(congratul_message)


def get_students():
    with open("C:/Users/Anna/Downloads/teacher_app/children.txt", "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def create_teams():
    stud_list = get_students()

    if not stud_list:
        print("Список учнів порожній😶‍🌫️ Спочатку введіть список😡")
        return

    random.shuffle(stud_list)
    quantity_of_students = len(stud_list)
    team_quantity = int(input("Введіть кількість бажаних команд: "))

    if team_quantity <= 0 or team_quantity > quantity_of_students:
        print("Недопустима кількість команд")

    teams = [[] for _ in range(team_quantity)]

    for i, student in enumerate(stud_list):
        teams[i % team_quantity].append(student)

    for i, team in enumerate(teams, 1):
        print(f"\nКоманда {i}:")
        for student in team:
            print(" -", student)


operations()
