# 7. Write a function to determine the best team and best player from a tournament statistics dictionary.
# Input: (2 CSK 2 Dhoni 50 0 Jadeja 40 2 MI 2 Rohit 85 0 Bumrah 10 3), (1 RCB 1 Kohli 100 0)
# Output: ('MI', 'Rohit'), ('RCB', 'Kohli')

def getBestTeamAndPlayer(tournament: dict):
    best_team = ("", 0)
    best_player = ("", 0)

    for team, players in tournament.items():
        team_runs = 0
        for p in players:
            name = p[0]
            runs = p[1]
            team_runs += runs
            if runs > best_player[1]:
                best_player = (name, runs)
        if team_runs > best_team[1]:
            best_team = (team, team_runs)

    return (best_team[0], best_player[0])

if __name__ == "__main__":
    tourney = {}
    n_teams = int(input("Enter number of teams: "))
    for i in range(n_teams):
        team = input("Enter team name: ")
        n_players = int(input("Enter number of players: "))
        plist = []
        for j in range(n_players):
            name = input("Enter player name: ")
            runs = int(input("Enter runs: "))
            wickets = int(input("Enter wickets: "))
            plist.append((name, runs, wickets))
        tourney[team] = plist
    print(getBestTeamAndPlayer(tourney))
