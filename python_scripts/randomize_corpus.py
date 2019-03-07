import random

f = open('final_corpus.txt')
file = open('randomized_corpus.txt', 'a')

message = f.read()
cases = message.split('\n')
	# cases[1] contains the first case

random.shuffle(cases);

for x in range(0, 581):
	file.write(str(cases[x] + "\n")

f.close()




TGrepID	EntireSentence	context	BestResponse
