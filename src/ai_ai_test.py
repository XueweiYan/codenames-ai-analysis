import os
import numpy as np
from tqdm import tqdm

def ai_test(outfile, num_games, algorithms, data):
	# outfile = '../../data/ai_ai_data.csv'
	# num_games = 100
	# algorithms = ['1', '2']  
	# data = 33

	#create data directory and add headings
	if not os.path.isdir('./data'):
		os.mkdir('./data/')
	with open("./data/ai_ai_data.csv", 'w') as f:
	    f.write(",".join(['turn', 'assassin', 'algorithm', 'data', 'seed', 'cb', 'ci']) + "\n")

	#change to game directory to run simulations and collect data
	os.chdir("game/code")

	data = [str(i) for i in range(1, data + 1)]
	seeds = [str(i) for i in np.random.randint(2**31 - 1, size = (num_games))]
	#loop through all combinations between algorithm, dataset, and seed
	for alg in algorithms:
		for d in data:
			print('----- algorithm={}, data={}/{}'.format(alg, d, len(data)))
			for s in tqdm(seeds):
				cmd = 'python codenames.py -p 2 2 2 2 -m pure_ai -a {} -d {} -s {} -o {}'.format(alg, d, s, outfile)
				os.system(cmd)

	os.chdir("../../codenames-ai-analysis")

def ai_stats(datafile, outdir):
	#read in data, create plots
	return None