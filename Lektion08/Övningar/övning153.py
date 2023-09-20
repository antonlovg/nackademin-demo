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


def make_list(result_dict):
    # 1. Skapa en tom lista
    resultat = []
    # 2. Iterera över dictionary
    for country in result_dict:
        # 2.1 Skapar nytt dictionary
        country_dict = {
            'country': country,
            'wins': teams[country]['wins'],
            'draws': teams[country]['draws'],
            'losses': teams[country]['losses'],
            'goals_for': teams[country]['goals_for'],
            'goals_against': teams[country]['goals_against'],
        }
        # 2.2 Lägg in den i dictionary
        resultat.append(country_dict)

    # 3 Skriv ut listan
    return resultat


# Räkna ut poäng
def sort_key(item):
    return item['wins'] * 3 + item['draws']

def sort_list(result_list):
    # reverse=True för att det ska vara flest poäng först
    sorted_list = sorted(result_list, key=sort_key, reverse=True)
    return sorted_list


def print_table(lista):
    print("-" * 50)
    print("| # |", "Nation".ljust(11), "| W | D | L | GF | GA | GD | P |")
    print("-" * 50)
    nummer = 1
    for i in lista:
        c = i['country']
        w = i['wins']
        d = i['draws']
        l = i['losses']
        gf = i['goals_for']
        ga = i['goals_against']
        gd = str(i['goals_for'] - i['goals_against'])
        p = (w * 3) + d
        print(
            f"| {nummer} | {c.ljust(11)} | {w} | {d} | {l} |  {gf} |  {ga} | {gd.rjust(2)} | {p} |")  # i = index eller item
        nummer += 1
    print("-" * 50)


# 17 June 2018 #
add_game("Costa Rica", 0, "Serbia", 1)
add_game("Brazil", 1, "Switzerland", 1)
# 22 June 2018 #
add_game("Brazil", 2, "Costa Rica", 0)
add_game("Serbia", 1, "Switzerland", 2)
# 27 June 2018 #
add_game("Serbia", 0, "Brazil", 2)
add_game("Switzerland", 2, "Costa Rica", 2)

# Anropa funktionen
teams_list = make_list(teams)
teams_list_sorted = sort_list(teams_list)
print_table(teams_list_sorted)
