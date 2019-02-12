f = open('corpus1.txt')

message = f.read()

cases = message.split('\n')
	# cases[1] contains the first case
	#print cases[1]

for x in range(1, 5):
	targetsentence = cases[x].split('###')
	# targetsentence[0] contains the TGrepID and the target sentence in cases[x]
	#print targetsentence[0]
	cleantarget = targetsentence[0].split('\t')
	# cleantarget[0] is TGrepID, cleantarget[1] is target sentence
	#print cleantarget[1]
	spl = cleantarget[1].split('some')
	# spl[0] is cleantarget before 'some', spl[1] is cleantarget after 'some',spl[2] is cleantarget after second some etc..
	length_spl = len(spl)
	if length_spl > 2:
		for n in range(length_spl-1,0,-1):
			possible_head = (spl[n])
			print possible_head
			a = open('heads1.txt')
			heads = a.read()
			heads_cases = heads.split('\n')
			#for every heads_cases, split into parts
			for a in range(0, 5):
				heads_split = heads_cases[a].split('\t')	
				if heads_split[0] == cleantarget[0]:
					print heads_split[2]
					# try to find heads_split[2] in possible_head



	

------------------------------------

a = open('heads1.txt')
heads = a.read()
heads_cases = heads.split('\n')
#for every heads_cases, split into parts

for a in range(0, 5):
	heads_split = heads_cases[a].split('\t')
	print heads_split[0]
	if heads_split[0] == "905:41":
		print heads_split[2]
	


	print heads_split[0]
	print heads_split[1]
	print heads_split[2]
	print heads_split[3]
	print heads_split[4]



# heads_split[0] --> ID
# heads_split[1] --> date
# heads_split[2] --> head
# heads_split[3] --> some number
# heads_split[4] --> new/old





heads_cases.find('priorities')


print heads_cases[0]
print heads_cases[1]






#add at the end of cases[1]


for x in range(1, 4):
    print (cases[x])

f.close()


###SpeakerA(\d+).(\d+)?t(\d+)(.\d+)?/g