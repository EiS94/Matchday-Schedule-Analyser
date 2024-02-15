import Season
from League import League
from Criteria import Criteria

season = Season.create_season(League.BUNDESLIGA_2, 2024)
season.analyze_season()

season.analyze_schedule(Criteria.OPPONENT_SHAPE)
