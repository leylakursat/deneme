f = open('saved_contexts_for_all.txt')
#f = open('corpus1.txt')

file = open('new_corpus.txt', 'a')

message = f.read()

cases = message.split('\n')
	# cases[1] contains the first case

def findnth(source, target, n):
    num = 0
    start = -1
    while num < n:
        start = source.find(target, start+1)
        if start == -1: return -1
        num += 1
    return start

def replacenth(source, old, new, n):
    p = findnth(source, old, n)
    if n == -1: return source
    return source[:p] + new + source[p+len(old):]

count = 0

#real range 0,577
for x in range(0, 577):
	targetsentence = cases[x].split('###')
	# targetsentence[0] contains the TGrepID and the target sentence in cases[x]
	cleantarget = targetsentence[0].split('\t')
	# cleantarget[0] is TGrepID, cleantarget[1] is target sentence
	spl = cleantarget[1].split('some')
	# spl[0] is cleantarget before 'some', spl[1] is cleantarget after 'some',spl[2] is cleantarget after second some etc..
	length_spl = len(spl)
	best_response = cleantarget[1]
	if length_spl > 2:
	# when there are multiple 'some's
	# be.<rk<e
		for n in range(length_spl-1,0,-1):
			possible_head = (spl[n])
			a = open('some_heads.txt')
			heads = a.read()
			heads_cases = heads.split('\n')
			#for every heads_cases, split into parts
			for a in range(0, 1335):
				heads_split = heads_cases[a].split('\t')
				#heads_split[0] is the TGrepID of each head	
				if heads_split[0] == cleantarget[0]:
					if possible_head.find(heads_split[2]) != -1:
						#print "MULTIPLE SOME'S!!! HEAD IS CONTAINED IN: " + possible_head 
						#print "HEAD: " + heads_split[2]
						#print "TARGET SENTENCE " + best_response
						best_response = "\t" + replacenth(best_response, "some", "all", n)
						#print "BEST RESPONSE: " + best_response
	else:
		#print "ONLY ONE SOME!!! TARGET SENTENCE: " + best_response
		best_response = "\t" + best_response.replace('some','all')
		#print "BEST RESPONSE: " + best_response
	cases[x] = cases[x] + best_response
	print cases[x]	
	file.write("\n" + cases[x])
	count = count +1

print count

f.close()
