# 5. Write a program to read cricket match stats from a CSV file, find best player and team, and save to JSON.
# Input: (match_data.csv match_result.json 4 CSK "Ruturaj Gaikwad" 45 0 CSK "Deepak Chahar" 4 3 SRH "Travis Head" 89 0 SRH "Pat Cummins" 6 2), (m.csv r.json 1 MI Rohit 50 0)
# Output:
#   Run 1:
#   Match result saved to JSON: {'best_player': {'name': 'Travis Head', 'runs': 89}, 'best_team': {'name': 'SRH', 'runs': 95}}
#   Run 2:
#   Match result saved to JSON: {'best_player': {'name': 'Rohit', 'runs': 50}, 'best_team': {'name': 'MI', 'runs': 50}}

import csv
import json

csv_file = input("Enter CSV filename: ")
json_file = input("Enter JSON output filename: ")
n = int(input("Enter number of players: "))

sample_data = [["Team", "Player", "Runs", "Wickets"]]
for i in range(n):
    team = input("Enter team: ")
    player = input("Enter player: ")
    runs = input("Enter runs: ")
    wickets = input("Enter wickets: ")
    sample_data.append([team, player, runs, wickets])

with open(csv_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(sample_data)

try:
    with open(csv_file, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        best_player = ("", 0)
        team_totals = {}
        for row in reader:
            team, player, runs, wickets = row[0], row[1], int(row[2]), int(row[3])
            team_totals[team] = team_totals.get(team, 0) + runs
            if runs > best_player[1]:
                best_player = (player, runs)

    best_team = max(team_totals.items(), key=lambda x: x[1])
    result = {
        "best_player": {"name": best_player[0], "runs": best_player[1]},
        "best_team": {"name": best_team[0], "runs": best_team[1]}
    }
    with open(json_file, "w") as f:
        json.dump(result, f, indent=4)
    print("Match result saved to JSON:", result)
except FileNotFoundError:
    print("CSV match data not found")
