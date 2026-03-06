
#Author Adriel Makaio Villarreal
# Step 4-5

import random, math


def play_game(sHometeam, sAwayTeam):

    sHometeam= 0
    sAwayTeam = 0

    while not(sHometeam == sAwayTeam) :
        iHomeScore = random.randrange(0,9)
        iAwayScore = random.randrange(0.9)

    if iHomeScore > iAwayScore :
        return "W"
    else :
        return "L"
    


def display_final_record(iwins, iloss, lstOfTeamsWon, lstOfTeamsLost) :

    #how are we storing whether we win or loose in the team dict, is the input a list a
    #repating call.


    print("\nTeam Wons agaist:")
    print(*lstOfTeamsWon, sep="\n")


    print("\nTeam Lost agaist:")
    print(*lstOfTeamsLost, sep="\n")


    print(f"Final season record {iwins} - {iloss}")
    totalGames = iwins + iloss

    if iwins >= math.floor((totalGames * .75)) :
        print("Qualified for the NCAA Soccer Tournament!\n")

    elif iwins >= math.floor((totalGames * .50)) :
        print("You had a good season.\n")

    else :
        print("Your team needs to practice!\n")


  
    