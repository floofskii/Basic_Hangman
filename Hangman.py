import random
import sys
from datetime import datetime, timedelta

word_list=['table', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'plant', 'chair', 'meaning','dictionary','ceiling','motorcycle','heavybike','linkedlist','priority',
         'filtrationplant','heavybike','farming','tissueculture','university','physics','austronat','spaceship',
         'watership','bycycle','training']

def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    
    now = datetime.now()
    maxTime = now + timedelta(minutes = 1)
    while not guessed and tries > 0 and datetime.now()<maxTime:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                print('Remaining tries:'+str(tries))
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congratulations!, you have guessed the word! You win!")
    elif datetime.now()>maxTime:
        print("Sorry, you ran out of time.try again")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")


def display_hangman(tries):
    stages = [  
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
               
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]
def admin():
    adminDict={
    "admin":"admin",
    "login":"login",
    "signin":"signin"
    }

    print('---ADMIN-PORTAL---')
    print('-----------------')
    adminName=input('ENTER USER NAME:')
    adminPass=input('ENTER PASSWORD')
    if(adminName=='' or adminPass==''):
        print('UserName or Password is empty please type again')
        admin()
    for u, p in adminDict.items():
        if u==adminName and p==adminPass:
            print('LOGIN SUCCESS')
            print("---WELCOME:"+adminName+"---")
            adminPage()
            
        print('credentials incorrect!')
        admin()
def adminPage():
        print('*********************************')
        print("Enter 1 To Print all items in list")
        print("Enter 2 to add new word to list")
        print("Enter 3 to Remove word from list:")
        adminInput=input("Enter 4 to go back to main menu:")
        if adminInput=='1':
            print(word_list)
            adminPage()
        elif adminInput=='2':
            enteredWord=input("Enter the word to add it must be atleast 8 characters long:")
            if enteredWord=='':
                print('Cant submit empty word!')
                adminPage()
            if len(enteredWord)>=8:
                word_list.append(enteredWord)
                print('word has been added')
                adminPage()
            else:
                print('Word should be minimum of 8 characters')
                adminPage()
        elif(adminInput=='3'):
            enteredWord=input("Enter the word to remove:")
            
            if enteredWord=='':
                print('Cant submit empty word!')
                adminPage()
            if enteredWord in word_list: 
                word_list.remove(enteredWord)
                print('word has been removed')
                adminPage()
            else:
                print('word not in list')
                adminPage()
        elif adminInput=='4':
            main()
        else:
            print('wrong input')
            adminPage()
def main():
    print("***************")
    print('Welcome to Hangman')
    print('------------------')
    print('Enter 1 for Admin')
    print('Enter 2 for Player')
    print('Enter 3 to exit')
    myInput = input("->")
    if myInput=='':
        print('cant submit empty input!')
        main()
    if myInput=='1':
        admin()
    elif myInput=='2':
        player()
    elif myInput=='3':
        sys.exit('Program Terminated!')
    else:
        print('invalid Syntax\n')
        main()

def player():
    print('Please enter your name to proceed')
    name=input()
    if name=='':
        print('Please enter a valid name, name cant be empty')
        player()
    print('Welcome to Hangeman game '+name)
    print("Total guesses:6")
    print('Total time:5 minutes')
    word = get_word()
    play(word)
    main()
    


if __name__ == "__main__":
    main()
