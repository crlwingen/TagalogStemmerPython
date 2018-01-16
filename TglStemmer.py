import sys

""" 
	CONSTANTS 
"""
VOWELS = "aeiouAEIOU"
CONSONANTS = "bdghklmnngprstwyBDGHKLMNNGPRSTWY"

""" 
	Affixes
"""
PREFIX_SET = [
	'nakikipag', 'pakikipag',
	'pinakama', 'pagpapa',
	'pakiki', 'magpa',
	'napaka', 'pinaka',
	'panganga', 'makapag',
	'nakapag', 'tagapag',
	'makipag', 'nakipag',
	'tigapag', 'pinag',
	'pagka', 'ipinag',
	'mapag', 'mapa',
	'taga', 'ipag',
	'tiga', 'pala',
	'pina', 'pang',
	'ipa', 'nang',
	'naka', 'pam',
	'pan', 'pag',
	'mag', 'nam',
	'nag', 'man',
	'may', 'ma',
	'na', 'ni',
	'pa', 'ka',
	'um', 'in',
	'i',
]

INFIX_SET = [
	'um', 'in',
]

SUFFIX_SET = [
	'uhan', 'han',
	'hin', 'ing',
	'ng', 'an',
	'in',
]

PREFIX = INFIX = SUFFIX = DUPLICATE = REPTITION = 'NONE'


def stemmer(mode, source):
	""" 
		Stems the tokens in a sentence.
			mode: if from .txt or string
			source: the string or file name 
		returns LIST
	"""

	print("TAGALOG WORDS STEMMER....")
	print("[1 FileName] [2 RawString]")

	PERIOD_FLAG = True

	word_info = {}
	stemmed = []
	root = []
	pre_stem = inf_stem = suf_stem = rep_stem = \
		du1_stem = du2_stem = cle_stem = '-'

	if mode is "1":
		print("Chosen text file as source. [" + source + "]")
		tokens = read_file(source)

	elif mode is "2":
		print("Chosen raw string as source.")
		tokens = source.split(' ')

	else:
		print("Unknown mode chosen. Exiting...")
		sys.exit()

	for token in tokens:
		token = token.lower() if PERIOD_FLAG == True else token
		
		word_info["word"] = token
		
		if PERIOD_FLAG == True or \
			PERIOD_FLAG == False and token[0].islower():
			
			du1_stem = clean_duplication(token)
			pre_stem = clean_prefix(du1_stem)
			rep_stem = clean_repitition(pre_stem)
			inf_stem = clean_infix(rep_stem)
			suf_stem = clean_suffix(inf_stem)
			du2_stem = clean_duplication(suf_stem)
			cle_stem = clean_lemmatized(du2_stem)

			if '-' in cle_stem:
				cle_stem.replace('-', '')

			word_info["root"]   = cle_stem
			word_info["prefix"] = PREFIX
			word_info["infix"]  = INFIX
			word_info["suffix"] = SUFFIX
			word_info["dup#1"]  = DUPLICATE
			word_info["dup#2"]  = DUPLICATE

		else:

			cle_stem = clean_lemmatized(token)

			word_info["root"]   = cle_stem
			word_info["prefix"] = 'NONE'
			word_info["infix"]  = 'NONE'
			word_info["suffix"] = 'NONE'
			word_info["dup#1"]  = 'NONE'
			word_info["dup#2"]  = 'NONE'

		PERIOD_FLAG = False
		stemmed.append(word_info)
		root.append(word_info["root"])
		print(word_info["word"] + " : " + word_info["root"])
		word_info = {}
		pre_stem = inf_stem = suf_stem = rep_stem = \
		du1_stem = du2_stem = cle_stem = '-'

	return stemmed, root


def clean_duplication(token):
	"""
		Checks token for duplication. (ex. araw-araw = araw)
			token: word to be stemmed duplication
		returns STRING
	"""

	global DUPLICATE

	if '-' in token and token.index('-') != 0 and \
		token.index('-') != len(token) -  1:

		token = token.split('-')

		# Checks for full duplication
		if token[0] == token[1]:
			DUPLICATE = token[0]
			return token[0]

		else:
		 	return '-'.join(token)

		# TODO: partial duplication
	
	return token


def clean_repitition(token):
	"""
		Checks token for repitition. (ex. nakakabaliw = nabaliw)
			token: word to be stemmed repitition
		returns STRING
	"""

	global REPTITION

	if len(token) >= 4:
		if check_vowel(token[0]):
			if token[0] == token[1]:
				REPTITION = token[0]
				return token[1:]

		elif check_consonant(token[0]) and len(token) >= 5:
			if token[0: 2] == token[2: 4]:
				REPTITION = token[2: 4]
				return token[2:]

	return token


