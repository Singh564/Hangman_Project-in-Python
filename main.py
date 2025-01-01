""" Hangman Game In Python"""

import random

#Make list of random words 
Word_Group = ['money','monkey','asia','docs','domain','roman']

#Get a random word using the list of word group
Random_Word= random.choice(Word_Group)


Gussed_Word = '_'*len(Random_Word)
print(Gussed_Word)
Total_Chances= 6


while True:
    #Take input from the user
    Gussed_letter = input('Enter The Letter ').lower()
    if Gussed_letter in Random_Word:
        for idx in range(len(Random_Word)):
            if Gussed_letter== Random_Word[idx]:
                Gussed_Word= Gussed_Word[:idx] + Gussed_letter + Gussed_Word[idx+1:]

        
        if Gussed_Word == Random_Word:
                print(' Hurrey,You have won the game')
                print(f"Correct Word is {Random_Word}")
                break

        else:
            print(f"Correct,Guess {Gussed_Word}")
            

    else:
        Total_Chances-=1
        print( f"Incorrect Guess, You have {Total_Chances} chances left ")

        if Total_Chances==0:
            print('You have LOST thE GAME')
            break

    








