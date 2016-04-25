import math
import random
import sqlite3
import time

CLASS = 'ANTH101'

def getRandom(current, questionList):
	answerList = []
	while len(answerList) < 4:
		num = math.floor(random.random() * 100) % len(questionList)
		num2 = math.floor(random.random() * 100) % 4
		if len(answerList) is 3 and current not in answerList:
			answerList.append(int(current))
		elif num2 is 3 and current not in answerList:
			answerList.append(int(current))
		elif num not in answerList:
			answerList.append(int(num))
	
	return answerList 

def isCorrect(val,answers,current):
	index = None
	if val is 'a':
		index = 0
	elif val is 'b':
		index = 1
	elif val is 'c':
		index = 2
	elif val is 'd':
		index = 3
	else: 
		return False
	if answers[index] is current:
		return True
	return False

conn = sqlite3.connect('StudyGuide.db')
c = conn.cursor()

c.execute("SELECT COUNT(*) FROM questions WHERE class = '%s'" % CLASS)
numQuestions = c.fetchone()

c.execute("SELECT * FROM questions NATURAL JOIN answers WHERE class = '%s'" % CLASS)
questions = c.fetchall()

n = 0
numCorrect = 0

for q in questions:
	time.sleep(1)
	print "%d) %s" % (n+1,q[2])
	answers = getRandom(n,questions)
	print "a) %s \tb) %s\nc) %s\td) %s\n" % (questions[answers[0]][3], questions[answers[1]][3], questions[answers[2]][3], questions[answers[3]][3])
	val = raw_input('Select an answer: [a,b,c,d]\n')
	if isCorrect(val,answers,n):
		numCorrect+=1
		print 'CORRECT!'
	else:
	 	print 'WRONG! The answer is: %s' % q[3]
	n+=1

print "Your score: %d out of %d. (%.2f%s)" % (numCorrect, n, numCorrect/n * 100, '%')



