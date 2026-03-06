# Group10_P2
Functions are us - P2

def get_home_team():
    """
    Ask the user for the home team name and number of games.
    Returns the team name and number of games.
    """

    # Ask user for team name
    sTeamName = input("Enter the name of your home team: ")

    # Ask user how many games they will play
    iNumGames = int(input(f"Enter the number of games that {sTeamName} will play: "))

    return sTeamName, iNumGames

def main():

    # Dictionary required by assignment
    dictTeams = {"Won Against": [], "Lost Against": []}

    # Counters
    wins = 0
    losses = 0

    # Call introduction function
    sTeamName, iNumGames = get_home_team()

    # Loop through games
    for game in range(1, iNumGames + 1):

        # Call function to get opponent name
        sAwayTeam = get_opponent(game)

        # Play the game
        result = play_game(sTeamName, sAwayTeam, dictTeams)

        # Update win/loss counters
        if result == "W":
            wins += 1
        else:
            losses += 1

    # Display season results
    display_results(sTeamName, wins, losses, dictTeams, iNumGames)
