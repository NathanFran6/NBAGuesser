
num =1
playChoiceInt = [] #Pick which player by choosing a row 

while len(playChoiceInt) < 50:
    playChoiceInt.append(num)
    num += 1 
    
playChoice = map(str, playChoiceInt)

print(playChoice)
