import random

datorVärde = random.randint(1,6)
spelarVärde = random.randint(1,6)

datorVärdeMedel = int(datorVärde/2)
datorGissning = datorVärdeMedel+random.randint(1,2)
print (datorGissning)

spelarTur = str(input("Vill du gissa eller bluffa?"))
while True:
    if spelarTur == "gissa":
        spelarGissning = int(input("Hur mycket gissar du på?"))
        if spelarGissning < datorGissning:
            str(input("Gissa igen"))
    elif spelarTur == "bluffa":
        break
    else: 
        spelarTur = str(input("Ogiltig input."))




gissning = int(input("Gissning "))
print(gissning)