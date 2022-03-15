import random
# PART 1
# display a menu with at least 3 difficulty choices and ask the user
# to select the desired level
# difficulty = "1" # sample data, normally the user should choose the difficulty



# STEP 2
# based on the chosen difficulty level, set the values 
# for the player's lives
# word_to_guess = "Cairo" # sample data, normally the word should be chosen from the countries-and-capitals.txt
# lives = 5 # sample data, normally the lives should be chosen based on the difficulty


# STEP 3
# display the chosen word to guess with all letters replaced by "_"
# for example instead of "Cairo" display "_ _ _ _ _"


# STEP 4
# ask the user to type a letter
# here you should validate if the typed letter is the word 
# "quit", "Quit", "QUit", "QUIt", "QUIT", "QuIT"... you get the idea :)
# HINT: use the upper() or lower() built-in Python functions


# STEP 5
# validate if the typed letter is already in the tried letters
# HINT: search on the internet: `python if letter in list`
# If it is not, than append to the tried letters
# If it has already been typed, return to STEP 5. HINT: use a while loop here
#already_tried_letters = [] # this list will contain all the tried letters


# STEP 6
# if the letter is present in the word iterate through all the letters in the variable
# word_to_guess. If that letter is present in the already_tried_letters then display it,
# otherwise display "_".


# if the letter is not present in the word decrease the value in the lives variable
# and display a hangman ASCII art. You can search the Internet for "hangman ASCII art",
# or draw a new beautiful one on your own.



# STEP 7
# check if the variable already_tried_letters already contains all the letters necessary
# to build the value in the variable word_to_guess. If so display a winning message and exit
# the app.
# If you still have letters that are not guessed check if you have a non negative amount of lives
# left. If not print a loosing message and exit the app.
# If neither of the 2 conditions mentioned above go back to STEP 4
life0 = """
            ---------------
           |              |
           |              |
           |              O
           |             \|/
           |              |
           |             / \ 
           |
           =================="""
life1 = """
            ---------------
           |              |
           |              |
           |              O
           |             \|/
           |              |
           |              
           |
           =================="""
life2 = """
            ---------------
           |              |
           |              |
           |              O
           |             \|/
           |              
           |              
           |
           =================="""
life3 = """
            ---------------
           |              |
           |              |
           |              O
           |             
           |              
           |              
           |
           =================="""
life4 = """
            ---------------
           |              |
           |              |
           |              
           |             
           |              
           |              
           |
           =================="""
life5 = """
            ---------------
           |              
           |              
           |              
           |             
           |              
           |              
           |
           =================="""
life6 = """
            
           |              
           |              
           |             
           |             
           |              
           |              
           |
           =================="""
life7 = """
            
                        
                        
                      
                      
           |              
           |              
           |
           =================="""
life8 = """
            
                       
                       
                       
                      
                        
                        
        
           =================="""
life9 = """
            
                        
                       
                     
                     
                       
                       
        
           ======"""
life10 = """
            
                        
                       
                     
                     
                       
                       
        
               """

life = 0
word_to_guess = ""
liste = []
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
memory = []
loop = True
# Space --STEP 1-- 

while True:
    difficulty = input("How taff are you? Easy: 10Lifes. Normal: 7Lifes Hard: 5Lifes.")
    if difficulty.lower() == "hard" or difficulty.lower() == "normal" or difficulty.lower() == "easy":
        if difficulty.lower() == "hard":
            life += 5
            break
        elif difficulty.lower() == "normal":
            life += 7
            break
        elif difficulty.lower() == "easy":
            life += 10
            break
    else:
        print("Pleas only write hard, normal or easy")

# Space --STEP 2-- 
datas_1 = open("countries-and-capitals.txt", "rt")
data = datas_1.readlines()
for x in data:
    y = x.split(" | ")
    liste.append(y[0])
    z = y[1].split("\n")
    liste.append(z[0])

word = random.randrange(0, len(liste))
word_to_guess = (liste[word])
datas_1.close()
word_to_do = word_to_guess

# Space --STEP 3-- 
if " " in word_to_guess:
    word_to_guess = word_to_guess.replace(" ", "   ")
    word_to_do = word_to_do.replace(" ", "   ")
for letter in alphabet:
    if letter.upper() in word_to_guess or letter.lower() in word_to_guess:
        word_to_do = word_to_do.replace(letter.upper(), "_ ")
        word_to_do = word_to_do.replace(letter.lower(), "_ ")
        word_to_guess = word_to_guess.replace(letter.lower(), letter.lower() + " ")
        word_to_guess = word_to_guess.replace(letter.upper(), letter.upper() + " ")
if life == 7:
    print(life7)
elif life == 5:
    print(life5)
elif life == 10:
    print(life10)
print(word_to_do)

# Space --STEP 4--
while loop:
    guess = input("choose your letter:")
    if len(guess) > 1 or guess.lower() not in alphabet:
        print("Sorry, please only use one english letter.")
    elif guess.upper() in memory:
        print("You already have these letter.")
    elif guess.upper() in word_to_guess or guess.lower() in word_to_guess:
        memory.append(guess.upper())
        while True:
            if guess.upper() in word_to_guess:
                letter_place = word_to_guess.find(guess.upper())
                word_to_guess1 = list(word_to_guess)
                word_to_guess1[letter_place] = "!"
                word_to_guess = "".join(word_to_guess1)
                word_to_do1 = list(word_to_do)
                word_to_do1[letter_place] = guess.upper()
                word_to_do = "".join(word_to_do1)
            if guess.lower() in word_to_guess:
                letter_place = word_to_guess.find(guess.lower())
                word_to_guess1 = list(word_to_guess)
                word_to_guess1[letter_place] = "!"
                word_to_guess = "".join(word_to_guess1)
                word_to_do1 = list(word_to_do)
                word_to_do1[letter_place] = guess.lower()
                word_to_do = "".join(word_to_do1)
            else:
                break
            # pause
    else:
        life -= 1
        memory.append(guess.upper())
    finish = word_to_do.count("_")
    if finish == 0:
        loop = False
    if life == 0:
        loop = False
        show = life0
    elif life == 1:
        show = life1
    elif life == 2:
        show = life2
    elif life == 3:
        show = life3
    elif life == 4:
        show = life4
    elif life == 5:
        show = life5
    elif life == 6:
        show = life6
    elif life == 7:
        show = life7
    elif life == 8:
        show = life8
    elif life == 9:
        show = life9
    elif life == 10:
        show = life10
    print(show)
    print("Your letters:" + str(memory))
    print(word_to_do)
if life == 0:
    print("Sorry, I think it was too hard for you. :)")
else:
    print("Congratulation, you have won this round. :)")
