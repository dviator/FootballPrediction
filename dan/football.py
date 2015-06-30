import nfldb


class Football(object):
		
	db = nfldb.connect()

	#Setup connection to database
	#Set default values for query parameters
	#These can all be overridden with football.variableName
        def __init__(self):
                self.q = nfldb.Query(Football.db)
		self.training_years = [2009,2010,2011,2012]
		self.season_type = 'Regular'
		self.stat = 'passing_yds'
		self.games_back = 6

	def mvg_avg(self):

		self.q.game(season_year=self.training_years, season_type=self.season_type,team='NE')


		mvg_avg_stat = []
		result = []
		query = self.q.sort([('season_year', 'asc'),('week', 'asc')]).as_games()
		for index, game in enumerate(query):
		
			if index > self.games_back:
				games_back_stats_sum = 0
				
				i = 1
				while (i <= self.games_back):
					referenceIndex = index - i
					by_game_stat = 0
					for pp in query[referenceIndex].play_players:
						if pp.team == 'NE':
							by_game_stat += pp.passing_yds
							#How do I call an attribute dynamically based on an arugment?
							#by_game_stat += pp.self.stat
					
					games_back_stats_sum += by_game_stat
			
					i += 1
		
				mvg_avg_stat.append(games_back_stats_sum/self.games_back) 
				if game.winner == 'NE':
					label = 'W'
				elif game.winner != 'NE':
					label = 'L'
				result.append(label)

		return mvg_avg_stat, result

