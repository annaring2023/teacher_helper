import random
print("привіт") 
while True:
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    correct = number1 - number2
    if correct < 0:
        continue
    print(f"{number1}-{number2}")
    answer = input( "твоя відповідь: ")
    if answer =="q":
       break
    answer = int(answer)
    if answer  == correct:
        print("молодець")
    else:
        print("давай ще раз")
        for i in range (2):
            answer = input("твоя відповідь: ")
            if answer == correct:
                print("молодець")