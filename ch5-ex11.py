import numpy
import thinkstats

# 10 consecutive shots from 15, is the probability of 10 out of 10 shots times 60 (there are 10 players, and each has 6 opportunities, shots 1-10 go in, or shots 2-11 etc.. up to  6-15)

odds_of_streak = ((0.5 ** 10) * 60)

print 'odds of a 10 streak from 10 players with 15 shots each, analytically:', odds_of_streak

odds_no_streak = 1 - odds_of_streak

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
for experiment in range(1000):
    for player in range(10):
       if player_has_streak(15, 10):
           streaks += 1.0
           break
        
print 'streak probability by monte-carlo:', streaks / 1000

print 'odds of seeing this at least once in 82 games:', 1 - ((1 - streaks / 1000) ** 82)
