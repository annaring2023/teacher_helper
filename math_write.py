import random
how_much = int(input("кількість прикладів: "))
with open("math_multiply", "w", encoding='utf8' ) as file:
    for i in range(how_much):
        number01 = random.randint(1,10)
        number02 = random.randint(1,10)
        math = f"{number01} * {number02} = \n"
        file.write(math)