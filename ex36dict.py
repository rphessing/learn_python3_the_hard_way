# This code is structured in the following way:
# First, the text variables with the texts used in the code
# Second, repetitive functions
# Third, functions with the unique variables stored in a dictionary and then used by 
# the repetitive functions

import datetime # import datetime module from python

# Username argument entered through command line (argv module)
from sys import argv # use argv attribute in the import module from python sys package
script, name_player, filename = argv # script name, player, game_history.txt file name
# sample string to start script: python3.6 ex36dict.py Jane game_history.txt

##########################################################################################
# FIRST, TEXT VARIABLES USED IN CODE

# game level 1 text
level1_text = (f"""
\nYou {name_player} are a rich king, and one day you wake-up and your gold is stolen by the Bavarians.

You must find back your gold and recover your country's peace but the Bavarians dumped you 
far away in the wood.

Go find the way back to your castle, 
release your friend from jail and fight the Bavarians. \n
    
With your friend you need to distract them to access and recover the gold and free 
your country from the Bavarians.
    
Now your hands are tight on your back and you are dumped into the river. 
You lay with your face down on the side of a river bend and you can barely breath.
    
Your nose and eyes and forehead are just slightly above the water.
    
How do you try to safe yourself from drowning?
    
A. Turn your back on the slippery rockbed and move your hands over the
rock to break the cord and get your hands loose.
    
B. Push yourself out of the riverbed onto the mainland.
    
C. Cry for help and pray.

Enter, A, B or C. Make your choice.""")  
## \n not required for breaks because it is double on Mac terminal. Not tested on other OS.

level1a_text = """You choose option A."""
level1b_text = """You choose option B."""
level1c_text = """You choose option C. You may skip 3 levels and move ahead to Level 5."""

# game level 1_1 text
level1_1_text = """\nYou turn and now you can't breath any longer, ...HELP! You can't breath, you:

A. quickly turn yourself back onto your belly
B. Scratch your hands very slowly over the rock even you are bleeding rapidly.
C. Scratch your hands very fast over the rock because you are bleeding rapidly.

Enter, A, B or C. Make your choice."""
 
level1_1a_text = """You choose option A.
You turn back on your back and return to level 1, and start again from the beginning..."""
level1_1b_text = """You choose option B. And you continue to level 2."""
level1_1c_text = """You choose option C. You bleed heavily, slip of the rock into the river
and die."""

# game level 2 text
level2_text = """
\nYou get your hands loose, get up and walk ashore. 
You think everything is fine now but you realize you are bleeding fast. 

How will you stop the bleeding?

A. stick your finger in your mouth to stop the bleeding.

B. Push the wound with your other hand to stop the bleeding.

C. Use your T-Shirt to stop the bleeding.

Enter A, B or C. Make your choice."""

level2a_text = """You choose option A. You lose consciousness and die."""
level2b_text = """You choose option B. Excellent. 
Your strange idea help stop the bleeding and you move ahead to level 3."""
level2c_text = """You choose option C. You try to take off your shirt, but it hurts too much."""

# game level 2_1 text
level2_1_text = """\nWill you try again? Choose option 'C' or:

A. stick your finger in your mouth to stop the bleeding.
B. Push the wound with your other hand to stop the bleeding.
C. Try again to use your T-Shirt to stop the bleeding."""

level2_1c_text = """You choose option C. You try to take off your shirt again, the pain make you faint and you die."""

# game level 3 text
level3_text = """
\nFind back the castle. And fast.

How will you find back the castle?

A. Use the sun's direction to navigate to the north.

B. Follow the river. Longer route. But sure way to arrive.

C. Take out your cellphone and call an Uber.

Enter, A, B or C. Make your choice."""

level3a_text = """You choose option A. Now lets see how well your survival skills are..."""
level3b_text = """You choose option B. You slip back into the river and die."""
level3c_text = """You choose option C. Wait?! Do you own Uber preferred stock or something?"""

# game level 3_1 text
level3_1_text = """
\nTo which side the sun goes down in the winter?

A. North-south.

B. Middle-east.

C. South-East.

Enter, A, B or C. Make your choice."""

level3_1a_text = """You choose option A. You're a lost cause. You die."""
level3_1b_text = """You choose option B. A Chinese Crocodile will eat you and you die."""
level3_1c_text = """You choose option C. Great! You arrive at the castle and move ahead to level 4."""

# game level 3_2 text
level3_2_text = """
\nYour Uber arrives at your location within 5 minutes but inside the car is the notorious
Uber Monster. What will do you?

A. Press the SOS button on your phone.

B. Attack.

C. Make a chat. Small-talk with the monster.

Enter, A, B or C. Make your choice."""

level3_2a_text = """You choose option A. Great. You are so smart... you skip one level and move ahead to level 5."""
level3_2b_text = """You choose option B. The Uber monster is Uber strong and you die."""
level3_2c_text = """You choose option C. Great! You are taken to the castle and move ahead to level 4. You are smart!"""

