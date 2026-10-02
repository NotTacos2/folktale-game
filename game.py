import time
import random

stillalive = True
money = 0
place = "forest"

while stillalive:
    if place == "forest":
        print("You are in a forest, Lost and confused on where you're going, There's a castle there, do you want to go in?")
        print("'Y' for yes, 'N' for no")

        time.sleep(0.3)

        answer = input("Y or N: ")

        if answer == "Y":
            print("Going in!")
            time.sleep(1)
            place = "castle"
        elif answer == "N":
            print("You didn't go in, but wandered around. Something shot you in the back, you are dead.")
            print("Game over.")
            time.sleep(0.5)
            stillalive = False
        else:
            print("Response invalid")
    elif place == "castle":
        print("You are in the castle, however it's dark in there. There are 2 rooms, dining room and upstairs")
        print("Where would you go?")
        print("'D' for dining, 'U' for upstairs")

        time.sleep(0.3)

        answer = input("D or U: ")

        if answer == "D":
            print("Going in dining room!")
            time.sleep(1)
            randomnum = random.randint(1,2)
            if randomnum == 1:
                print("Turns out a knight was standing there and he spotted you and stabbed you with his sword. You are dead.")
                print("Game over.")
                time.sleep(0.5)
                stillalive = False
                break
            elif randomnum == 2:
                print("You walk in and you saw a plate of food. You ate and gained some energy. However there's a pot of gold in one of the plates, would you take it?")
                print("'Y' for yes, 'N' for no")

                time.sleep(0.3)

                answer = input("Y or N: ")

                if answer == "Y":
                   randomnum = random.randint(1,2)
                   if randomnum == 1: 
                    print("Turns out a knight just walked in and stabbed you. You are dead.")
                    print("game over.")
                    time.sleep(0.5)
                    stillalive = False
                    break
                   if randomnum == 2:
                    money += 500
                    print("You grabbed the gold and gained some money. Great job! You head back and saw a room that wasn't there before.")
                    print("It was a room towards the dungeon. Do you want to go upstairs or to the dungeon?")
                    print("'U' for upstairs, 'D' for dungeon")

                    time.sleep(0.3)

                    answer = input("U or D: ")
                    if answer == "U":
                        print("Going in upstairs!")
                        time.sleep(1)
                        randomnum = random.randint(1,2)
                        if randomnum == 1:
                            print("Turns out there was a banana peel and you slipped on it. Your head hits on the bear trap and you are dead.")
                            print("Game over.")
                            time.sleep(0.5)
                            stillalive = False
                            break
                        elif randomnum == 2:
                            print("You walk up and there are 3 rooms, which one would you go?")
                            print("'1' for room 1, '2' for room 2, '3' for room 3")

                            time.sleep(0.3)

                            answer = input("1 or 2 or 3: ")
                            if answer == "1":
                                print("Turns out room 1 was a trap and you got stabbed behind and you are dead.")
                                print("Game over.")
                                time.sleep(0.5)
                                stillalive = False
                                break
                            elif answer == "2":
                                print("Turns out room 2 was a trap and you got stabbed behind and you are dead.")
                                print("Game over.")
                                time.sleep(0.5)
                                stillalive = False
                                break
                            elif answer == "3":
                                print("Turns out room 3 had nothing and you head back to the main lobby, Are you going to the dungeon or leave?")
                                print("'D' for dungeon, 'L for leave'")
                                time.sleep(0.5)
                                answer = input("D or L: ")
                                if answer == "L":
                                    print("You have successfully escape! Great work! You gained" + money + " coins. Thanks for playing!")
                                    time.sleep(0.5)
                                    stillalive = False
                                    break
                                elif answer == "D":
                                    print("Turns out the dungeon was a trap and the knight has trapped you inside. Game over.")
                                    time.sleep(0.5)
                                    stillalive = False
                                    break
                                else:
                                    print("Response invalid")  
                            else:
                                print("Response invalid")    
                    else:
                        print("Response invalid")
                elif answer == "N":
                    print("You head back and saw a room that wasn't there before.")
                    print("It was a room towards the dungeon. Do you want to go upstairs or to the dungeon?")
                    print("'U' for upstairs, 'D' for dungeon")

                    time.sleep(0.3)

                    answer = input("U or D: ")
                    if answer == "U":
                        print("Going in upstairs!")
                        time.sleep(1)
                        randomnum = random.randint(1,2)
                        if randomnum == 1:
                            print("Turns out there was a banana peel and you slipped on it. Your head hits on the bear trap and you are dead.")
                            print("Game over.")
                            time.sleep(0.5)
                            stillalive = False
                            break
                        elif randomnum == 2:
                            print("You walk up and there are 3 rooms, which one would you go?")
                            print("'1' for room 1, '2' for room 2, '3' for room 3")

                            time.sleep(0.3)

                            answer = input("1 or 2 or 3: ")
                            if answer == "1":
                                print("Turns out room 1 was a trap and you got stabbed behind and you are dead.")
                                print("Game over.")
                                time.sleep(0.5)
                                stillalive = False
                                break
                            elif answer == "2":
                                print("Turns out room 2 was a trap and you got stabbed behind and you are dead.")
                                print("Game over.")
                                time.sleep(0.5)
                                stillalive = False
                                break
                            elif answer == "3":
                                print("Turns out room 3 had nothing and you head back to the main lobby, Are you going to the dungeon or leave?")
                                print("'D' for dungeon, 'L for leave'")
                                time.sleep(0.5)
                                answer = input("D or L: ")
                                if answer == "L":
                                    print("You have successfully escape! Great work! You gained" + money + " coins. Thanks for playing!")
                                    time.sleep(0.5)
                                    stillalive = False
                                    break
                                elif answer == "D":
                                    print("Turns out the dungeon was a trap and the knight has trapped you inside. Game over.")
                                    time.sleep(0.5)
                                    stillalive = False
                                    break
                                else:
                                    print("Response invalid")  
                            else:
                                print("Response invalid")
                    elif answer == "D":
                        print("Turns out the dungeon was a trap and the knight has trapped you inside. Game over.")
                        time.sleep(0.5)
                        stillalive = False  
                        break  
                else:
                    print("Response invalid")

        if answer == "U":
            print("Going in upstairs!")
            time.sleep(1)
            randomnum = random.randint(1,2)
            if randomnum == 1:
                print("Turns out there was a banana peel and you slipped on it. Your head hits on the bear trap and you are dead.")
                print("Game over.")
                time.sleep(0.5)
                stillalive = False
                break
            elif randomnum == 2:
                print("You walk up and there are 3 rooms, which one would you go?")
                print("'1' for room 1, '2' for room 2, '3' for room 3")

                time.sleep(0.3)

                answer = input("1 or 2 or 3: ")
                if answer == "1":
                    print("Turns out room 1 was a trap and you got stabbed behind and you are dead.")
                    print("Game over.")
                    time.sleep(0.5)
                    stillalive = False
                    break
                elif answer == "2":
                    print("Turns out room 2 was a trap and you got stabbed behind and you are dead.")
                    print("Game over.")
                    time.sleep(0.5)
                    stillalive = False
                    break
                elif answer == "3":
                    print("Turns out room 3 had nothing and you head back to the main lobby, Are you going to the dungeon or leave?")
                    print("'D' for dungeon, 'L for leave'")
                    time.sleep(0.5)
                    answer = input("D or L: ")
                    if answer == "L":
                        print("You have successfully escape! Great work! You gained" + str(money) + " coins. Thank you for playing!")
                        time.sleep(0.5)
                        stillalive = False
                        break
                    elif answer == "D":
                        print("Turns out the dungeon was a trap and the knight has trapped you inside. Game over.")
                        time.sleep(0.5)
                        stillalive = False
                        break
                    else:
                        print("Response invalid")
                else:
                    print("Response invalid")   
              
        else:
            print("Response invalid")


