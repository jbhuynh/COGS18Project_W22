from IPython.display import YouTubeVideo

import sys

video = YouTubeVideo("O7_DFG3Vkrk")
video2 = YouTubeVideo("TDnSdmznaTk")

def hp_intro():
    """Introduction. User inputs their name and is introduced to the game.
    
    PARAMETERS
    ----------
    None
    
    RETURNS
    -------
    Intro: str
        text specified by what is inputed by user
    """
    
    #input name for custom intro message
    name = input("What is your name?\n")
    
    print("""    Hello """ + name + """! Welcome to Hogwarts! This game
    will allow you to win points for your house based on how much you know 
    about your Hogwartshouse. Get ready! Each question varies in points 
    depending on level of difficulty. Choose carefully as you can lose 
    points if you answer wrong.\n""")
    
    #introduction for each house
    hp_house = input("What Hogwarts house are you in? If you don't know, type 'IDK' \n"
                     " 1. Gryffindor \n 2. Ravenclaw \n 3. Hufflepuff \n 4. Slytherin \n 5. 'IDK' \n")
                     
    if hp_house == "1":
        intro = ("""       "\033[1;34;31mHello brave lion. I see you are ready to step forward to 
        complete this challenge. Proceed with caution. Do not think only with 
        your brawns.\033[00m"\n""")
    elif hp_house == "2":
        intro = ("""       "\033[1;34;61mHello wise raven. I see you are ready to utilize your 
        intellect to complete this challenge. Do not become too arrogent and 
        allow yourself a moment's notice.\033[00m"\n """)
    elif hp_house == "3":
        intro = ("""       "\033[1;34;33mHello sweet badger. I see you are ready to complete this
        challenge. Proceed with caution. Do not let others get into your head 
        and believe in yourself.\033[00m"\n""")
    elif hp_house == "4":
        intro = ("""       "\033[1;34;32mHello cunning snake. I see you are eager to win. Proceed 
        with caution. Do not get ahead of yourself and set your pride to the 
        side and seek for help when needed.\033[00m"\n""")
    elif hp_house == "5":
        intro = ("""       "\033[1;34;35mHello! I assume you are new to this! No worries, we will 
        quiz you on the basics of the Harry Potter franchise, unless you prefer
        to test your knowledge on the other houses. Good luck!\033[00m"\n""")
    else:
        sys.exit("Uh oh! Seems like you did not input one of the numbers listed above.\n"
                 "Please restart and try again.\n")
    
    print(intro)
    

def house(Gryffindor, Ravenclaw, Hufflepuff, Slytherin, idk_quiz):
    select_house = input("Which house would you like to be tested on?\n 1. Gryffindor \n" 
                         " 2. Ravenclaw \n 3. Hufflepuff \n 4. Slytherin \n 5. 'IDK' \n ")
    """User inputs their Hogwart's house.
    
    PARAMETERS
    ----------
    Gryffindor : string
        Takes user to quiz on gryffindor
    Ravenclaw : string
        Takes user to quiz on ravenclaw
    Hufflepuff : string
        Takes user to quiz on hufflepuff
    Slytherin : string
        Takes user to quiz on slytherin
    idk_quiz : string
        Takes user to quiz on general Harry Potter questions 
    
    RETURNS
    -------
    The function correcsponding for each Hogwart's house
    """
# once number is selected, user will be directed to corresponding quiz    
    if select_house == "1":
        
        return Gryffindor()
    
    elif select_house == "2":
        
        return Ravenclaw()
    
    elif select_house == "3":
        
        return Hufflepuff()
    
    elif select_house == "4":
        
        return Slytherin()
    
    elif select_house == "5":
        
        return idk_quiz()
    
    else:
        sys.exit("Uh oh! Seems like you did not input one of the numbers listed above.\n"
                 "Please restart and try again.\n")
    