# game level 4 text
level4_text = """
\nYou reach the castle at 4AM and the gate is up. You try your security-code to get in but
the Bavarians changed the code and now it asks you the secret question.

Do you remember the answer to the secret question?

If you answer it correctly, you will be able to reset your password and open the gate."""

# game level 5 text
level5_text = """The castle gate opens and you enter. You notice everybody is asleep, including
the guard you walk pass. Now you must find your friend and release him from his jail cell.

What will do you?

A. Go downstairs.

B. Take the elevator instead.

C. Throw a rope through the window, go down and get inside your friends jail cell from the outside.

Enter, A, B or C. Make your choice."""

level5a_text = """You choose option A. Great. You are so smart... you move ahead to level 6."""
level5b_text = """You choose option B. Castles don't have elevators you lazy king. You die."""
level5c_text = """You choose option C. Great! You do reach the jail cell but get stuck inside. You die"""

# game level 6 text
level6_text = """A guard is snorring in front of the cell. He have the keys in his pocket.

What will you do?

A. Put your hand in his pocket and grab the key.

B. Knock him on the head, then grab the keys.

C. Start a conversation with your friend.

Enter, A, B or C. Make your choice."""

level6a_text = """You choose option A. To bad. The guard wakes-up and dies."""
level6b_text = """You choose option B. Awesome. You obtain the keys and open the lock and release
your friend. Congratulations. You won!!!"""
level6c_text = """You choose option C. You make noice. The other guards are alerted and you die."""

##########################################################################################  
# SECOND, REPETITIVE FUNCTIONS

# repetitive function to start each new level
# (level_number) = 'level1' or 'level2' etc, to return a dictionary
def start_new_level(level_number):
    attempt = 1 # variable to track attempts used by 'game_difficulty_nr'
        
    global dictionary
    dictionary = level_number() # used to fill 'level_end' with game level data from a
    # dictionary defined on a per level basis. See also: level1() or level2(), etc. 
    
    print(dictionary['txt']) # print story
    
    while True:
        choice = input('> ') # variable = user input prompt

        if "A" in choice or "B" in choice or "C" in choice: # if true then
            level_end(choice) # call function
        elif attempt < game_difficulty_level_nr: # if attempt smaller than 'variable'
            print("Wrong answer. Enter: A, B or C  only. Please try again")
            attempt = attempt + 1 # update attempt value
        else: # if-statement is other than 'A' or 'B' or 'C' then
            print("Enter: A, B or C  only. GAME-OVER.")
            game_over() # call game over function

def level_end(choice):
    if choice =="A":
        print(dictionary['option_a'])
        start_new_level(dictionary['next_function_a'])
    elif choice =="B":
        print(dictionary['option_b'])
        start_new_level(dictionary['next_function_b'])
    elif choice =="C":
        print(dictionary['option_c'])
        start_new_level(dictionary['next_function_c'])
    
##########################################################################################  
# THIRD, FUNCTIONS WITH UNIQUE VALUES calling the repetitive functions

# I wanted to avoid the use of 'global variables' and choose to use a dictionary instead
# The level dependent variables are all stored in the 'dictionary'
# Each time 'start_new_level' is called the 'dictionary' key values are updated with the 
# level specific key variables. 
# Each level in this game (except for level 4) uses 'start_new_level'
  
# the 'dictionary' is used by the 'level_end' function

def level1():
    return {'txt':level1_text, # fill txt (key) with correct text (key value)
    'option_a':level1a_text,
    'option_b':level1b_text,
    'option_c':level1c_text,
    
    'next_function_a':level1_1, # fill next_function (key) with function name (key value)
    'next_function_b':level2, 
    'next_function_c':level5,
    'player_level':1} # used in game history log inside 'game_over' function
  
def level1_1():
    return {'txt':level1_1_text, 
    'option_a':level1_1a_text,
    'option_b':level1_1b_text,
    'option_c':level1_1c_text,
    
    'next_function_a':level1,
    'next_function_b':level2, 
    'next_function_c':game_over,
    'player_level':1} 
    
def level2():
    return {'txt':level2_text, 
    
    'option_a':level2a_text,
    'option_b':level2b_text,
    'option_c':level2c_text,
    
    'next_function_a':game_over, 
    'next_function_b':level3, 
    'next_function_c':level2_1,
    'player_level':2} 

# level2_1 = equal as level2 with text difference function_c = game_over on second try    
def level2_1():
    return {'txt':level2_1_text,
    
    'option_a':level2a_text,
    'option_b':level2b_text,
    'option_c':level2_1c_text,
    
    'next_function_a':game_over, 
    'next_function_b':level3, 
    'next_function_c':game_over}		
        
def level3():
    return {'txt':level3_text,
    
    'option_a':level3a_text,
    'option_b':level3b_text,
    'option_c':level3c_text,
    
    'next_function_a':level3_1, 
    'next_function_b':game_over, 
    'next_function_c':level3_2,
    'player_level':3}

def level3_1():
    return {'txt':level3_1_text, 
    
    'option_a':level3_1a_text,
    'option_b':level3_1b_text,
    'option_c':level3_1c_text,
    
    'next_function_a':game_over, 
    'next_function_b':game_over,
    'next_function_c':level4,
    'player_level':3}

