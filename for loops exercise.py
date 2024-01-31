names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']

names.append(input("Add the name of a friend"))
names1.append(input("Add the name of the other friend"))

for name in names:
    print(f'{name.capitalize()}! You are invited to the party on saturday.')
for name in names1:
    print(f'{name.capitalize()}! You are invited to the party on saturday.')