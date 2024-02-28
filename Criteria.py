from enum import Enum


class Criteria(Enum):
    # oppenent_shape calculates the average points per game of the last 3 games of the opponent
    OPPONENT_SHAPE = "opponent_shape"
    OPPONENT_POINTS = "opponent_points"
    OPPONENT_RANKING = "opponent_ranking"
