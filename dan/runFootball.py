from football import *

x = Football()
x.games_back = 6
x.training_years = [2009,2010,2011,2012]
x.stat = ['rushing_yds', 'passing_yds']

y = Football()
y.training_years = [2013,2014]
y.stat = ['rushing_yds', 'passing_yds']

z = Football()

z.classify(x,y)
