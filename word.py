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



secret_words=random.choice(words)       #store secret word which was chosen by program
guessed_letters=[]                      #store guessed letter which was guessed by user
attempts=6                             #number of attempts
display_word=["_"]*len(secret_words)    #hidden numbers 
game_over=False                         #controls games loop


while attempts>0:                       #for continuing the game until player guess or games end 
    guess=input('Enter you guess:')

    for i in range(len(secret_words)):
      if guess == secret_words[i]:
        display_word[i]=guess
        print('Secret_words:',"".join(display_word))
        
    if guess in secret_words:
        print('corect guess')
    else:
      print('incorrect guess')
      attempts-=1                       #decreasing number of guesses

    
    print("Attempts:",attempts)


    if "_" not in display_word:
      print("Congratulation")
      break
    if attempts == 0:
     print("the correct word is ",secret_words)