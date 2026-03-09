# -------------------------------------------------------
# Team Members:
# Kimball Mueller
# Student 2
# Student 3
#
# A6 Soccer Teams Program
# Rewritten using functions from Assignment 5
# -------------------------------------------------------

import random


def get_home_team():

    sTeamName = input("Enter the name of your home team: ")
    iNumGames = int(input(f"Enter the number of games that {sTeamName} will play: "))

    return sTeamName, iNumGames


def get_opponent(game_number):

    sAwayTeam = input(f"\nEnter the name of the away team for game {game_number}: ")

    return sAwayTeam


def play_game(home_team, away_team, dictTeams):

    homeScore = random.randint(0, 3)
    awayScore = random.randint(0, 3)

    while homeScore == awayScore:
        homeScore = random.randint(0, 3)
        awayScore = random.randint(0, 3)

    print(f"{home_team}'s score: {homeScore} - {away_team}'s score: {awayScore}")

    if homeScore > awayScore:
        dictTeams["Won Against"].append(away_team)
        return "W"
    else:
        dictTeams["Lost Against"].append(away_team)
        return "L"


def display_results(home_team, wins, losses, dictTeams, total_games):

    print("\nTeams won against:")
    for team in dictTeams["Won Against"]:
        print("  " + team)

    print("\nTeams lost against:")
    for team in dictTeams["Lost Against"]:
        print("  " + team)

    print(f"\nFinal season record: {wins} - {losses}")

    winPct = wins / total_games

    if winPct >= 0.75:
        print("Qualified for the NCAA Soccer Tournament!")
    elif winPct >= 0.50:
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