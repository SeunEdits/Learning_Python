
csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = ['Exercise: fill me with names']
print(friends_list)
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise
csv = csv.replace(':', ',')
print(csv)

csv = csv.replace(';', ',')
print(csv)

friends_list = csv.split(',')
print(friends_list)
