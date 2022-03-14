"""Test for my functions. A lot of the return for my
functions return strings so a lot of the testing is similar.
"""
import mock
import builtins

from functions import hp_intro, house, Gryffindor, Ravenclaw, Hufflepuff, Slytherin, idk_quiz


def test_hp_intro():
    assert callable(hp_intro)
    #tests the intro since this function uses input
    with mock.patch.object(builtins, 'input', lambda _: 'Jade'):
        
        intro = hp_intro()
        assert intro == "Hello Jade! Welcome to Hogwarts! This game will allow you to\n"
        "win points for your house based on how much you know about your Hogwarts house.\n"
        "Get ready! Each question varies in points depending on level of difficulty. Choose \n"
        "carefully as you can lose points if you answer wrong." 
        assert type(hp_intro) == str
        
#The remaining tests below are used to test if code is callable with the correct variable
def test_house():
    
    assert callable(house)                   
    assert score == int
    assert type(select_house) == int
    assert len(select_house) == 1
       
def test_Gryffindor():
    
    assert callable(Gryffindor)
    assert score == int
    assert question_1.lower() == "fat lady"

def test_Ravenclaw():
    
    assert callable(Ravenclaw)
    assert score == int
    assert question_3.lower() == "rowena ravenclaw"

def test_Hufflepuff():
    
    assert callable(Hufflepuff)
    assert score == int
    assert question_3.lower() == "helga hufflepuff"
                 
def test_Slytherin():
    
    assert callable(Slytherin)
    assert score == int
    assert question_3.lower() == "salazar slytherin"
    
def test_idk_quiz():
    
    assert callable(idk_quiz)
    assert score == int
    assert question_1.lower() == "harry potter"