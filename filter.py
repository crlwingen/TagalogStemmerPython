import sys

def read_data():
	with open('output/root_only.txt', 'r') as myfile:
		data = myfile.read().replace('\n', ' ')

	return data.split(' ')


def remove_duplicate():
	with open('validation.txt', 'a') as valid:
		valid.write('\n'.join(set(read_data())))

remove_duplicate()
