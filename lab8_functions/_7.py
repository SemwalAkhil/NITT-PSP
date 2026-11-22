# 7. Write a function to determine the best team and best player from a tournament statistics dictionary.
# Input: tourney={"CSK": [("Dhoni", 50, 0), ("Jadeja", 40, 2)], "MI": [("Rohit", 85, 0), ("Bumrah", 10, 3)]}
# Output: ('MI', 'Rohit')

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
    tourney = {
        "CSK": [("Dhoni", 50, 0), ("Jadeja", 40, 2)],
        "MI": [("Rohit", 85, 0), ("Bumrah", 10, 3)]
    }
    print(getBestTeamAndPlayer(tourney))
