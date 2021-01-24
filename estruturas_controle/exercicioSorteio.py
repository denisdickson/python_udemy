from random import randint


def sortearDado():
    return randint(1, 7)


for i in range(1, 7):
    if i % 2 == 1:
        continue

    if sortearDado() == i:
        print('Acertou' , i)
        break
else:
    print("Errou", i )

