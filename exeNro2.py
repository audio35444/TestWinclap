def annograms(word):
	#words = [w.rstrip() if len(w)==len(word) else  for w in open('WORD.LST')]
	words = [] 
	for w in open('WORD.LST'):
		if len(w.rstrip())==len(word) and w.rstrip()!=word:
			stringNow=w.rstrip()
			for item in word:
				stringNow = stringNow.replace(item,'',1)
			if len(stringNow)==0:
				words.append(w.rstrip())	

	return words

if __name__=='__main__':
	print (annograms('train'))
	print '--'
	print (annograms('drive'))
	print '--'
	print (annograms('python'))



