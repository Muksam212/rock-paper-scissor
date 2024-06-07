

from random import choice

dictt = {'r': 'Rock', 's': 'Scissor', 'p': 'Paper'}

Home = 0 #score for first player

Away = 0 #score for computer player

print("Rock...Paper...Scissor...Shoot!!!")
play = True

#game logic
while play:
    random_choice = ['r', 's', 'p']
    X = choice(random_choice) # X is computer move

    #get move of player (main player)
    prompt = input("Make a move (r, p, s) or 'q' to exit :  ")

    #whenever there is tie
    if prompt == 'p' or prompt == 's' or prompt == 'r':
        if prompt == X:
            print("It's a tie")
            print("Home: " + str(Home) + '--' + "Away: " + str(Away))

        #this is cases where player (prompt) is going to win
        elif (prompt == 's' and X == 'p') or \
                (prompt == 'p' and X == 'r') or (prompt == 'r' and X == 's'):

            print(f"Computer chose {dictt[X]} and I chose {dictt[prompt]}, Player won")
            Home = Home + 1
            print("Home: " + str(Home) + '--' + "Away: " + str(Away))


        else:
            print(f"Computer chose {dictt[X]} and I chose {dictt[prompt]}, Computer won")
            Away = Away + 1
            print("Home: " + str(Home) + '--' + "Away: " + str(Away))

    elif prompt == 'q':
        print("Home: " + str(Home) + '--' + "Away: " + str(Away))
        play = False

    else:
        print("Invalid input")
