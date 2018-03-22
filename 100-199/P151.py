# A printing shop runs 16 batches (jobs) every week and each batch requires a
# sheet of special colour-proofing paper of size A5. Every Monday morning, the
# foreman opens a new envelope, containing a large sheet of the special paper
# with size A1. He proceeds to cut it in half, thus getting two sheets of size 
# A2. Then he cuts one of them in half to get two sheets of size A3 and so on 
# until he obtains the A5-size sheet needed for the first batch of the week. All
# the unused sheets are placed back in the envelope. 
#		_________________________
#  		|			|			|
#  		|			|	A3		|
#   A1:	|			|			|
#  		|	A2		|___________|
#  		|			|	  |	A5	|
#  		|			|	  |_____|
#  		|			| A4  |	A5	|
#  		|___________|_____|_____|
#
# At the beginning of each subsequent batch, he takes from the envelope one 
# sheet of paper at random. If it is of size A5, he uses it. If it is larger, he
# repeats the 'cut-in-half' procedure until he has what he needs and any 
# remaining sheets are always placed back in the envelope. Excluding the first 
# and last batch of the week, find the expected number of times (during each
# week) that the foreman finds a single sheet of paper in the envelope. Give
# your answer rounded to six decimal places using the format x.xxxxxx .

import random
from time import clock
from sys import argv
st = clock()
c = 0
num_trials = int(argv[1])
for p in range(num_trials):
	envelope = {1:0, 2:1, 3:1, 4:1, 5:1}
	while(not all([not envelope[i] for i in range(1,6)])):
		e = random.choice([j for j in envelope.keys() if envelope[j] > 0])
		envelope[e] -= 1
		for s in range(e+1, 6):
			envelope[s] += 1
		if sum(envelope.values()) == 1:
			c += 1
print(clock() - st)
print("{0:.6f}".format(c/num_trials))