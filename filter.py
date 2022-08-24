import sys

def read_data():
	with open('validation.txt', 'r') as myfile:
		data = myfile.read().replace('\n', ' ')

	return data.split(' ')


def remove_duplicate():
	with open('validation2.txt', 'a') as valid:
		valid.write('\n'.join(set(read_data())))

remove_duplicate()
