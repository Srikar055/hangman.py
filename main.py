from time import sleep
from random import *

print('Welcome to HANGMAN GAME')

name = input('Enter your name ')
print("Let's get started "+name)
sleep(2)
print('The game is about to start..!')

def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    global word1
    words_to_guess=["Srikar","Srinivas","Mounika","Chandrakala","Mohan","Jana","Swarna","Anvi","Nani","Sunny"]
    word = choice(words_to_guess)
    word1=word
    length=len(word)
    count=0
    display='_'*length
    already_guessed=[]
    play_game=''


def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit=5
    guess=input("This is the HANGMAN word "+display+" guess now \n")
    guess=guess.strip()
    if len(guess.strip())==0 or len(guess.strip())>=2 or guess<="9":
        print('INVALID INPUT,please try again')
        hangman()
    elif guess in word:
        already_guessed.append(guess)
        index=word.find(guess)
        word=word[:index]+'_'+word[index+1:]
        display=display[:index]+guess+display[index+1:]
        print(display)
    else:
        count+=1
        if count==1:
            sleep(1)
            print(" ____ \n"
                  " |   |\n"
                  " |    \n"
                  " |    \n"
                  " |    \n"
                  " |    \n"
                  " |    \n"
                  "_|_   \n")
            print('Wrong guess,try again.!,you are left with '+str(limit - count)+' guess')
        if count == 2:
            sleep(1)
            print(" ____    \n"
                  " |   |   \n"
                  " |   |   \n"
                  " |       \n"
                  " |       \n"
                  " |       \n"
                  " |       \n"
                  "_|_      \n")
            print('Wrong guess,try again.!,you are left with ' + str(limit - count) + ' guess')
        if count==3:
            sleep(1)
            print(" ____    \n"
                  " |   |   \n"
                  " |   |   \n"
                  " |   |   \n"
                  " |       \n"
                  " |       \n"
                  " |       \n"
                  "_|_      \n")
            print('Wrong guess,try again.!,you are left with ' + str(limit - count) + ' guess')
        if count == 4:
            sleep(1)
            print(" ____        \n"
                  " |   |       \n"
                  " |   |       \n"
                  " |   |       \n"
                  " |   0       \n"
                  " |           \n"
                  " |           \n"
                  "_|_          \n")
            print('Wrong guess,try again.!,you are left with ' + str(limit - count) + ' guess')
        if count == 5:
            sleep(1)
            print(" ____    \n"
                  " |   |   \n"
                  " |   |   \n"
                  " |   |   \n"
                  " |   0   \n"
                  " |  /|\  \n"
                  " |   |   \n"
                  " |  / \  \n"
                  "_|_")
            print('Wrong guess,you are hanged')
            print('The word was ',word1)

            play_loop()

    if word=='_' * length:
        print('Congrats you guessed it correct')
        sleep(2)
        play_loop()
    elif count!=limit:
        hangman()

def play_loop():
    global play_game
    play_game=input('Do you want to play again if yes please enter "y" else "n" \n')
    while play_game not in ['Y','N','y','n']:
        play_game=input('Do you want to play again if yes please enter "y" else "n"\n')
    if play_game=='Y' or play_game=='y':
        main()
        hangman()
    else:
        print('Thank you..!')
    exit()

main()
hangman()