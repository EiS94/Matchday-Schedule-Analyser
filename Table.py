class Table:

    def __init__(self, ranking, matchday_number):
        self.ranking = ranking
        self.matchday_number = matchday_number

    def __str__(self):
        result = ""
        counter = 1
        for team_tuple in self.ranking:
            result += f"{counter}. {team_tuple[0].name}, "
            counter += 1
        return result[:-2]

    def pretty_print_table(self):
        result = ""
        counter = 1
        for team_tuple in self.ranking:
            # ranking and team name
            result += str(counter).rjust(2) + ". " + team_tuple[0].name.ljust(25)
            # number of matches and goals
            result += str(self.matchday_number).rjust(2).ljust(5) + str(team_tuple[3]).rjust(3)
            # goals against and points
            result += ":" + str(team_tuple[4]).rjust(3).ljust(5) + str(team_tuple[1]).rjust(3) + "\n"

            counter += 1
        return result


def table_sorter(item):
    return -item[1], -item[2], -item[3], item[4]


def calculate_table(teams, matchday_number):
    team_tuples = []
    for team in teams:
        if len(team.matches) < matchday_number:
            raise Exception(f"Error while calculating table for matchday number {matchday_number}")

        points = team.get_points_after_x_matches(matchday_number)
        goal_difference = team.get_goal_difference_after_x_matches(matchday_number)
        goals = team.get_goals_after_x_matches(matchday_number)
        goals_against = team.get_goals_against_after_x_matches(matchday_number)

        team_tuples.append((team, points, goal_difference, goals, goals_against))

    sorted_table = sorted(team_tuples, key=table_sorter)

    return Table(sorted_table, matchday_number)
