# TagalogStemmerPython
## Tagalog Words Stemmer using Python
By: Carl Jerwin F. Gensaya, PUP 4th Year ComSci Student <br />
__
###### Usage:
python TglStemmer.py [mode] [source] [info] <br />
- **modes:** [1: text_file] [2: raw_string]
- **source:** [1: file_name] [2: "raw_string"]
- **info:** [1 word-root] [2: show_word_info]<br />

##### ToDo-List:
- [ ] mag-aa
- [ ] mag-alinlangan : g-alinlang ??
- [ ] lalung-lalo
- [ ] mangitlog : gitlog
- [ ] mangingisdang : gingisda
- [ ] napapakinggan : pakingg
- [ ] pagkakasunod-sunod : sunod-sunod???
- [ ] pinagtratrabahuhan : ratrabaho ???
- [ ] 2nd pass
- [ ] bibigay = igay?
- [ ] if prefix[-1] = c >> should be v + c
- [ ] kaluguran : lugor
- [ ] partial >> if token[0] == token[1][0:len(token[0])] >> ret token[1]
- [ ] prefix + partial dupli 
- [ ] prefix >> if - in token > if tok - prefix != tok2 > return token
- [ ] punong-bayan : punong-bay
- [ ] tagpuan : puan
- [ ] tsismis : sismis
- [ ] katangi-tanging : tangi-tang
- [ ] validation data