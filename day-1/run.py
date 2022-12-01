# run.py

import sys

def readFile(file_name):
	with open(file_name) as f:
		lines = f.readlines()
	#print(lines)
	return lines

def convertToElfs(lines):
	elfs = list()
	current_elf = 0
	for line in lines:
		#print(current_elf)
		if line == '\n':
			elfs.append(current_elf)
			current_elf = 0
		else:
			current_elf += int(line[:-1])

	return elfs

def main(input):
	lines = readFile(input)
	elfs = convertToElfs(lines)
	elfs = sorted(elfs)
	#print(elfs)
	print(f'Elf carrying the most Calories are:')
	print(f'1: {elfs[-1]}')
	print(f'2: {elfs[-2]}')
	print(f'3: {elfs[-3]}')
	total = elfs[-1] + elfs[-2] + elfs[-3]
	print(f'They have a total of {total}')
	return

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("Usage: python3 run.py <input>")
		sys.exit()
	print("\n************************")
	print("****   AOC - Day 1  ****")
	print("************************\n")
	sys.exit(main(sys.argv[-1]))