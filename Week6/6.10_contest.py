num_students = int(input())

team_counts = {}

for i in range(num_students):
    student, team = input().split()
    
    if team in team_counts:
        team_counts[team] += 1
    else:
        team_counts[team] = 1

for team in team_counts:
    print(team, team_counts[team])


largest_team = ""
highest_count = 0

for team in team_counts:
    if team_counts[team] > highest_count:
        highest_count = team_counts[team]
        largest_team = team

print(f"Largest Team: {largest_team}")