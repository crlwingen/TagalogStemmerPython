# Tagalog Words Stemmer using Python
__By: Carl Jerwin F. Gensaya, PUP 4th Year ComSci Student__ <br />
###### Usage:
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