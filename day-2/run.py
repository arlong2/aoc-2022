# run.py

import sys

COMBINATIONS = {'X': [0, {'A': 3, 'B': 1, 'C': 2}],
			    'Y': [3, {'A': 1, 'B': 2, 'C': 3}],
			    'Z': [6, {'A': 2, 'B': 3, 'C': 1}]}


def main(input):
	data = open(input).read()
	score = 0
	for l in data.split("\n"):
	    opponent, move = l.split()
	    base, opp_r = COMBINATIONS[move]
	    score += (base + opp_r[opponent])

	print(f'Winning score is {score}')
	return

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("Usage: python3 run.py <input>")
		sys.exit()
	print("\n************************")
	print("****   AOC - Day 2  ****")
	print("************************\n")
	sys.exit(main(sys.argv[-1]))
