# Tagalog Words Stemmer using Python
_By: Carl Jerwin F. Gensaya, PUP 4th Year ComSci Student_ <br /> <br />

##### Description:

Tagalog Words Stemmer is a program that processes Tagalog words by removing all of its affixes and returns the root of the words.

##### Sample Output:

> _Input: "Patuloy pa din sila sa paghahanap ng posibleng gamot sa malubhang sakit ng dinaramdam ng kanyang ina."_ <br />

##### word : root
- patuloy : tuloy
- pa : pa
- din : din
- sila : sila
- sa : sa
- paghahanap : hanap
- ng : ng
- posibleng : posible
- gamot : gamot
- sa : sa
- malubhang : lubha
- sakit : sakit
- ng : ng
- dinaramdam : daramdam
- ng : ng
- kanyang : kanya
- ina. : ina <br />

##### word_info
- {'dup#1': [], 'repeat': [], 'root': 'tuloy', 'word': 'patuloy', 'dup#2': [], 'infix': [], 'suffix': [], 'prefix': ['pa']}
- {'dup#1': [], 'repeat': [], 'root': 'pa', 'word': 'pa', 'dup#2': [], 'infix': [], 'suffix': [], 'prefix': []}
- {'dup#1': [], 'repeat': [], 'root': 'din', 'word': 'din', 'dup#2': [], 'infix': [], 'suffix': [], 'prefix': []}
- {'dup#1': [], 'repeat': [], 'root': 'sila', 'word': 'sila', 'dup#2': [], 'infix': [], 'suffix': [], 'prefix': []}
- {'dup#1': [], 'repeat': [], 'root': 'sa', 'word': 'sa', 'dup#2': [], 'infix': [], 'suffix': [], 'prefix': []}
- {'dup#1': [], 'repeat': ['ha'], 'root': 'hanap', 'word': 'paghahanap', 'dup#2': [], 'infix': [], 'suffix': [], 'prefix': ['pag']}
- {'dup#1': [], 'repeat': [], 'root': 'ng', 'word': 'ng', 'dup#2': [], 'infix': [], 'suffix': [], 'prefix': []}
- {'dup#1': [], 'repeat': [], 'root': 'posible', 'word': 'posibleng', 'dup#2': [], 'infix': [], 'suffix': ['ng'], 'prefix': []}
- {'dup#1': [], 'repeat': [], 'root': 'gamot', 'word': 'gamot', 'dup#2': [], 'infix': [], 'suffix': [], 'prefix': []}
- {'dup#1': [], 'repeat': [], 'root': 'sa', 'word': 'sa', 'dup#2': [], 'infix': [], 'suffix': [], 'prefix': []}
- {'dup#1': [], 'repeat': [], 'root': 'lubha', 'word': 'malubhang', 'dup#2': [], 'infix': [], 'suffix': ['ng'], 'prefix': ['ma']}
- {'dup#1': [], 'repeat': [], 'root': 'sakit', 'word': 'sakit', 'dup#2': [], 'infix': [], 'suffix': [], 'prefix': []}
- {'dup#1': [], 'repeat': [], 'root': 'ng', 'word': 'ng', 'dup#2': [], 'infix': [], 'suffix': [], 'prefix': []}
- {'dup#1': [], 'repeat': [], 'root': 'daramdam', 'word': 'dinaramdam', 'dup#2': [], 'infix': ['in'], 'suffix': [], 'prefix': []}
- {'dup#1': [], 'repeat': [], 'root': 'ng', 'word': 'ng', 'dup#2': [], 'infix': [], 'suffix': [], 'prefix': []}
- {'dup#1': [], 'repeat': [], 'root': 'kanya', 'word': 'kanyang', 'dup#2': [], 'infix': [], 'suffix': ['ng'], 'prefix': []}
- {'dup#1': [], 'repeat': [], 'root': 'ina', 'word': 'ina.', 'dup#2': [], 'infix': [], 'suffix': [], 'prefix': []} <br />

##### Usage:
python TglStemmer.py [mode] [source] [info] <br />
- **modes:** [1: text_file] [2: raw_string]
- **source:** [1: file_name] [2: "raw_string"]
- **info:** [1 word-root] [2: show_word_info]<br />

##### ToDo-List:
- [x] mag-aa
- [x] mag-alinlangan : g-alinlang ??
- [ ] lalung-lalo
- [x] mangitlog : gitlog
- [ ] mangingisdang : gingisda
- [ ] napapakinggan : pakingg
- [x] pagkakasunod-sunod : sunod-sunod???
- [x] pinagtratrabahuhan : ratrabaho ???
- [ ] 2nd pass
- [x] bibigay = igay?
- [ ] if prefix[-1] = c >> should be v + c
- [x] kaluguran : lugor
- [ ] partial >> if token[0] == token[1][0:len(token[0])] >> ret token[1]
- [ ] prefix + partial dupli 
- [ ] prefix >> if - in token > if tok - prefix != tok2 > return token
- [ ] punong-bayan : punong-bay
- [ ] tagpuan : puan
- [x] tsismis : sismis
- [ ] katangi-tanging : tangi-tang
- [ ] validation data