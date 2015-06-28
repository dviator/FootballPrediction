from pandas import DataFrame
from MovingAverage import mvg_avg
from ggplot import *

rushing_yds, passing_yds, result = mvg_avg()
df = DataFrame.from_records(data={'rushing_yds':rushing_yds,'passing_yds':passing_yds,'result':result}, columns = ['rushing_yds','passing_yds','result'])
print df
plot = ggplot(df, aes(x = 'rushing_yds', y = 'passing_yds', color = 'result')) + geom_point()
print plot
