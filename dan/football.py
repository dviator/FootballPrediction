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
		self.stat = ['passing_yds']
		self.games_back = 6
		self.team = 'DEN'
	
	#Calculates a moving average based on the instance attributes given. 
	def mvg_avg(self):
		
		#Get all the games for one team within the given games selection and sort in order 
		#so we can calculate a historical average.
		self.q.game(season_year=self.training_years, season_type=self.season_type,team=self.team)
		query = self.q.sort([('season_year', 'asc'),('week', 'asc')]).as_games()

		mvg_avg_stat = []
		result = []

		for index, game in enumerate(query):
			
			#Exclude games without enough prior history for the average.
			if index > self.games_back:
				#Initialize dictionary to hold sums over i games back of chosen stats.
				games_back_stats_sum = dict.fromkeys(self.stat, 0)
				stats_bag = []

				i = 1
				while (i <= self.games_back):
					#Travel back i games to get history
					referenceIndex = index - i
					#Initialize dictionary to hold stat sums of each game.
					by_game_stat = dict.fromkeys(self.stat, 0)
					#Loop through play_player objects to sum stats of the game
					for pp in query[referenceIndex].play_players:
						#Check that the player plays for the chosen team
						if pp.team == self.team:
							#Get each stat and sum in dict for each play_player
							for stat in self.stat:
								by_game_stat[stat] += getattr(pp, stat)
					#Aggregate each stat through all i games
					for key in games_back_stats_sum:
						games_back_stats_sum[key] += by_game_stat[key]
					i += 1
 				#Compute average and store in list ordered for classify.py
				for s in games_back_stats_sum:
					stats_bag.append(games_back_stats_sum[s]/float(self.games_back))	
				mvg_avg_stat.append(stats_bag)
				#Record result in companion list 
				if game.winner == self.team:
					label = 'W'
				elif game.winner != self.team:
					label = 'L'
				result.append(label)

		return mvg_avg_stat, result

	def classify(self,trainingObject,testingObject):
		# features_train, labels_train, features_test, labels_test = makeNFLdata()
		features_train, labels_train = Football.mvg_avg(trainingObject)
		features_test, labels_test = Football.mvg_avg(testingObject)
		print features_train
		print labels_train
		print features_test
		print labels_test
		# Use K-nearest-neighbors algorithm to train/test our classifier 
		from sklearn.neighbors import KNeighborsClassifier
		clf = KNeighborsClassifier(n_neighbors=3, weights='distance')
		clf.fit(features_train, labels_train)
		pred = clf.predict(features_test)

		from sklearn.metrics import accuracy_score
		accuracy = accuracy_score(pred, labels_test)
		print accuracy
		return accuracy

