# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 17:20:15 2021

@author: talha
"""
    

def main(): 
    leave = "P"
    while leave == "P":
        gryffindor = 0
        ravenclaw = 0
        hufflepuff = 0
        slytherin = 0
        incorrect_Letter = 0
        name = input("What is your name?\n")
        #name[0] = name[0].upper
        sorting_Hat = input("\nHello " + name + "!! \nThe sorting hat is ready for you now. \nGood Luck! \n\nType any key to wear the sorting hat: ")
        name = name.upper()
        if len(sorting_Hat) > 0:
            q1_answer = input("\nHow would you describe yourself? \na) brave \nb) studious \nc) loyal \nd) ambitious\n \nChoose a, b, c, or d: ")
            q1_answer = q1_answer.upper()
            if q1_answer == "A":
                gryffindor = gryffindor + 1
            elif q1_answer == "B":
                ravenclaw = ravenclaw + 1
            elif q1_answer == "C":
                hufflepuff = hufflepuff + 1
            elif q1_answer == "D":
                slytherin = slytherin + 1
            else:
                incorrect_Letter = incorrect_Letter + 1
            q2_answer = input("\nWhat can you be found doing on the weekends? \na) Going on adventures \nb) Doing my homework \nc) Spending time with family or friends \nd) Plotting revenge on my enemies\n \nChoose a, b, c, or d: ")
            q2_answer = q2_answer.upper()
            if q2_answer == "A":
                gryffindor = gryffindor + 1
            elif q2_answer == "B":
                ravenclaw = ravenclaw + 1
            elif q2_answer == "C":
                hufflepuff = hufflepuff + 1
            elif q2_answer == "D":
                slytherin = slytherin + 1
            else:
                incorrect_Letter = incorrect_Letter + 1
            q3_answer = input("\nWhat would you do if the Dark Lord was going to invade your school? \na) Fight him \nb) Look up some good defensive curses in a book \nc) Stand by my friends no matter what \nd) Help the Dark Lord invade the school as an inside spy\n \nChoose a, b, c, or d: ")
            q3_answer = q3_answer.upper()
            if q3_answer == "A":
                gryffindor = gryffindor + 1
            elif q3_answer == "B":
                ravenclaw = ravenclaw + 1
            elif q3_answer == "C":
                hufflepuff = hufflepuff + 1
            elif q3_answer == "D":
                slytherin = slytherin + 1
            else:
                incorrect_Letter = incorrect_Letter + 1
            q4_answer = input("\nChoose one of the following elements: \na) Fire \nb) Air \nc) Earth \nd) Water\n \nChoose a, b, c, or d: ")
            q4_answer = q4_answer.upper()
            if q4_answer == "A":
                gryffindor = gryffindor + 1
            elif q4_answer == "B":
                ravenclaw = ravenclaw + 1
            elif q4_answer == "C":
                hufflepuff = hufflepuff + 1
            elif q4_answer == "D":
                slytherin = slytherin + 1
            else:
                incorrect_Letter = incorrect_Letter + 1
            
            if name == "FATIMAH MATADAR" or name == "FATIMAH":
                print("\nThe sorting hat does not place muggles, sorry Fatimah :).")
            elif gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin and gryffindor > incorrect_Letter:
                print("\nThe sorting hat has recieved your answers. \nIt is making it's decision. \n\nYou will be in house...     GRYFFINDOR!!!!!!")
            elif ravenclaw > gryffindor and ravenclaw > hufflepuff and ravenclaw > slytherin and ravenclaw > incorrect_Letter:
                print("\nThe sorting hat has recieved your answers. \nIt is making it's decision. \n\nYou will be in house...     RAVENCLAW!!!!!!")
            elif hufflepuff > gryffindor and hufflepuff > ravenclaw and hufflepuff > slytherin and hufflepuff > incorrect_Letter:
                print("\nThe sorting hat has recieved your answers. \nIt is making it's decision. \n\nYou will be in house...     HUFFLEPUFF!!!!!!")
            elif slytherin > gryffindor and slytherin > ravenclaw and slytherin > hufflepuff and slytherin > incorrect_Letter:
                print("\nThe sorting hat has recieved your answers. \nIt is making it's decision. \n\nYou will be in house...     SLYTHERIN!!!!!!")
            elif incorrect_Letter > gryffindor and incorrect_Letter > ravenclaw and incorrect_Letter > hufflepuff and incorrect_Letter > slytherin:
                print("\nThe sorting hat refuses to sort someone who can't follow simple instrunctions.\n \nYour acceptance at Hogwarts has been rescinded.\n \nIn fact, I will make you forget about the magic world in it's entirety!!!\n \nOBLIVIAAAAATEEEEEE!!!!!!!!!!!")
            else:
                print("\nThe sorting hat will need some more information to place you correctly, why don't you take the test again?\n")
                
                
            leave = (input("\n\n\nTo play again type P or X(or any other key) to quit: \n")).upper()
            print("\n")
        
    
    
    
main()
