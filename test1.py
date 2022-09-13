import random

random_words=['sculpture','can','relationship','deviation','brain']
random_word=random.choice(random_words)

user_guess=''
chances=10

while(chances>0):
    x=len(random_word)
    for char in random_word:
        if char in user_guess:
            print( char)
            x-=1
            if(x==0):
                print('congratulation you have won the game the word is '+ random_word)
                break
            else:
                continue
        else:
            print('*')

    guess_word=input("Enter the guessing chracter")
    user_guess+=guess_word

    if(guess_word not in random_word):
        chances-=1
        print('please try aonther character')

        if chances==0:
            print('game over')

