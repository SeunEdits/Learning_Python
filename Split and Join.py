msg ='Welcome  to  Python  101: Split  and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
print('-'.join(friends_list))
splitted = csv.split(',')
print(splitted)
position = splitted.index('Terry')
print(position)
splitted[splitted.index('Terry')] = 'Bola'
print(','.join(splitted))