def Gryffindor():
    """These are questions for those who chose Gryffindor and will be asked four different 
    questions, each question will give them a certain amount of points for their house based 
    on how difficult the question is.

    PARAMETERS
    ----------
    none

    RETURNS
    -------
    Score: int
        Current score calculated as user inputs answers
    """

    # initializes score to 320
    score = 320
    print("\nGood Luck! Answer carefully. Your house is currently at 320 points!")

    question_1 = input("\nWho guards the entrance to Gryffindor tower?\n")
    if question_1.lower() == "fat lady":
        score += 5
        print("Correct! Your score: " + str(score))
    else:
        score -= 5
        print("Incorrect. Your score: " + str(score))

    question_2 = input("\nWho is the resident ghost of Gryffindor?\n")
    if question_2.lower() == "sir nick" or question_2 == "nearly headless nick":
        score += 10
        print("Correct! Your Score:" + str(score))
    else:
        score -= 10
        print("Incorrect. Your score: " + str(score))   

    question_3 = input("\nWho is the founder of Gryffindor?\n")
    if question_3.lower() == "grodric gryffindor":
        score += 2
        print("Correct! Your Score:" + str(score))
    else:
        score -= 2
        print("Incorrect. Your score: " + str(score)) 

    question_4 = input("\nWho killed Nagini?\n")
    if question_4.lower() == "neville longbottom":
        score += 5
        print("Correct! Your Score:" + str(score))
    else:
        score -= 5
        print("Incorrect. Your score: " + str(score))

    print("\033[2;31;51mpoints earned: " + str(score))
    print("\n\033[1;34;36mLearn more about each of the houses below!")
    display(video)

def Ravenclaw():
    """These are questions for those who chose Ravenclaw and will be asked four 
    different questions, each question will give them
    a certain amount of points for their house.

    PARAMETERS
    ----------
    none


    RETURNS
    -------
    Score: int
        Current score calculated as user inputs answers
    """

    # initializes score to 320
    score = 320
    
    print("\nGood Luck! Answer carefully. Your house is currently at 320 points!")

    question_1 = input("\nWhat is Ravenclaw's mascot?\n")
    if question_1.lower() == "eagle":
        score += 5
        print("Correct! Your score: " + str(score))
    else:
        score -= 5
        print("Incorrect. That was a tricky one. Your score: " + str(score))

    question_2 = input("\nWho is the resident ghost of Ravenclaw?\n")
    if question_2.lower() == "grey lady" or question_2 == "helena ravenclaw":
        score += 10
        print("Correct! Your Score:" + str(score))
    else:
        score -= 10
        print("Incorrect. Your score: " + str(score))   

    question_3 = input("\nWho is the founder of Ravenclaw?\n")
    if question_3.lower() == "rowena ravenclaw":
        score += 2
        print("Correct! Your Score:" + str(score))
    else:
        score -= 2
        print("Incorrect. Your score: " + str(score)) 

    question_4 = input("\nWhat did Harry Potter seek from this house?\n")
    if question_4.lower() == "diadem" or question_4.lower() == "crown":
        score += 5
        print("Correct! Your Score:" + str(score))
    else:
        score -= 5
        print("Incorrect. Your score: " + str(score))

    print('\033[2;31;51mpoints earned: ' + str(score))
    print("\n\033[1;34;36mLearn more about each of the houses below!")
    display(video)

def Hufflepuff():
    """These are questions for those who chose Hufflepuff and will be asked four 
    different questions, each question will give them a certain amount of points 
    for their house.

    PARAMETERS
    ----------
    none


    RETURNS
    -------
    Score: int
        Current score calculated as user inputs answers
    """

    # initializes score to 320
    score = 320
    
    print("\nGood Luck! Answer carefully. Your house is currently at 320 points!")

    question_1 = input("\nWhat is Hufflepuff's mascot?\n")
    if question_1.lower() == "badger" or question_1.lower() == "honey badger":
        score += 5
        print("Correct! Your score: " + str(score))
    else:
        score -= 5
        print("Incorrect. Your score: " + str(score))

    question_2 = input("\nWho is the resident ghost of Hufflepuff?\n")
    if question_2.lower() == "fat friar":
        score += 10
        print("Correct! Your Score:" + str(score))
    else:
        score -= 10
        print("Incorrect. That was a tricky one. Your score: " + str(score))   

    question_3 = input("\nWho is the founder of Hufflepuff?\n")
    if question_3.lower() == "helga hufflepuff":
        score += 2
        print("Correct! Your Score:" + str(score))
    else:
        score -= 2
        print("Incorrect. Your score: " + str(score)) 

    question_4 = input("\nWho's a famous metamorphmagus from this house?\n")
    if question_4.lower() == "tonks" or question_4.lower() == "nymphadora tonks":
        score += 5
        print("Correct! Your Score:" + str(score))
    else:
        score -= 5
        print("Incorrect. Your score: " + str(score))

    print('\033[2;31;51mpoints earned: ' + str(score))
    print("\n\033[1;34;36mLearn more about each of the houses below!")
    display(video)
    
