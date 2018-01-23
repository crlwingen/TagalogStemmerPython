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
	'pinagka', 'panganga', 
	'makapag', 'nakapag', 
	'tagapag', 'makipag', 
	'nakipag', 'tigapag',
	'pakiki', 'magpa',
	'napaka', 'pinaka',
	'ipinag', 'pagka', 
	'pinag', 'mapag', 
	'mapa', 'taga', 
	'ipag', 'tiga', 
	'pala', 'pina', 
	'pang', 'naka',
	'nang', 'mang',
	'sing',
	'ipa', 'pam',
	'pan', 'pag',
	'tag', 'mai',
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
	'syon',
	'dor', 'ita',
	'han', 'hin', 
	'ing', 'ang', 
	'ng', 'an', 
	'in',
]

PERIOD_FLAG = True
PASS_FLAG = False

def stemmer(mode, source, info_dis):
	""" 
		Stems the tokens in a sentence.
			mode: if from .txt or string
			source: the string or file name 
		returns LIST
	"""

	print("TAGALOG WORDS STEMMER....")
	print("[1 FileName] [2 RawString] [3 ShowInfo]")

	global PERIOD_FLAG
	global PASS_FLAG

	word_info    = {}
	stemmed      = []
	word_root    = []
	root_only    = []
	errors       = []
	pre_stem     = inf_stem = suf_stem = rep_stem = \
		du1_stem = du2_stem = cle_stem = '-'

	PREFIX     = []
	INFIX      = []
	SUFFIX     = []
	DUPLICATE  = []
	REPITITION = []
	CLEANERS   = []

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
		word_info["word"] = token
		
		if (PERIOD_FLAG == True and token[0].isupper()) or \
			(PERIOD_FLAG == False and token[0].islower()):

			token 	 = token.lower()		
			du1_stem = clean_duplication(token, DUPLICATE)
			pre_stem = clean_prefix(du1_stem, PREFIX)
			rep_stem = clean_repitition(pre_stem, REPITITION)
			inf_stem = clean_infix(rep_stem, INFIX)
			rep_stem = clean_repitition(inf_stem, REPITITION)
			suf_stem = clean_suffix(rep_stem, SUFFIX)
			du2_stem = clean_duplication(suf_stem, DUPLICATE)
			cle_stem = clean_stemmed(du2_stem, CLEANERS, REPITITION)
			cle_stem = clean_duplication(cle_stem, DUPLICATE)

			if '-' in cle_stem:
				cle_stem.replace('-', '')

			# if stemmed is wrong, go to 2nd pass
			if check_validation(cle_stem) == False:
				PASS_FLAG = True
				du1_stem  = clean_duplication(cle_stem, DUPLICATE)
				pre_stem  = clean_prefix(du1_stem, PREFIX)
				rep_stem  = clean_repitition(pre_stem, REPITITION)
				inf_stem  = clean_infix(rep_stem, INFIX)
				rep_stem  = clean_repitition(inf_stem, REPITITION)
				suf_stem  = clean_suffix(rep_stem, SUFFIX)
				du2_stem  = clean_duplication(suf_stem, DUPLICATE)
				cle_stem  = clean_stemmed(du2_stem, CLEANERS, REPITITION)
				cle_stem  = clean_duplication(cle_stem, DUPLICATE)

			word_info["root"]   = cle_stem
			word_info["prefix"] = PREFIX
			word_info["infix"]  = INFIX
			word_info["suffix"] = SUFFIX
			word_info["repeat"] = REPITITION
			word_info["dupli"]  = DUPLICATE
			word_info["clean"]  = CLEANERS

			PASS_FLAG  = False
			PREFIX     = []
			INFIX      = []
			SUFFIX     = []
			DUPLICATE  = []
			REPITITION = []
			CLEANERS   = []

		else:
			PERIOD_FLAG = False
			cle_stem = clean_stemmed(token, CLEANERS, REPITITION)
			word_info["root"]   = token
			word_info["prefix"] = '[]'
			word_info["infix"]  = '[]'
			word_info["suffix"] = '[]'
			word_info["repeat"] = '[]'
			word_info["dupli"]  = '[]'
			word_info["clean"]   = '[]'

		stemmed.append(word_info)
		root_only.append(word_info["root"])
		word_root.append(word_info["word"] + ' : ' + word_info["root"])

		if info_dis == '1':
			print(token + ' : ' + word_info["root"])
		else:
			print(token + ' : ' + word_info["root"] + ' = ', word_info)

		word_info = {}
		pre_stem = inf_stem = suf_stem = rep_stem = \
		du1_stem = du2_stem = cle_stem = '-'

	write_file(stemmed, word_root, root_only)
	print('Accuracy: ' + str(validate(root_only, errors)) + '%')
	print('Errors: ' + (str(set(errors)) if len(errors) >= 1 else '[]'))

	return stemmed, root_only


