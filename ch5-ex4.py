import numpy

stick_wins = 0
switch_wins = 0

for i in range(1000):
    prize_door = numpy.random.randint(3)
    chosen_door = numpy.random.randint(3)
    if chosen_door != prize_door:
#if the contestant didn't get the right door with their first guess, they can only win by switching
        switch_wins += 1
    else:
#if their first guess is right, they have to stick with it to win
        stick_wins += 1 


print 'switch wins', switch_wins
print 'stick wins', stick_wins    
