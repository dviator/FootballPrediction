import nfldb

db = nfldb.connect()
q = nfldb.Query(db)

q.game(season_year="2012", season_type="Regular")
q.player(full_name="Marshawn Lynch")

for p in q.as_plays():
	print p.rushing_yds
