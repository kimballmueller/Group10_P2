#
# -------------------------------------------------------
# Team Members:
# Kimball Mueller
# Adriel Makaio Villarreal
# Jane Jeppesen
#
# A6 Soccer Teams Program
# -------------------------------------------------------

import random
import math

# Jane's Section
# Get team name input


def get_home_team():

    sTeamName = input("Enter the name of your home team: ")
    iNumGames = int(input(f"Enter the number of games that {sTeamName} will play: "))

    return sTeamName, iNumGames

# Kimball's Section
# Get team name input

def get_opponent(game_number):

    sAwayTeam = input(f"\nEnter the name of the away team for game {game_number}: ")
    return sAwayTeam


# ---- Adriel's section (fixed but same logic * Kimball Mueller) ----
def play_game(sHometeam, sAwayTeam, dictTeams):

    # generate scores
    iHomeScore = random.randrange(0, 9)
    iAwayScore = random.randrange(0, 9)

    # prevent ties
    while iHomeScore == iAwayScore:
        iHomeScore = random.randrange(0, 9)
        iAwayScore = random.randrange(0, 9)

    print(f"{sHometeam}'s score: {iHomeScore} - {sAwayTeam}'s score: {iAwayScore}")

    if iHomeScore > iAwayScore:
        dictTeams["Won Against"].append(sAwayTeam)
        return "W"
    else:
        dictTeams["Lost Against"].append(sAwayTeam)
        return "L"


# ---- Adriel's display logic adapted -  fixed but same logic * Kimball Mueller ----
def display_results(home_team, iwins, iloss, dictTeams, totalGames):

    lstOfTeamsWon = dictTeams["Won Against"]
    lstOfTeamsLost = dictTeams["Lost Against"]

    print("\nTeams won against:")
    print(*lstOfTeamsWon, sep="\n")

    print("\nTeams lost against:")
    print(*lstOfTeamsLost, sep="\n")

    print(f"\nFinal season record {iwins} - {iloss}")

    if iwins >= math.floor((totalGames * .75)):
        print("Qualified for the NCAA Soccer Tournament!")

    elif iwins >= math.floor((totalGames * .50)):
        print("You had a good season.")

    else:
        print("Your team needs to practice!")


def main():

    dictTeams = {"Won Against": [], "Lost Against": []}

    wins = 0
    losses = 0

    sTeamName, iNumGames = get_home_team()

    for game in range(1, iNumGames + 1):

        sAwayTeam = get_opponent(game)

        result = play_game(sTeamName, sAwayTeam, dictTeams)

        if result == "W":
            wins += 1
        else:
            losses += 1

    display_results(sTeamName, wins, losses, dictTeams, iNumGames)


main()