def clean_prefix(token):
	"""
		Checks token for prefixes.
			token: word to be stemmed for prefixes
		returns STRING
	"""
	global PREFIX

	for prefix in PREFIX_SET:
		if len(token) - len(prefix) >= 3 and \
			count_vowel(token[len(prefix):]) >= 2:
			
			if prefix == ('i') and check_consonant(token[2]):
		 		break

			elif token[0: len(prefix)] == prefix:
				if count_vowel(token[len(prefix):]) >= 2:
					PREFIX = prefix

					if prefix == 'panganga':
						return 'ka' + token[len(prefix):]
					
					return token[len(prefix):]

	return token

 
def clean_infix(token):
	"""
		Checks token for infixes.
			token: word to be stemmed for infixes
		returns STRING
	"""

	global INFIX

	for infix in INFIX_SET:
		if len(token) - len(infix) >= 3 and count_vowel(token[len(infix):]) >= 2:
			if token[0] == token[4] and token[1: 4] == infix:
				INFIX = infix
				return token[4:]

			elif token[1: 3] == infix and check_vowel(token[3]):
				INFIX = infix
				return token[0] + token[3:]

	return token


def clean_suffix(token):
	"""
		Checks token for suffixes.
			token: word to be stemmed for suffixes
		returns STRING
	"""

	global SUFFIX

	for suffix in SUFFIX_SET:
		print(token[0:len(token) - len(suffix)] + " : " + suffix)
		if len(token) - len(suffix) >= 3 and count_vowel(token[0:len(token) - len(suffix)]) >= 2:
			if token[len(token) - len(suffix): len(token)] == suffix:

				if count_vowel(token[0: len(token) - len(suffix)]) >= 2:
					SUFFIX = suffix
					return token[0: len(token) - len(suffix)]
 
	return token


def check_vowel(letter):
	"""
		Checks if the letter is a vowel.
			letter: letter to be tested
		returns BOOLEAN
	"""
	return letter in VOWELS


def check_consonant(letter):
	"""
		Checks if the letter is a consonant.
			letter: letter to be tested
		returns BOOLEAN
	"""
	return letter in CONSONANTS


def count_vowel(token):
	"""
		Count vowels in a given token.
			token: string to be counted for vowels
		returns INTEGER
	"""

	count = 0

	for tok in token:
		if check_vowel(tok):
			count+=1

	return count


def clean_lemmatized(token):
	"""
		Checks for left-over affixes and letters.
			token: word to be cleaned for excess affixes/letters
		returns STRING
	"""

	if len(token) >= 3 and count_vowel(token) >= 2:
		if check_consonant(token[-1]) and token[- 2] == 'u':
			token = change_letter(token, -2, 'o')

		elif token[len(token) - 1] == 'u':
			token = change_letter(token, -1, 'o')

		elif token[-1] == 'r' and (token[-2]  == 'o' or token[-2] == 'i'):
			token = change_letter(token, -1, 'd')

		elif token[-1] == 'h' and check_vowel(token[-1]):
			token = token[0:-1]

		if token[0] == 'i':
			token = token[1:]

		if token[0] == token[1]:
			token = token[1:]

		if (token[0: 2] == 'ka' or token[0: 2] == 'pa') and check_consonant(token[2]) \
			and count_vowel(token) >= 3:
			
			token = token[2:]

		if(token[-3:]) == 'han' and count_vowel(token[0:-3]) == 1:
			token = token[0:-3] + 'i'

		elif len(token) >= 2 and count_vowel(token) >= 3:
			if token[-1] == 'h' and check_vowel(token[-2]):
				token = token[0:-1]

	if not check_vowel(token[-1]) and not check_consonant(token[-1]):
		token = token[0:-1]

	return token


def change_letter(token, index, letter):
	"""
		Replaces a letter in a token.
			token: word to be used
			index: index of the letter
			letter: letter used to replace
		returns STRING
	"""
	
	_list = list(token)
	_list[index] = letter

	return ''.join(_list)


def read_file(source):
	"""
		Gets content of a text file.
			source: file name
		returns LIST
	"""

	with open(source, 'r') as myfile:
		data = myfile.read().replace('\n', ' ')

	return data.split(' ')


mode = sys.argv[1] # 1: Text File // 2: Raw String
source = sys.argv[2] # if 1: .txt name // 2: raw string

if __name__ == "__main__":
	stemmer(mode, source)
