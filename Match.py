class Match:

    def __init__(self, home_team, away_team, home_goals, away_goals):
        self.home_team = home_team
        self.away_team = away_team
        self.home_goals = home_goals
        self.away_goals = away_goals
        self.home_team.matches.append(self)
        self.away_team.matches.append(self)

    def __str__(self):
        return f"{self.home_team.name} {self.home_goals}:{self.away_goals} {self.away_team.name}"

    def get_winner(self):
        if self.home_goals > self.away_goals:
            return self.home_team
        elif self.away_goals > self.home_goals:
            return self.away_team
        else:
            return None
