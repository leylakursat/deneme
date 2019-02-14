Python scripts to make changes in corpus:

remove_cases.py --> preprocesses the corpus, contains a list of TGrepIDs that should be (items_to_add) in the corpus, finds them in contexts.txt and copies them to contexts_for_all.txt
	input: (list is taken from some_replacement.xlsx), contexts.txt
	output: contexts_for_all.txt, (a list called added[] -manually saved as ID_contexts_for_all.txt)

not_addded.py --> compares the list of cases included in contexts_for_all.txt (ID_contexts_for_all.txt) and list of cases that should be included(items_to_add from remove_cases.py)
	output: (manually save the list as not added to ID_contexts_for_all.txt)

edit_corpus.py --> processes the corpus, replaces the "some" in target sentence and saves it at the end of each case, when there are multiple "some"s, compares the possible heads in the sentence to the head in some_heads.txt. 
	input: saved_contexts_for_all.txt, some_heads.txt
	output: new_corpus.txt

Test Files: test_corpus1.txt, test_format.txt, test_head1.txt



