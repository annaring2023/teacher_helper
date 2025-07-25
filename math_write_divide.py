import random
i = 0
how_much = int(input("кількість прикладів: "))
with open("math_divide.txt", "w", encoding='utf8' ) as file_divide:
    while i < how_much:
        number01 = random.randint(1,100)
        number02 = random.randint(1,100)
        if number01 % number02 != 0:
            continue
        correct = f"{number01} / {number02} = \n"
        file_divide.write(correct)
        i += 1