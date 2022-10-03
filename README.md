# Tagalog Words Stemmer using Python

### Description:

Tagalog Words Stemmer is a program that processes Tagalog words by removing all of its affixes and returns the root of the words.

### Sample Output:

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
- {'prefix': ['pa'], 'clean': [], 'infix': [], 'root': 'tuloy', 'repeat': [], 'suffix': [], 'word': 'Patuloy', 'dupli': []}
- {'prefix': '[]', 'clean': '[]', 'infix': '[]', 'root': 'pa', 'repeat': '[]', 'suffix': '[]', 'word': 'pa', 'dupli': '[]'}
- {'prefix': [], 'clean': [], 'infix': [], 'root': 'din', 'repeat': [], 'suffix': [], 'word': 'din', 'dupli': []}
- {'prefix': [], 'clean': [], 'infix': [], 'root': 'sila', 'repeat': [], 'suffix': [], 'word': 'sila', 'dupli': []}
- {'prefix': [], 'clean': [], 'infix': [], 'root': 'sa', 'repeat': [], 'suffix': [], 'word': 'sa', 'dupli': []}
- {'prefix': ['pag'], 'clean': [], 'infix': [], 'root': 'hanap', 'repeat': ['ha'], 'suffix': [], 'word': 'paghahanap', 'dupli': []}
- {'prefix': [], 'clean': [], 'infix': [], 'root': 'ng', 'repeat': [], 'suffix': [], 'word': 'ng', 'dupli': []}
- {'prefix': [], 'clean': [], 'infix': [], 'root': 'posible', 'repeat': [], 'suffix': ['ng'], 'word': 'posibleng', 'dupli': []}
- {'prefix': [], 'clean': [], 'infix': [], 'root': 'gamot', 'repeat': [], 'suffix': [], 'word': 'gamot', 'dupli': []}
- {'prefix': [], 'clean': [], 'infix': [], 'root': 'sa', 'repeat': [], 'suffix': [], 'word': 'sa', 'dupli': []}
- {'prefix': ['ma'], 'clean': [], 'infix': [], 'root': 'lubha', 'repeat': [], 'suffix': ['ng'], 'word': 'malubhang', 'dupli': []}
- {'prefix': [], 'clean': [], 'infix': [], 'root': 'sakit', 'repeat': [], 'suffix': [], 'word': 'sakit', 'dupli': []}
- {'prefix': [], 'clean': [], 'infix': [], 'root': 'ng', 'repeat': [], 'suffix': [], 'word': 'ng', 'dupli': []}
- {'prefix': [], 'clean': [], 'infix': ['in'], 'root': 'daramdam', 'repeat': [], 'suffix': [], 'word': 'dinaramdam', 'dupli': []}
- {'prefix': [], 'clean': [], 'infix': [], 'root': 'ng', 'repeat': [], 'suffix': [], 'word': 'ng', 'dupli': []}
- {'prefix': [], 'clean': [], 'infix': [], 'root': 'kanya', 'repeat': [], 'suffix': ['ng'], 'word': 'kanyang', 'dupli': []}
- {'prefix': [], 'clean': ['.'], 'infix': [], 'root': 'ina', 'repeat': [], 'suffix': [], 'word': 'ina.', 'dupli': []} <br />


##### validation
- Accuracy: 94.12%
- Errors: ['daramdam'] <br />

### Usage:
> python TglStemmer.py [mode] [source] [info] <br />
- **modes:** [1: text_file] [2: raw_string]
- **source:** [1: file_name] [2: "raw_string"]
- **info:** [1 word-root] [2: show_word_info] <br />

### Fix List:
- [x] mag-aa
- [x] mag-alinlangan : g-alinlang ??
- [x] lalung-lalo
- [x] mangitlog : gitlog
- [ ] mangingisdang : gingisda
- [ ] napapakinggan : pakingg
- [x] pagkakasunod-sunod : sunod-sunod???
- [x] pinagtratrabahuhan : ratrabaho ???
- [x] 2nd pass
- [x] bibigay = igay?
- [ ] if prefix[-1] = c >> should be v + c
- [x] kaluguran : lugor
- [ ] partial >> if token[0] == token[1][0:len(token[0])] >> ret token[1]
- [x] prefix + partial dupli 
- [ ] prefix >> if - in token > if tok - prefix != tok2 > return token
- [ ] punong-bayan : punong-bay
- [ ] tagpuan : puan
- [x] tsismis : sismis
- [ ] katangi-tanging : tangi-tang
- [x] validation data
- [x] period tracker
