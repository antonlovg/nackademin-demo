import övning14x_ui as ui

teams = {
    'Brazil': {
        'wins': 0,
        'draws': 0,
        'losses': 0,
        'goals_for': 0,
        'goals_against': 0
    },
    'Serbia': {
        'wins': 0,
        'draws': 0,
        'losses': 0,
        'goals_for': 0,
        'goals_against': 0
    },
    'Switzerland': {
        'wins': 0,
        'draws': 0,
        'losses': 0,
        'goals_for': 0,
        'goals_against': 0
    },
    'Costa Rica': {
        'wins': 0,
        'draws': 0,
        'losses': 0,
        'goals_for': 0,
        'goals_against': 0
    }
}


# Enklaste sättet att lösa denna uppgift på blir då att först kolla mål som släpps in samt görs, sen kan man jämföra
# det och lägga in += 1 på wins eller draws om det blev lika


def add_game(home_team, home_score, away_team, away_score):
    teams[home_team]["goals_for"] += home_score
    teams[home_team]["goals_against"] += away_score
    teams[away_team]["goals_for"] += away_score
    teams[away_team]["goals_against"] += home_score

    if home_score > away_score:
        teams[home_team]["wins"] += 1
        teams[away_team]["losses"] += 1
    elif away_score > home_score:
        teams[away_team]["wins"] += 1
        teams[home_team]["losses"] += 1
    else:  # oavgjort
        teams[home_team]["draws"] += 1
        teams[away_team]["draws"] += 1


def make_list(dict):
    resultat = []


# 17 June 2018 #
add_game("Costa Rica", 0, "Serbia", 1)
add_game("Brazil", 1, "Switzerland", 1)
# 22 June 2018 #
add_game("Brazil", 2, "Costa Rica", 0)
add_game("Serbia", 1, "Switzerland", 2)
# 27 June 2018 #
add_game("Serbia", 0, "Brazil", 2)
add_game("Switzerland", 2, "Costa Rica", 2)

ui.linjer()
ui.title()
ui.linjer()
for team, stats in teams.items():
    ui.ställning(
        f"{team.ljust(12)} | {stats['wins']} | {stats['draws']} | {stats['losses']} |  {stats['goals_for']} |  {stats['goals_against']} |")
ui.linjer()
