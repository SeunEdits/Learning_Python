print('Lambdas Exercise')

def join_list_no_duplicates(list_a,list_b):
   return list(set(list_a + list_b))
list_a = [1,2,3,4]
list_b = [3,4,5,6,7]
#write lambda below 
join_list_no_duplicates1 = lambda list_a,list_b: list(set(list_a + list_b))
print(join_list_no_duplicates1(list_a,list_b))
















#Complete the function so it returns a function
#def create_quad_func(a,b,c):
#    '''return function f(x) = ax^2 + bx + c'''
#    return lambda x:
#f = create_quad_func(2,4,6)
#g = 
#print(f(2))
#print(g(2))
















#signups = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']
#print(sorted(signups)) # Lexicographic sort
#write sorting by integer
#print(sorted(...)) # Integer sort



















class Player:
   def __init__(self, name, score):
       self.name = name
       self.score =  score

Eric = Player('Eric', 116700)
John = Player('John', 24327)
Terry = Player('Terry', 150000)
player_list = [Eric, John, Terry]


#Exercise: Sort this by score using lambda!
#write code here
#print([player.name for player in player_list])

