# 9. Write a program to find players and teams with maximum runs and wickets from cricket match data.
# Input: (2 CSK 2 "Ruturaj Gaikwad" 45 0 "Deepak Chahar" 4 3 MI 2 "Rohit Sharma" 25 0 "Jasprit Bumrah" 2 3), (1 CSK 1 "Dhoni" 50 0)
# Output:
#   Run 1:
#   Player with max runs Ruturaj Gaikwad - 45 runs
#   Player with max wickets Deepak Chahar - 3 wickets
#   Team with max runs CSK - 49 runs
#   Team with max wickets CSK - 3 wickets
#   Run 2:
#   Player with max runs Dhoni - 50 runs
#   Player with max wickets  - 0 wickets
#   Team with max runs CSK - 50 runs
#   Team with max wickets  - 0 wickets

num_teams = int(input("Enter number of teams: "))
match_data:dict[str,list] = {}
for i in range(num_teams):
    team_name = input("Enter team name: ")
    num_players = int(input("Enter number of players: "))
    p_list = []
    for j in range(num_players):
        p_name = input("Enter player name: ")
        runs = int(input("Enter runs: "))
        wickets = int(input("Enter wickets: "))
        p_list.append((p_name, runs, wickets))
    match_data[team_name] = p_list

max_run:tuple = ("",0,0)
max_wicket:tuple = ("",0,0) 
team_totals:dict[str,list] = {}
team_highest_score:tuple = ("",0)
team_highest_wicket:tuple = ("",0)

for team,players in match_data.items():
    team_totals[team] = [0,0]
    for player in players:
        if player[1] > max_run[1]:
            max_run = player
        if player[2] > max_wicket[2]:
            max_wicket = player
        team_totals[team][0] += player[1]
        team_totals[team][1] += player[2]
    if team_totals[team][0] > team_highest_score[1]:
        team_highest_score = (team,team_totals[team][0])
    if team_totals[team][1] > team_highest_wicket[1]:
        team_highest_wicket = (team,team_totals[team][1])

print(f"Player with max runs {max_run[0]} - {max_run[1]} runs")
print(f"Player with max wickets {max_wicket[0]} - {max_wicket[2]} wickets")
print(f"Team with max runs {team_highest_score[0]} - {team_highest_score[1]} runs")
print(f"Team with max wickets {team_highest_wicket[0]} - {team_highest_wicket[1]} wickets")
