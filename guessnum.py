import random

random_num = random.randint(1,100)
score=0

print("let's play the number guessing  game")
permision = input('do you want to play game yes/no ')

if permision.lower() == "yes" :
   print('>> you have guess the number in 10 attemps only after that game will over')
   for num in range(0,10) :
    print('you have {} attems now and your score is {}'.format(10-num,score))
    try:
        user = int(input('type a number '))
    except ValueError :
        print('Please enter number only')
    if num==9:
       print(random_num)
    if user==random_num :
        print(">> Wow you got it, let's see how much score you can do....")
        score+=1
        random_num = random.randint(1,100)
    elif user>random_num :
        print('>> opps ! you entered greater value')
    elif(user<random_num) :
        print('>> opps ! you have entered lower value')
elif permision=='no' :
    print("okay next time")
