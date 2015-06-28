def mvg_avg():
	import nfldb

	db = nfldb.connect()

	q = nfldb.Query(db)

#def GetGameIndex(game):
#	return (game.season_year-2009)*16+game.week
#
#def GameIndexToGSIS(query,gameIndex):
#	for game in query.as_games():
#		searchedIndex = GetGameIndex(game)
#		if searchedIndex == gameIndex:
#			return game.gsis_id

	q.game(season_year=[2009,2010,2011,2012], season_type='Regular',team='NE')

#Need to get an index of the game within the sequence of valid games. 
#Compute the average of a statistic over the last six games. 

#MovingAverage(q,passing_yds)
#def MovingAverage(q,statistic):
	
#	for game in q.as_games():
#		gameIndex=	

	mvg_avg_passing_yds = []
	mvg_avg_rushing_yds = []
	result = []
	#print type(q.as_games())
	query = q.sort([('season_year', 'asc'),('week', 'asc')]).as_games()
	for index, game in enumerate(query):
#for game in q.sort([('season_year', 'asc'),('week', 'asc')]).as_games():
#	CurrentGameIndex = GetGameIndex(game)
#	print CurrentGameIndex
	#if CurrentGameIndex > 6:
	#print index
	#print game.week
		if index > 5:
			#aggTracker = []
			last_six_passing_yds = 0
			last_six_rushing_yds = 0
			by_game_set = []
			i = 1
			while (i <= 6):
				#ReferenceGameIndex = CurrentGameIndex - i
				referenceIndex = index - i
				#x = nfldb.Query(db)
				#x.game(gsis_id=GameIndexToGSIS(q,ReferenceGameIndex))
				by_game_passing_yds = 0
				by_game_rushing_yds = 0
				#for g in x.as_games():
					##print g.gsis_id
					#for pp in g.play_players:
					#	if pp.team == 'NE':
					#		by_game_passing_yds += pp.passing_yds
				for pp in query[referenceIndex].play_players:
					if pp.team == 'NE':
						by_game_passing_yds += pp.passing_yds
						by_game_rushing_yds += pp.rushing_yds
					#print by_game_passing_yds
						#aggTracker.append(pp.passing_yds)
				last_six_passing_yds += by_game_passing_yds
				last_six_rushing_yds += by_game_rushing_yds
			#by_game_set.append(by_game_passing_yds)
			
				i += 1
		
		#print "Last Six Passing Yds"
		#print last_six_passing_yds
		#mvg_avg_passing_yds.append([last_six_passing_yds/6,game.week,by_game_set]) 
			mvg_avg_passing_yds.append(last_six_passing_yds/6) 
			mvg_avg_rushing_yds.append(last_six_rushing_yds/6)
			if game.winner == 'NE':
				label = 'W'
			elif game.winner != 'NE':
				label = 'L'
			result.append(label)
	return mvg_avg_passing_yds, mvg_avg_rushing_yds, result

#	lastGameIndex = CurrentGameIndex-1
#	lastGameGSIS = GameIndexToGSIS(q,lastGameIndex)
#	x = nfldb.Query(db)
#	x.game(gsis_id=lastGameGSIS)
#	
#	print "Current:" + str(game.season_year)
#	print "Current:" + str(game.week)
#	for g in x.as_games():
#		print "Back Reference" + str(g.season_year)
#		print "Back Reference" + str(g.week)
#
	#if game.week > 6:
	#	#x = q 
		
	#	i = 1
	#	while (i <= 6):
	#		print "looping"
	#		x = q
	##		for checker in x.as_games():
	#			print "Full X Contains" + str(checker.week)
	#		x.game(season_year=game.season_year, week=game.week-i)
	#		for innergame in x.as_games():
	#			print innergame.season_year
	#			print innergame.week
			#i += 1
