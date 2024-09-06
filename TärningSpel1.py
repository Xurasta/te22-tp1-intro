import random

datorVärde = random.randint(1,6)
spelarVärde = random.randint(1,6)

datorVärdeMedel = int(datorVärde/2)
print (datorVärdeMedel+random.randint(1,2))

spelarTur = string(input("Vill du gissa eller bluffa?"))
if spelarTur == "gissa":
    spelarGissning = int(input("Hur mycket gissar du på?"))

gissning = int(input("Gissning "))
print(gissning)