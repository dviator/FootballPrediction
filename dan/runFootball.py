from football import *

x = Football()
x.games_back = 3
x.training_years = [2009]
print x.mvg_avg()

y = Football()
y.games_back = 3
y.training_years = [2009,2010]

print y.mvg_avg()
