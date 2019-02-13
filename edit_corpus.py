f = open('corpus1.txt')

message = f.read()

cases = message.split('\n')
	# cases[1] contains the first case
	#print cases[1]

print cases[0]

for x in range(1, 5):
	targetsentence = cases[x].split('###')
	# targetsentence[0] contains the TGrepID and the target sentence in cases[x]
	#print targetsentence[0]
	cleantarget = targetsentence[0].split('\t')
	# cleantarget[0] is TGrepID, cleantarget[1] is target sentence
	#print cleantarget[0]
	spl = cleantarget[1].split('some')
	# spl[0] is cleantarget before 'some', spl[1] is cleantarget after 'some',spl[2] is cleantarget after second some etc..
	length_spl = len(spl)
	if length_spl > 2:
	# when there are multiple 'some's
		for n in range(length_spl-1,0,-1):
			possible_head = (spl[n])
			a = open('heads1.txt')
			heads = a.read()
			heads_cases = heads.split('\n')
			#for every heads_cases, split into parts
			for a in range(0, 5):
				heads_split = heads_cases[a].split('\t')	
				if heads_split[0] == cleantarget[0]:
					if possible_head.find(heads_split[2]) != -1:
						#print "multiple some's, head is contained in: " + possible_head 
						# print "head: " + heads_split[2]
						best_response = cleantarget[1]
						#print "target sentence: " + best_response
						best_response = "\t" + best_response.replace('some','all',n)
						#print "best reponse: " + best_response
	else:
		best_response = cleantarget[1]
		#print "only one some, target sentence: " + best_response
		best_response = "\t" + best_response.replace('some','all')
		#print "best reponse: " + best_response
	cases[x] = cases[x] + best_response
	print cases[x]



	

print cases[0]	






						#change some in possible head and add ad the end of cases[x] 
					



	

f.close()


###SpeakerA(\d+).(\d+)?t(\d+)(.\d+)?/g