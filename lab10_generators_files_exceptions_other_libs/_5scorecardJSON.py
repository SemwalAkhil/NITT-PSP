# 5. Write a program to read cricket match stats from a CSV file, find best player and team, and save to JSON.
# Input: (1 result_clean.json), (2 result_errors.json)
# Output:
#   Run 1:
#   Match result saved to JSON: {'best_player': {'name': 'Travis Head', 'runs': 89}, 'best_team': {'name': 'Sunrisers Hyderabad', 'runs': 247}}
#   Run 2:
#   Skipping invalid player record 'Deepak Chahar'
#   Skipping invalid player record 'Jasprit Bumrah'
#   Match result saved to JSON: {'best_player': {'name': 'Rohit Sharma', 'runs': 50}, 'best_team': {'name': 'MI', 'runs': 50}}

import csv
import json
import os

sample_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample_data")
choice = input("Use sample data? (1 = clean, 2 = with errors, 0 = type my own): ").strip()

if choice == "1":
    csv_file = os.path.join(sample_dir, "match_data_clean.csv")
elif choice == "2":
    csv_file = os.path.join(sample_dir, "match_data_errors.csv")
else:
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

if choice in ("1", "2"):
    json_file = input("Enter JSON output filename: ")

try:
    with open(csv_file, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        best_player = ("", 0)
        team_totals = {}
        for row in reader:
            if not row or len(row) < 4:
                continue
            team, player = row[0], row[1]
            try:
                runs, wickets = int(row[2]), int(row[3])
            except ValueError:
                print(f"Skipping invalid player record '{player}'")
                continue
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
