import random as rand

print('Project - Math Tutor')
how_many_questions = int(input('How many questions would you like to answer: '))
max_multiple = int(input('What is the maximum number you would like to be used: '))
questions_answers = dict()
num_correct = 0
num_incorrect = 0

#print(rand1)
for num in range(how_many_questions):
    rand1 = rand.randint(1, max_multiple)
    rand2 = rand.randint(1, max_multiple)
    actual_answer = rand1 * rand2
    #if f'{rand1} * {rand2}' in questions_answers.keys():
        #how_many_questions+=1
        #continue
    user_answer = int(input(f'{rand1} * {rand2} = '))
    questions_answers.update({f'{rand1} * {rand2}': actual_answer})
    if actual_answer == user_answer:
        num_correct+=1
    else:
        num_incorrect+=1
    
percentage_correct = num_correct / how_many_questions * 100
print('Thank you for playing our game!')
print(f'You got a total of {num_correct} correct and {num_incorrect} incorrect. i.e you got {percentage_correct}% correct')

print('These are the questions and their corresponding answers: ')
for key,value in questions_answers.items():
    print(key +' = '+ str(value))
