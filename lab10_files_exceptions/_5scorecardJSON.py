import csv
import json

csv_file = "match_data.csv"
json_file = "match_result.json"

sample_data = [
    ["Team", "Player", "Runs", "Wickets"],
    ["CSK", "Ruturaj Gaikwad", "45", "0"],
    ["CSK", "Deepak Chahar", "4", "3"],
    ["SRH", "Travis Head", "89", "0"],
    ["SRH", "Pat Cummins", "6", "2"]
]

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
