class Team:

    def __init__(self, name, icon_url):
        self.name = name
        self.icon_url = icon_url
        self.matches = []
        self.schedule_points = 0

    def get_points_after_x_matches(self, x):
        if x > len(self.matches):
            raise Exception(
                f"Points after {x} matches for {self.name} cannot be calculated. Only {len(self.matches)} matches are available")
        points = 0
        for i in range(x):
            winning_team = self.matches[i].get_winner()
            if winning_team is None:
                points += 1
            elif winning_team == self:
                points += 3
        return points

    def get_goals_after_x_matches(self, x):
        if x > len(self.matches):
            raise Exception(
                f"Goals after {x} matches for {self.name} cannot be calculated. Only {len(self.matches)} matches are available")
        goals = 0
        for i in range(x):
            match = self.matches[i]
            if match.home_team == self:
                goals += match.home_goals
            else:
                goals += match.away_goals
        return goals

    def get_goals_against_after_x_matches(self, x):
        if x > len(self.matches):
            raise Exception(
                f"Goals against after {x} matches for {self.name} cannot be calculated. Only {len(self.matches)} matches are available")
        goals_against = 0
        for i in range(x):
            match = self.matches[i]
            if match.home_team == self:
                goals_against += match.away_goals
            else:
                goals_against += match.home_goals
        return goals_against

    def get_goal_difference_after_x_matches(self, x):
        if x > len(self.matches):
            raise Exception(
                f"Goal difference against after {x} matches for {self.name} cannot be calculated. Only {len(self.matches)} matches are available")
        return self.get_goals_after_x_matches(x) - self.get_goals_against_after_x_matches(x)

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        result = f"{self.name}, Punkte: {self.get_points_after_x_matches(len(self.matches))}"
        result += f", Tore: {self.get_goals_after_x_matches(len(self.matches))}:{self.get_goals_against_after_x_matches(len(self.matches))}"
        return result
