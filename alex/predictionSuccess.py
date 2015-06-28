from classify import classify

f = open("teamnames.txt", 'r')
successRates = 0
for teamname in f:
	successRates += classify(str.strip(teamname))

#number = classify("NYJ")
#print number
overallSuccess = successRates/32
print "Overall Accuracy is: " + str(overallSuccess)
