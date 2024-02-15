from Match import Match


class Matchday:

    def __init__(self, number):
        self.number = number
        self.table = None
        self.matches = []

    def get_team_schedule_points(self, team, criteria):
        counter = 1
        for team_tuple in self.table.ranking:
            if team_tuple[0] == team:
                if criteria.value == "opponent_ranking":
                    return counter
                elif criteria.value == "opponent_points":
                    return team_tuple[1]
                elif criteria.value == "opponent_shape":
                    shape_points = 0
                    counter = 0
                    for i in range(3):
                        if self.number - 1 - i < 0:
                            break
                        match = team_tuple[0].matches[self.number - 1 - i]
                        winner = match.get_winner()
                        if winner is None:
                            shape_points += 1
                        elif winner == team_tuple[0]:
                            shape_points += 3
                        counter += 1
                    return shape_points / counter
            counter += 1
        raise Exception(f"Team {team.name} not found.")

    def __str__(self):
        return f"{self.number}. Spieltag"


def get_team(name, teams):
    for team in teams:
        if team.name == name:
            return team


def parse_matchday(number, json_data, teams):
    matchday = Matchday(number)

    for match in json_data:
        home_team = get_team(match["team1"]["teamName"], teams)
        away_team = get_team(match["team2"]["teamName"], teams)
        for match_result in match["matchResults"]:
            if match_result["resultName"] == "Endergebnis":
                home_goals = match_result["pointsTeam1"]
                away_goals = match_result["pointsTeam2"]

                matchday.matches.append(Match(home_team, away_team, home_goals, away_goals))

    return matchday