def level3_2():
    return {'txt':level3_2_text,
    
    'option_a':level3_2a_text,
    'option_b':level3_2b_text,
    'option_c':level3_2c_text,
    
    'next_function_a':level5, 
    'next_function_b':game_over,
    'next_function_c':level4,
    'player_level':3}

def level4():
    dictionary['txt'] = level4_text # update existing dictionary entry
    print(level4_text)
    dictionary['player_level'] = 4 # update existing dictionary entry
    request_for_secret_answer() # call level specific function
    
def level5():
    return {'txt':level5_text,
    
    'option_a':level5a_text,
    'option_b':level5b_text,
    'option_c':level5c_text,
    
    'next_function_a':level6, 
    'next_function_b':game_over, 
    'next_function_c':game_over,
    'player_level':5} 
    
def level6():
    return {'txt':level6_text, 
    
    'option_a':level6a_text,
    'option_b':level6b_text,
    'option_c':level6c_text,
    
    'next_function_a':game_over, 
    'next_function_b':win_game, 
    'next_function_c':game_over,
    'player_level':6} 
    
##########################################################################################
# Other non repetitive functions

# function to exit program without errors by 'game-over' or 'winning' the game
def game_over():
    #write to game history log function
    game_history = open(filename, 'a+')
        
    # Variable using a method to write previous prompted lines for input to the file
    game_history.write(datetime.datetime.now().ctime())
    game_history.write(f""" Game level: {dictionary['player_level']} was reached by: {name_player} ({game_difficulty_level} level player)\n""")
    
    # Close file
    game_history.close()
    
# I had to close the file and then open it again, otherwise it does not reflect the 
# (.write)changes that are made by this function after it opened the file. 
# Other solution to load the changes is to flush to see the latest changes.  
    
    game_history = open(filename)
    #read_to_game_history_log function
    print(f"Here is your the game history log: {filename}")
    print(game_history.read())
    
    # Close file
    game_history.close()
    exit(0) # good normal exit without errors.
    
def win_game():
    dictionary['player_level'] = 'Game won!' # update existing dictionary entry for log file
    game_over() # call level function
    
def game_level_difficulty():
    print(f"""Hi {name_player}, Please select the games' difficulty level:
    
    A. Novice
    B. Intermediate
    C. Expert
    
Please enter: Novice, Intermediate or Expert. Enter: Exit to close the program. Make your choice.""")
    global game_difficulty_level
        
    while True: 
        game_difficulty_level = input('> ')
    
        if game_difficulty_level == "Novice" or game_difficulty_level == "Intermediate" or game_difficulty_level == "Expert":
            print(f"Great {name_player}! You are a {game_difficulty_level} player.")

            game_level_difficulty_level_conversion()
            
        elif game_difficulty_level == "Exit":
            print("Goodbye")
            game_over()
        
        else:
            print("I've got no idea what that means.")
            print("Enter: Novice, Intermediate or Expert  only. Please try again.")

def game_level_difficulty_level_conversion(): # Did not know of another way to convert this
    global game_difficulty_level_nr
    if game_difficulty_level == "Expert":
        game_difficulty_level_nr = 1
        configure_castle_gate_security_question()
        
    elif game_difficulty_level == "Intermediate":
        game_difficulty_level_nr = 3
        configure_castle_gate_security_question()
          
    else:
        game_difficulty_level_nr = 5 # Novice
        configure_castle_gate_security_question()
        
# Level 4 function ot open castle Gate ###################################################
def configure_castle_gate_security_question():
    print(f"{name_player}, Please define a security question that only YOU know the answer to in the field below?")
    global secret_question # Set variable to global to call it outside this function
    
    while True:
        secret_question = input('> ') # variable = user input prompt
        
        secret_question_word_count = (len(secret_question))
    
        if secret_question == "Exit":
            print("Goodbye")
            game_over()
            
        elif secret_question_word_count <10:
            print("Your question should be a sentence. Minimal 10 characters are required.")
            print("Please try again or type 'Exit' to end program.")
        
        else:
            configure_castle_gate_security_answer()

def configure_castle_gate_security_answer():       
    print(f"{name_player}, please provide the answer to your following question: \n{secret_question}")
    global secret_answer # Set variable to global to call it outside this function
    secret_answer = input('> ') # variable = user input prompt
    print('Thank you! Your security settings have now been updated.')
    start_new_level(level1)

def request_for_secret_answer():
    attempt = 1 # outside while true. Inside it does not work. Why?
    print(f"Please provide us with the answer to the following question: \n{secret_question}")

    while True: # infinitive loop
        answer = input('> ')
        if answer == secret_answer:
            print("Your answer is correct!")
            start_new_level(level5)
            
        elif attempt < game_difficulty_level_nr and answer != secret_answer:
            print("Wrong answer. Please try again")
            attempt = attempt + 1

        else:
            print(f"Wrong answer. Goodbye {name_player}. GAME OVER!")
            game_over()

##########################################################################################
    
game_level_difficulty()   
