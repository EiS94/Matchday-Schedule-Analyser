## Matchday-Schedule-Analyser

### What is this?

With this script you can find out which football teams were particularly lucky with the matchday scheduling.
You can analyze according to 3 criteria:
- Average points of the opponent in the last 3 games before the respective game
- Average table position before the respective match
- Total number of points of the opponents before the respective match

### Example Result
```
Durchschnittliche Punkte der Gegner aus den vorherigen 3 Spielen zum Zeitpunkt der Begegnungen:
 1. VfB Stuttgart            2.70
 2. FC Augsburg              2.87
 3. Borussia Mönchengladbach 2.91
 4. Eintracht Frankfurt      3.30
 5. Bayer Leverkusen         3.39
 6. VfL Bochum               3.61
 7. RB Leipzig               3.65
 8. Borussia Dortmund        3.70
 9. SC Freiburg              3.78
10. FC Bayern München        3.83
11. Werder Bremen            3.83
12. SV Darmstadt 98          3.87
13. 1. FSV Mainz 05          3.91
14. VfL Wolfsburg            3.96
15. 1. FC Heidenheim 1846    4.17
16. TSG 1899 Hoffenheim      4.43
17. 1. FC Union Berlin       4.52
18. 1. FC Köln               4.96
```

### How to use

Customize the main class to get the desired league, year and criterion

```
import Season
from League import League
from Criteria import Criteria

season = Season.create_season(League.BUNDESLIGA_1, 2024)
season.analyze_season()

season.analyze_schedule(Criteria.OPPONENT_SHAPE)
```
