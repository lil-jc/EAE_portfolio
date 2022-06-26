# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():

    # Ensure correct usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []
    # TODO: Read teams into memory from file
    filename = sys.argv[1]
    with open(filename) as file:
        # the csv.DictReader funtion read csv files like a dictionary (right side corresond to left side)
        reader = csv.DictReader(file)

        # for t in reader makes (t = one row in csv file) skiping thr header
        for t in reader:
            # change the data type in csv file for rating to a int and put it back
            t["rating"] = int(t["rating"])
            teams.append(t)

    counts = {}
    # TODO: Simulate N tournaments and keep track of win counts
    for i in range(N):
        # run simulate_tournament and store return value in winner
        winner = simulate_tournament(teams)

        # if winner is ald recoreded in count: increment winner
        if winner in counts:
            counts[winner] += 1
        # if winner is not ald recorded in count add winner and set winner to 1
        else:
            counts[winner] = 1

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # TODO
    while len(teams) > 1:
        # simulate_round() will append the winners to team and will end up with only one winner
        teams = simulate_round(teams)
    # return the first and only winner left in (teams of "team") to get team name
    return teams[0]["team"]


if __name__ == "__main__":
    main()