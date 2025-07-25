import random
i = 0
how_much = int(input("кількість прикладів: "))
with open("math_attention", "w", encoding='utf8' ) as file:
    while i < how_much :
        number01 = random.randint(1,100)
        number02 = random.randint(1,100)
        correct = number01 - number02
        if correct < 0:
            continue
        file.write(f"{number01} - {number02} = \n")