def clean_duplication(token, DUPLICATE):
	"""
		Checks token for duplication. (ex. araw-araw = araw)
			token: word to be stemmed duplication
		returns STRING
	"""

	if check_validation(token):
		return token

	if '-' in token and token.index('-') != 0 and \
		token.index('-') != len(token) -  1:

		split = token.split('-')

		if all(len(tok) >= 3 for tok in split):
			if split[0] == token[1] or split[0][-1] == 'u' and change_letter(split[0], -1, 'o') == split[1] or \
				split[0][-2] == 'u' and change_letter(split[0], -2, 'o')  == split[1]:
				DUPLICATE.append(split[0])
				return split[0]

			elif split[0] == split[1][0:len(split[0])]:
				DUPLICATE.append(split[1])
				return split[1]

			elif split[0][-2:] == 'ng':
				if split[0][-3] == 'u':
					if split[0][0:-3] + 'o' == split[1]:
						print('test')
						DUPLICATE.append(split[1])
						return split[1]

				if split[0][0:-2] == split[1]:
					print('test')
					DUPLICATE.append(split[1])
					return split[1]

		else:
			return '-'.join(split)
	
	return token


def clean_repitition(token, REPITITION):
	"""
		Checks token for repitition. (ex. nakakabaliw = nabaliw)
			token: word to be stemmed repitition
		returns STRING
	"""

	if check_validation(token):
		return token

	if len(token) >= 4:
		if check_vowel(token[0]):
			if token[0] == token[1]:
				REPITITION.append(token[0])
				return token[1:]

		elif check_consonant(token[0]) and count_vowel(token) >= 2:
			if token[0: 2] == token[2: 4] and len(token) - 2 >= 4:
				REPITITION.append(token[2:4])
				return token[2:]
			
			elif token[0: 3] == token[3: 6] and len(token) - 3 >= 4:
				REPITITION.append(token[3:6])
				return token[3:]

	return token


def clean_prefix(token,	 PREFIX):
	"""
		Checks token for prefixes. (ex. naligo = ligo)
			token: word to be stemmed for prefixes
		returns STRING
	"""

	if check_validation(token):
		return token

	for prefix in PREFIX_SET:
		if len(token) - len(prefix) >= 3 and \
			count_vowel(token[len(prefix):]) >= 2:

			if prefix == ('i') and check_consonant(token[2]):
				continue

			if '-' in token:	
				token = token.split('-')

				if token[0] == prefix and check_vowel(token[1][0]):
					PREFIX.append(prefix)
					return token[1]

				token = '-'.join(token)

			if token[0: len(prefix)] == prefix:
				if count_vowel(token[len(prefix):]) >= 2:
					# if check_vowel(token[len(token) - len(prefix) - 1]):
				# 	continue

					if prefix == 'panganga':
						PREFIX.append(prefix)
						return 'ka' + token[len(prefix):]
					
					PREFIX.append(prefix)
					return token[len(prefix):]

	return token

 
