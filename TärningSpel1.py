import random

datorVärde = random.randint(1,6)
spelarVärde = random.randint(1,6)

totalaVärde = datorVärde + spelarVärde
gissade = 0

datorVärdeMedel = int(datorVärde/2)
datorGissning = datorVärdeMedel+random.randint(1,2)
print("Din tärning visar: ")
print (spelarVärde)
print("Datorn gissar på: ")
print (datorGissning)

spelarTur = str(input("Vill du gissa eller bluffa?"))
while True:
    if spelarTur == "gissa":
        spelarGissning = int(input("Hur mycket gissar du på?"))
        if spelarGissning < datorGissning:
            continue
        elif spelarGissning > datorGissning:
            gissade = 1
            break
    elif spelarTur == "bluffa":
        break
    else: 
        spelarTur = str(input("Ogiltig input."))

if gissade == 1:
    if datorVärde * 2 + random.randint(1,2) < spelarGissning:
        print("Dator säger bluff")
        print("Datorns värde var: ")
        print(datorVärde)
        print("Det totala värdet var: ")
        print(totalaVärde)
        if totalaVärde > spelarGissning:
            print("Spelaren Vann")
            quit()
        else:
            print("Datorn Vann")
            quit()
    else:
        datorGissning = spelarGissning + random.randint(1,2)
        print("Datorn gissar på: ")
        print(datorGissning)
else:
    if totalaVärde > datorGissning:
        print("Datorn Vann")
        quit()
    else:
        print("Spelaren Vann")
        quit()

gissade = 0

spelarTur = str(input("Vill du gissa eller bluffa?"))
while True:
    if spelarTur == "gissa":
        spelarGissning = int(input("Hur mycket gissar du på?"))
        if spelarGissning < datorGissning:
            continue
        elif spelarGissning > datorGissning:
            gissade = 1
            break
    elif spelarTur == "bluffa":
        break
    else: 
        spelarTur = str(input("Ogiltig input."))

if gissade == 1:
    if datorVärde * 2 + random.randint(1,2) < spelarGissning:
        print("Dator säger bluff")
        print("Datorns värde var: ")
        print(datorVärde)
        print("Det totala värdet var: ")
        print(totalaVärde)
        if totalaVärde > spelarGissning:
            print("Spelaren Vann")
            quit()
        else:
            print("Datorn Vann")
            quit()
    else:
        datorGissning = spelarGissning + random.randint(1,2)
        print("Datorn gissar på: ")
        print(datorGissning)
else:
    if totalaVärde > datorGissning:
        print("Datorn Vann")
        quit()
    else:
        print("Spelaren Vann")
        quit()