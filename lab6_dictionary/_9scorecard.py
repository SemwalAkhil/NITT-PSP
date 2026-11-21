match_data:dict[str,list] = {
    "Chennai Super Kings": [
        ("Ruturaj Gaikwad", 45, 0),
        ("Devon Conway", 32, 0),
        ("Ajinkya Rahane", 61, 0),
        ("Shivam Dube", 28, 0),
        ("Ravindra Jadeja", 15, 2),
        ("MS Dhoni", 12, 0),
        ("Deepak Chahar", 4, 3),
        ("Tushar Deshpande", 0, 2),
        ("Maheesh Theekshana", 2, 1),
        ("Matheesha Pathirana", 0, 2),
        ("Simarjeet Singh", 1, 0)
    ],
    "Mumbai Indians": [
        ("Rohit Sharma", 25, 0),
        ("Ishan Kishan", 38, 0),
        ("Suryakumar Yadav", 52, 0),
        ("Tilak Varma", 22, 0),
        ("Hardik Pandya", 14, 1),
        ("Tim David", 18, 0),
        ("Romario Shepherd", 8, 1),
        ("Jasprit Bumrah", 2, 3),
        ("Gerald Coetzee", 0, 2),
        ("Piyush Chawla", 1, 1),
        ("Akash Madhwal", 0, 1)
    ],
    "Royal Challengers Bengaluru": [
        ("Faf du Plessis", 35, 0),
        ("Virat Kohli", 74, 0),
        ("Glenn Maxwell", 12, 1),
        ("Cameron Green", 25, 2),
        ("Rajat Patidar", 42, 0),
        ("Dinesh Karthik", 28, 0),
        ("Karn Sharma", 4, 1),
        ("Reece Topley", 0, 2),
        ("Lockie Ferguson", 2, 2),
        ("Yash Dayal", 0, 1),
        ("Mohammed Siraj", 1, 1)
    ],
    "Kolkata Knight Riders": [
        ("Phil Salt", 48, 0),
        ("Sunil Narine", 85, 2),
        ("Shreyas Iyer", 38, 0),
        ("Venkatesh Iyer", 26, 0),
        ("Rinku Singh", 19, 0),
        ("Andre Russell", 15, 3),
        ("Ramandeep Singh", 10, 0),
        ("Mitchell Starc", 2, 2),
        ("Harshit Rana", 0, 2),
        ("Varun Chakravarthy", 0, 1),
        ("Suyash Sharma", 0, 0)
    ],
    "Sunrisers Hyderabad": [
        ("Travis Head", 89, 0),
        ("Abhishek Sharma", 65, 1),
        ("Heinrich Klaasen", 34, 0),
        ("Aiden Markram", 22, 0),
        ("Shahbaz Ahmed", 11, 1),
        ("Nitish Kumar Reddy", 18, 2),
        ("Pat Cummins", 6, 2),
        ("Bhuvneshwar Kumar", 2, 2),
        ("Jaydev Unadkat", 0, 1),
        ("T. Natarajan", 0, 3),
        ("Mayank Markande", 0, 0)
    ]
}
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