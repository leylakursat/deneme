################################################
########find heads that are found###############

f = open('saved_new_corpus.txt')

message = f.read()

cases = message.split('\n')
	# cases[1] contains the first case

found = []

for x in range(1, 583):
	targetsentence = cases[x].split('###')
	# targetsentence[0] contains the TGrepID and the target sentence in cases[x]
	cleantarget = targetsentence[0].split('\t')
	# cleantarget[0] is TGrepID, cleantarget[1] is target sentence
	id = cleantarget[0]
	a = open('some_heads.txt')
	heads = a.read()
	heads_cases = heads.split('\n')
	#for every heads_cases, split into parts
	for a in range(0, 1335):
		heads_split = heads_cases[a].split('\t')
		#heads_split[0] is the TGrepID of each head	
		if heads_split[0] == id:
			found.append(id)
		else: 
			continue

f.close()

################################################
########find unchanged##########################

f = open('final_corpus.txt')

message = f.read()

unchanged = []

cases = message.split('\n')
	# cases[1] contains the first case

#real range 1,583
for x in range(1, 583):
	targetsentence = cases[x].split('\t')
	if targetsentence[1] == targetsentence[3]:
		unchanged.append(targetsentence[0])

print unchanged

################################################
#####find heads that are not found and need to be found#####

f = open('saved_new_corpus.txt')

message = f.read()

#102 items
unchanged = ['86088:57', '112290:7', '1177:17', '11991:7', '112156:136', '90995:20', '107909:42', '23510:57', '63606:10', '171124:6', '175702:23', '31080:8', '9486:04', '22018:5', '55028:10', '134479:41', '147340:7', '30391:26', '1214:19', '155521:29', '41388:61', '156671:38', '81221:70', '117354:63', '63108:7', '36621:7', '36613:5', '38898:13', '130958:7', '108790:33', '72090:7', '13059:11', '59953:42', '4457:24', '55892:50', '2006:05:00', '163703:15', '75025:28', '20045:19', '108757:10', '115343:46', '128696:11', '108856:73', '66134:57', '1206:10', '27773:13', '66483:25', '148463:10', '143752:15', '151303:29', '72079:13', '27056:5', '173724:18', '52283:13', '100889:88', '42653:25', '4529:07', '9797:33', '19933:5', '99355:10', '75949:43', '43900:8', '135535:24', '38991:16', '148183:40', '173289:7', '140818:55', '2722:07', '16415:5', '56809:31', '36737:8', '36612:7', '120517:9', '120178:18', '13469:7', '160595:7', '175669:10', '16349:60', '55078:22', '27683:75', '108737:78', '4528:07', '156639:7', '73140:10', '142141:14', '100571:7', '146612:75', '156650:7', '126455:10', '84205:26', '168217:7', '15261:95', '159110:25', '8884:22', '157049:37', '148456:26', '87654:69', '37263:24', '108521:93', '47856:7', '9762:24', '98822:22']

cases = message.split('\n')

multiple_some = []
single_some = []

#real range 1,583
for x in range(1, 583):
	targetsentence = cases[x].split('\t')
	#targetsentence[0] is id 
	#targetsentence[1] is entiresentence
	#targetsentence[2] is context
	#targetsentence[3] should be best response 
	for a in range(0, 101):
		if targetsentence[0] == unchanged[a]:
			count = targetsentence[1].count("some")
			if count == 1:
				single_some.append(targetsentence[0])
			elif count > 1:
				multiple_some.append(targetsentence[0])
			else:
				print "something's wrong"
				print targetsentence[0]
				print targetsentence[1]

print multiple_some
print single_some
len_multiple = len(multiple_some)
len_single = len(single_some)





