def clean_infix(token, INFIX):
	"""
		Checks token for infixes. (ex. bumalik = balik)
			token: word to be stemmed for infixes
		returns STRING
	"""

	if check_validation(token):
		return token

	for infix in INFIX_SET:
		if len(token) - len(infix) >= 3 and count_vowel(token[len(infix):]) >= 2:
			if token[0] == token[4] and token[1: 4] == infix:
				INFIX.append(infix)
				return token[4:]

			elif token[2] == token[4] and token[1: 3] == infix:
				INFIX.append(infix)
				return token[0] + token[3:]

			elif token[1: 3] == infix and check_vowel(token[3]):
				INFIX.append(infix)
				return token[0] + token[3:]

	return token


def clean_suffix(token, SUFFIX):
	"""
		Checks token for suffixes. (ex. bigayan = bigay)
			token: word to be stemmed for suffixes
		returns STRING
	"""
	
	if check_validation(token):
		return token
	
	for suffix in SUFFIX_SET:
		if len(token) - len(suffix) >= 3 and count_vowel(token[0:len(token) - len(suffix)]) >= 2:

			if token[len(token) - len(suffix): len(token)] == suffix:
				if len(suffix) == 2 and not count_consonant(token[0:len(token) - len(suffix)]) >= 1:
					continue

				if count_vowel(token[0: len(token) - len(suffix)]) >= 2:
					if suffix == 'ang' and check_consonant(token[-4]) \
						and token[-4] != 'r' and token[-5] != 'u':
						continue

					# if check_vowel(suffix[0]) and check_consonant(token[len])
		
					SUFFIX.append(suffix)

					return token[0: len(token) - len(suffix)] + 'a' if SUFFIX == 'ita' \
						else  token[0: len(token) - len(suffix)]
 
	return token


def check_vowel(substring):
	"""
		Checks if the substring is a vowel.
			letters: substring to be tested
		returns BOOLEAN
	"""

	return all(letter in VOWELS for letter in substring)


def check_consonant(substring):
	"""
		Checks if the letter is a consonant.
			letter: substring to be tested
		returns BOOLEAN
	"""

	return all(letter in CONSONANTS for letter in substring)



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


def count_consonant(token):
	"""
		Count consonants in a given token.
			token: string to be counted for consonants
		returns INTEGER
	"""

	count = 0

	for tok in token:
		if check_consonant(tok):
			count+=1

	return count


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


