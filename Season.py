from datetime import datetime
import requests
import json

import Table
from Team import Team
import Matchday

from tqdm import tqdm


class Season:

    def __init__(self, year):
        self.year = year
        self.teams = []
        # detect min and max matches of all teams in not completed seasons
        self.min_matches = 35
        self.max_matches = 0
        self.matchdays = []

    def __str__(self):
        result = f"Saison {self.year}/{self.year + 1}\nTeams:\n"
        for team in self.teams:
            result += f"- {team.name}\n"
        return result

    def get_team(self, name):
        for team in self.teams:
            if team.name == name:
                return team

    def analyze_season(self):
        for i in tqdm(range(1, self.max_matches + 1)):
            url = f"https://api.openligadb.de/getmatchdata/bl1/{self.year}/{i}"
            request = requests.get(url)

            result = json.loads(request.text)
            self.matchdays.append(Matchday.parse_matchday(i, result, self.teams))

        for matchday in self.matchdays:
            matchday.table = Table.calculate_table(self.teams, matchday.number)

    def analyze_schedule(self, criteria="opponent_ranking"):
        if self.min_matches != self.max_matches:
            print("Not every team has the same amount of matches. This could lead to errors in result.")

        for i in range(1, self.min_matches):
            matchday = self.matchdays[i]
            matchday_before = self.matchdays[i - 1]
            for match in matchday.matches:
                match.home_team.schedule_points += matchday_before.get_team_schedule_points(match.away_team, criteria)
                match.away_team.schedule_points += matchday_before.get_team_schedule_points(match.home_team, criteria)

        self.teams = sorted(self.teams, key=lambda x: x.schedule_points)
        if criteria == "opponent_ranking" or criteria == "opponent_shape":
            for team in self.teams:
                team.schedule_points = team.schedule_points / self.min_matches

        for team in self.teams:
            print(team.name.ljust(25) + str(team.schedule_points))
        # else:
        # TODO name other criteria
        #    raise Exception(
        #        f"Error while analyzing schedule: Unknown criteria {criteria}.\nUse one of the following: 'opponent_ranking, '")


def create_season(year):
    year = int(year) - 1
    if year < 2001 or year > datetime.now().year + 1:
        raise Exception(f"Please select a year between 2001 and {datetime.now().year} + 1")

    season = Season(year)

    # detect all teams of the season
    url = f"https://api.openligadb.de/getbltable/bl1/{year}"
    request = requests.get(url)
    if request.status_code != 200:
        raise Exception(f"Error while getting teams for season {year}\n{url} raised status-code {request.status_code}")
    else:
        result = json.loads(request.text)
        for team in result:
            season.teams.append(Team(team["teamName"], team["teamIconUrl"]))
            if team["matches"] > season.max_matches:
                season.max_matches = team["matches"]
            if team["matches"] < season.min_matches:
                season.min_matches = team["matches"]

    return season
