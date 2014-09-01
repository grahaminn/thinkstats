import numpy
import thinkstats

# 10 consecutive shots from 15

odds_of_streak_within_shots = ((2 * (2 ** 4)) + (6 * (2 ** 3)) + (4 * (2 ** 2)) + 11)  / (2.0 ** 15)
print 'odds of streak within shots:', odds_of_streak_within_shots
odds_no_streak = 1.0 - odds_of_streak_within_shots
print 'odds of no streak for player:', odds_no_streak

odds_no_streak_any_player = (odds_no_streak ** 10.0)
print 'odds of no streak for any players:', odds_no_streak_any_player

odds_of_streak = 1.0 - odds_no_streak_any_player

print 'odds of a 10 streak from 10 players with 15 shots each, analytically:', odds_of_streak

def player_has_streak(shots, streak_threshold):
    in_streak = False
    streak = 0
    for shot in range(shots):
        if numpy.random.randint(2) == 0:
            if in_streak is True:
                streak = 0
                in_streak = False
        else:
            streak += 1
            if streak == streak_threshold:
                return True
            in_streak = True
    return False      

streaks = 0.0
for experiment in range(10000):
    for player in range(10):
        if player_has_streak(15, 10):
            streaks += 1.0
            break
      
print 'streak probability by monte-carlo:', streaks / 10000.0

print 'odds of seeing this at least once in 82 games:', 1 - ((1 - (streaks / 10000.0)) ** 82)