def clean_stemmed(token, CLEANERS, REPITITION):
	"""
		Checks for left-over affixes and letters.
			token: word to be cleaned for excess affixes/letters
		returns STRING
	"""

	global PERIOD_FLAG
	global PASS_FLAG

	CC_EXP = ['gl', 'gr', 'ng', 'kr', 'kl', 'kw', 'ts', 'tr', 'pr', 'sw', 'sy'] # Consonant + Consonant Exceptions

	if token[-1] == '.' and PASS_FLAG == False:
		PERIOD_FLAG = True

	if not check_vowel(token[-1]) and not check_consonant(token[-1]):
		CLEANERS.append(token[-1])
		token = token[0:-1]

	if not check_vowel(token[0]) and not check_consonant(token[0]):
		CLEANERS.append(token[0])
		token = token[1:]

	if check_validation(token):
		return token

	if len(token) >= 3 and count_vowel(token) >= 2:
		token = clean_repitition(token,	REPITITION)

		if check_consonant(token[-1]) and token[- 2] == 'u':
			CLEANERS.append('u')
			token = change_letter(token, -2, 'o')

		if token[len(token) - 1] == 'u':
			CLEANERS.append('u')
			token = change_letter(token, -1, 'o')

		if token[-1] == 'r':
			CLEANERS.append('r')
			token = change_letter(token, -1, 'd')

		if token[-1] == 'h' and check_vowel(token[-1]):
			CLEANERS.append('h')
			token = token[0:-1]

		# if token[0] == 'i':
		# 	token = token[1:]

		if token[0] == token[1]:
			CLEANERS.append(token[0])
			token = token[1:]

		if (token[0: 2] == 'ka' or token[0: 2] == 'pa') and check_consonant(token[2]) \
			and count_vowel(token) >= 3:
			
			CLEANERS.append(token[0: 2])
			token = token[2:]

		if(token[-3:]) == 'han' and count_vowel(token[0:-3]) == 1:
			CLEANERS.append('han')
			token = token[0:-3] + 'i'

		if(token[-3:]) == 'han' and count_vowel(token[0:-3]) > 1:
			CLEANERS.append('han')
			token = token[0:-3]

		if len(token) >= 2 and count_vowel(token) >= 3:
			if token[-1] == 'h' and check_vowel(token[-2]):
				CLEANERS.append('h')
				token = token[0:-1]

		if len(token) >= 6 and token[0:2] == token[2:4]:
			CLEANERS.append('0:2')
			token = token[2:]

		if any(REP[0] == 'r' for REP in REPITITION):
			CLEANERS.append('r')
			token = change_letter(token, 0, 'd')

		if token[-2:] == 'ng' and token[-3] == 'u':
			CLEANERS.append('u')
			token = change_letter(token, -3, 'o')

		if token[-1] == 'h':
			CLEANERS.append('h')
			token = token[0:-1]

		if any(token[0:2] != CC for CC in CC_EXP) and check_consonant(token[0:2]):
			CLEANERS.append(token[0:2])
			token = token[1:]

	return token


def read_file(source):
	"""
		Gets content of a text file.
			source: file name
		returns LIST
	"""

	with open(source, 'r') as myfile:
		data = myfile.read().replace('\n', ' ')

	return data.split(' ')


def write_file(stemmed_info, word_root, root):
	"""
		Creates a log for the output.
			stemmed_info: list of dicts with stemming info
			word_root: format [word : root]
			root: list of stemmed words
		returns NULL
	"""

	with open('output/with_info.txt', 'w') as with_info, \
		open('output/root_word.txt', 'w') as root_word, \
		open('output/root_only.txt', 'w') as root_only:
		
		for inf, rw, ro in zip(stemmed_info, word_root, root):
			with_info.write(str(inf) + '\n')
			root_word.write(rw + '\n')
			root_only.write(ro + '\n')


def check_validation(token):
	with open('validation.txt', 'r') as valid:
		data = valid.read().replace('\n', ' ')

	return True if token in data else False



def validate(stemmed, errors):
	"""
		Calculates accuracy.
			stemmed: list of stemmed words
			errors: list of stemming errors
		returns FLOAT
	"""

	check = 0

	with open('validation.txt', 'r') as valid:
		data = valid.read().replace('\n', ' ')
		
	for stem in stemmed:
		if stem[0].isupper() or stem in data:
			check += 1

		else:
			errors.append(stem)
	
	return format((float(check) / len(stemmed) * 100), '.2f') # Python 2.7
	# return format((check / len(stemmed) * 100), '.2f') # Python 3.0



mode = sys.argv[1] # 1: Text File // 2: Raw String
source = sys.argv[2] # 1: .txt name // 2: raw string
info_dis = sys.argv[3] # 1: no info // 2: show info

if __name__ == "__main__":
	stemmer(mode, source, info_dis)


"""
TODOS:
	mangingisdang : gingisda
	napapakinggan : pakingg
	if prefix[-1] = c >> should be v + c
	partial >> if token[0] == token[1][0:len(token[0])] >> ret token[1]
	prefix >> if - in token > if tok - prefix != tok2 > return token
	punong-bayan : punong-bay
	tagpuan : puan
	katangi-tanging : tangi-tang
	panana = s?
	nin?
	syon?
	Validation: 5000
"""