print "DELETE FROM answers;";
print "DELETE FROM questions;";
with open('questions.txt', 'r') as f:
	i = 20
	for line in f.readlines():
		values = line.split('|')
		print "INSERT INTO questions (id,class,question) VALUES (%d,'ANTH101','%s');" % (int(i),values[0].replace('\'','\'\''))
		print "INSERT INTO answers (id,answer) VALUES (%d,'%s');" % (int(i),values[1].replace('\'','\'\''))
		i+=1

