import random
words=[
    'Guess',
    'Generator',
    'Albania',
    'Tunisia',
    'Ronaldo',
    'Minister',
    'Praline',
    'Console',
    'Powershell',
    'Selection',
    'Python'
]



secret_words=random.choice(words)
guessed_letters=[]
attempts=6
display_word=["_"]*len(secret_words)
game_over=False


while attempts>0:
    guess=input('Enter you guess:')

    if guess in secret_words:
       print('corect guess')
    else:
      print('incorrect guess')
      attempts-=1

    print('Secret_words:',"".join(display_word))
    print("Attempts:",attempts)


    if "_" not in display_word:
      print("Congratulation")
    if attempts==0:
     print("the correct word is ",secret_words)