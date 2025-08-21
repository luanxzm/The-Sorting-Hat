gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0
#Primeira Questão
q1 = float(input('''Do you like Dawn or Dusk?
1) Dawn
2) Dusk
'''))
if q1 == 1:
  gryffindor += 1 
  ravenclaw += 1
elif q1 == 2:
  hufflepuff += 1
  slytherin += 1
else:
  print('Wrong Input')
#Segunda Questão
q2 = float(input('''When I’m dead, I want people to remember me as:
1) The Good
2) The Great
3) The Wise
4) The Bold 
'''))
if q2 == 1:
  hufflepuff += 2
elif q2 == 2:
  slytherin += 2
elif q2 == 3:
  ravenclaw += 2
elif q2 == 4:
  gryffindor += 2
else:
  print('Wrong Input')
#Terceira Questão
q3 = int(input('''Which kind of instrument most pleases your ear?
1) The violin
2) The trumpet
3) The piano
4) The drum 
'''))
if q3 == 1:
  slytherin += 4
elif q3 == 2:
  hufflepuff += 4
elif q3 == 3:
  ravenclaw += 4
elif q3 == 4:
  gryffindor += 4
else:
  print('Wrong Input')
#Resultado2
scores = {
    "Slytherin": slytherin,
    "Hufflepuff": hufflepuff,
    "Ravenclaw": ravenclaw,
    "Gryffindor": gryffindor
}
house = max(scores, key=scores.get)
print(f"Your House is {house}!")