def Slytherin():
    """These are questions for those who chose Slytherin and will be asked 
    four different questions, each question will give them a certain amount 
    of points for their house.

    PARAMETERS
    ----------
    none

    RETURNS
    -------
    Score: int
        Current score calculated as user inputs answers
    """

    # initializes score to 320
    score = 320
    
    print("\nGood Luck! Answer carefully. Your house is currently at 320 points!")

    question_1 = input("\nWhat is Slytherin's mascot?\n")
    if question_1.lower() == "serpent":
        score += 5
        print("Correct! Your score: " + str(score))
    else:
        score -= 5
        print("Incorrect. Your score: " + str(score))

    question_2 = input("\nWho is the resident ghost of Slytherin?\n")
    if question_2.lower() == "bloody baron":
        score += 10
        print("mCorrect! Your Score: " + str(score))
    else:
        score -= 10
        print("Incorrect. Your score: " + str(score))   

    question_3 = input("\nWho is the founder of Slytherin?\n")
    if question_3.lower() == "salazar slytherin":
        score += 2
        print("Correct! Your Score:" + str(score))
    else:
        score -= 2
        print("Incorrect. Your score: " + str(score)) 

    question_4 = input("\nWho is the most famous wizard from this house?\n")
    if question_4.lower() == "tome riddle" or question_4.lower() == "lord voldemort":
        score += 5
        print("\033[1;34;61mCorrect! Your Score:" + str(score))
    else:
        score -= 5
        print("Incorrect. Your score: " + str(score))

    print('\033[2;31;51mpoints earned: ' + str(score))
    print("\n\033[1;34;36mLearn more about each of the houses below!")
    display(video)


def idk_quiz():
    """These are questions for those who don't know much about Hogwarts will be 
    asked four different questions, each question will give them a certain 
    amount of points and at the end will determine how much they know about Harry Potter.

    PARAMETERS
    ----------
    none

    RETURNS
    -------
    Score: int
        Current score calculated as user inputs answers
    none
    """

    # initializes score to 0
    score = 0
    print("\nGood Luck! Answer carefully. The amount of points you earn will\n"
          "determine how much you know about Harry Potter!")

    question_1 = input("\nWho killed Lord Voldemort?\n")
    if question_1.lower() == "harry potter":
        score += 5
        print("Correct! Your score: " + str(score))
    else:
        score -= 5
        print("Incorrect. Your score: " + str(score))

    question_2 = input("\nDid Headmaster Dumbledore die?\n")
    if question_2.lower() == "yes":
        score += 5
        print("Correct! Your Score:" + str(score))
    else:
        score -= 5
        print("Incorrect. Your score: " + str(score))   

    question_3 = input("\nWho wrote Harry Potter?\n")
    if question_3.lower() == "j.k. rowling" or question_3.lower() == "jk rowling":
        score += 2
        print("Correct! Your Score:" + str(score))
    else:
        score -= 2
        print("Incorrect. Your score: " + str(score)) 

    question_4 = input("\nWhat are non-magical people called in Harry Potter?\n")
    if question_4.lower() == "muggles":
        score += 10
        print("Correct! Your Score:" + str(score))
    else:
        score -= 10
        print("Incorrect. Your score: " + str(score))

    print('\033[2;31;51mpoints earned: ' + str(score))
    print("\n\033[1;34;36mLearn more about the Harry Potter movies below!")
    display(video2)

    
hp_intro()
house(Gryffindor, Ravenclaw, Hufflepuff, Slytherin, idk_quiz)
   
   
   
   
   
   
   