# FootballPrediction
For working on machine learning models to predict the nfl with the nfldb project

## ALEX's COMMITS ##

6/28 - Added 3 files : classify.py, average.py, nfldb
       they work together

## DAN's COMMITS ##
Got the average of the classifier bit working. Haven't figured out how to use classify by itself now but I think the average is more useful anyway.
Just call python predictionSuccess.py and it runs the classifier for all teams and returns the average. 

Next up is to parameterize some of the stuff we've done here so that we can more rapidly iterate going forward. I think my implementation of the 
moving average function is a bit faster, and it does start to make a difference when you're looping through the teams, so I will work on formatting
that one to work with the classifier function and take different paramaters. 

6/29
Halfway through writing the Football class, so far lets you parameterize some parts of the moving average calculation
