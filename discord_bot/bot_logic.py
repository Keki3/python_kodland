import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

#tirar dados
def dice(sides, count):
    dice_list = []
    result = "El resultado es:"
    total = 0

    for i in range(count):
        die = random.randint(1, sides)
        dice_list.append(die)
    
    for d in dice_list:
        result += " "
        result += str(d)
        total += d

    result += " = " + str(total)

    return result
