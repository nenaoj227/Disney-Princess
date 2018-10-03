import time
import sys
def game():
        x = input("Hello, would you like to play a game to find out which Disney Princess you are? ")
        if ( x == "yes" or x == "Yes" ):
                gender= input("What type of princess are you? Boy? Girl? Alligator? :  ")
                if (gender == "Boy" or gender == "boy"):
                        print("Too bad! You're still a princess.")
                elif (gender == "girl" or gender == "Girl"):
                        print ("Well, let's figure out which Princess you are!")
                else :
                        print("Welp! Then you're a " + gender + " princess!")
        elif ( x == "no" or x == "No"):
                sys.exit("Too Bad!")
        else: 
                print ('Please say "yes" or "no".')
                game()
game()
def seas():
        season = input("What season do you prefer!? Winter or Summer? : ")
        if (season == "Winter" or season == "winter"):
                def bouj():
                        boujee= input ("Would you consider yourself to be boujee? (Yes or No): ")
                        if (boujee == "Yes" or boujee == "yes"):
                                def work():
                                        worker =  input("Are you a hard worker? (Yes or No): ")
                                        if (worker == "Yes" or worker == "yes"):
                                                print ("You are Princess Cinderella. You are consistent and have a focused work ethic which helps you achieve success! ")
                                        elif (worker == "No" or worker == "no"):
                                                print ("You are Princess Aurora. You are a couch potato who enjoys napping on their free time.")
                                        else:
                                                print ('Yo, STOP PLAYING AND PICK "YES" OR "NO"!')
                                                work()
                                work()
                        elif (boujee == "No" or "no"):
                                def sibs():
                                        siblings = input("Do you have siblings? (Yes or No): ")
                                        if (siblings == "Yes" or siblings == "yes"):
                                                print ("You are Merida. You have sibling(s) who drive you crazy, but you sill love them.")
                                        elif (siblings == "No" or siblings == "no"):
                                                print ("You are Fa Mulan. You are an only child who works hard to make thier parents proud.")
                                        else: 
                                                print ('PLEASE PICK "YES" OR "NO"!')
                                                sibs()
                                sibs()
                        else: 
                                print ('Stop playing, please enter "yes" or "no". ')
                                bouj()
                bouj()
        elif (season == "Summer" or season == "summer"):
                def adven():
                        adventure= input("Are you adventurous? (Yes or No): ")
                        if (adventure == "yes" or adventure == "Yes"):
                                def cult():
                                        culture = input("Are you cultured? (Yes or No): ")
                                        if (culture == "yes" or culture == "Yes"):
                                                print ("Congragulations you are Tiana! You love livn life on the bayou! ")
                                        elif (culture == "No" or culture == "no"):
                                                print ("You are definitely Rapunzal! Quite adventurous and free to be just like summer! ")
                                        else: 
                                                print('Please type either "Yes" or "No": ')
                                                cult()
                                cult()
                        elif (adventure == "No" or adventure == "no"):
                                def BM():
                                        BorM = input("Do you prefer the beach or the mountains? : ")
                                        if (BorM == "Beach" or BorM == "beach"):
                                                print(" Wow! You're totally Ariel! Going with the flow of summer without a care just enjoying life! ")
                                        elif (BorM == "Mountains" or BorM == "mountains"):
                                                print("Your Disney princess is obviously Belle! Perhaps not as lively as others but you definitely like to relax when you can! ")
                                        else:
                                                print('I am sorry! Please type either "Beach" or "Mountains": ')
                                                BM()
                                BM()
                        else:
                                print('Please type "Yes" or "No"! ')
                                adven()
                adven()
        else:
                print('I am sorry! Please enter "Summer" or "Winter"! ')
                seas()
seas()