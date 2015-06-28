import nfldb
import sys

def movingAvgData():

	db = nfldb.connect()
	train = nfldb.Query(db)
	test = nfldb.Query(db)

	def compute(query, team):

		all_games = []
		for game in query.as_games():
			all_games.append(game)


		# sort the games by date (from gsis_id),
		def byGSIS_id(game):
			return int(game.gsis_id)

		games_sorted = sorted(all_games, key=byGSIS_id)


		#compute the moving averages (of the difference between teams passing yards)
		def mv_avg(index, array, span):
			tmp_sum_passing_yards = 0.0
			tmp_sum_rushing_yards = 0.0
			tmp_sum_passing_tds = 0.0		
			tmp_sum_rushing_tds = 0.0	
			tmp_sum_kicking_fgbs = 0.0

		 	for i in range (index-span, index-1):
			 	for pp in array[i].play_players:
			 		if (pp.team == team):
			 			tmp_sum_passing_yards += float(pp.passing_yds)
			 			tmp_sum_rushing_yards += float(pp.rushing_yds)
			 			tmp_sum_passing_tds += float(pp.passing_tds)
			 			tmp_sum_rushing_tds += float(pp.rushing_tds)
			 			tmp_sum_kicking_fgbs += float(pp.kicking_fgb)
			 		else: #for the other team, subtract from the total yards
			 			tmp_sum_passing_yards -= float(pp.passing_yds)
			 			tmp_sum_rushing_yards -= float(pp.rushing_yds)
			 			tmp_sum_passing_tds -= float(pp.passing_tds)
			 			tmp_sum_rushing_tds -= float(pp.rushing_tds)	
			 			tmp_sum_kicking_fgbs -= float(pp.kicking_fgb)
		 					 			
			return [tmp_sum_passing_yards/float(span), 
				    tmp_sum_rushing_yards/float(span), 
				    tmp_sum_passing_tds/float(span),
				    tmp_sum_rushing_tds/float(span),
				    tmp_sum_kicking_fgbs/float(span)
				    ]

		moving_averages = []
		next_game_results = []

		for index in range(len(games_sorted)):
		 	if (index >= 6) and (index < len(games_sorted)):
		 		datapoint = [0,0,0,0,0]
		 		datapoint[0], datapoint[1], datapoint[2], datapoint[3], datapoint[4]= mv_avg(index, games_sorted, 6)
			 	moving_averages.append(datapoint)
			 	if(games_sorted[index].winner == team):
			 		next_game_results.append('W')
			 	else:
			 		next_game_results.append('L')


		return [moving_averages, next_game_results]		

	# END COMPUTE FUNCTION

	team = sys.argv[1]

	train.game(season_year=[2009, 2010, 2011, 2012], season_type=['Regular'], team=team)
	features_train, labels_train = compute(train, team)

	test.game(season_year=[2013, 2014], season_type=['Regular'], team=team)
	features_test, labels_test = compute(test, team)

	return [features_train, labels_train, features_test, labels_test]