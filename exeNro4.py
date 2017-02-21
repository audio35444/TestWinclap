class ListIsEmpty(Exception):
	def __init__(self,value):
		self.value = value
	def __str__(self):
		return self.value

def sleeping(N):
	if N > 0:
		listNums = [True for item in range(10)]
		T = 0
		while True:
			T+=1
			NumRound= N*T
			while NumRound >= 1:
				rest = NumRound % 10
				listNums[rest] = False
				if not(any(listNums)):
					return str(T*N)
				NumRound = NumRound /10

	return 'INSOMNIA'

if __name__ == '__main__':
	try:
		listNums = [item.rstrip() for item in open('c-input.in')]
		if max(listNums)>200:
			for element in listNums:
				if int(element) > 200:
					listNums.remove(element)
		
		if len(listNums)> 100:
			listNums = listNums[:100]
		elif len(listNums)<1:
			raise ListIsEmpty('The list is Empty')
		i = 0
		for element in listNums:
			i+=1
			print ('CASE #%s: %s'%(i,sleeping(int(element))))
	except ListIsEmpty as msg:
		print msg
	except ValueError as msg:
		print msg
	except :
		print 'You need support, please send a message to juaninsis@gmail.com'
