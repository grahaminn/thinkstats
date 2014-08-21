import thinkstats

# 10 consecutive shots from 15, is the probability of 10 out of 10 shots times 60 (there are 10 players, and each has 6 opportunities, shots 1-10 go in, or shots 2-11 etc.. up to  6-15)

odds_of_streak = ((0.5 ** 10) * 60)

print 'odds of a 10 streak from 10 players with 15 shots each:', odds_of_streak

odds_no_streak = 1 - odds_of_streak

print 'odds of seeing this at least once in 82 games:', 1 - (odds_no_streak ** 82)

 
