def thousands_with_commas(i):
	if isinstance(i,int):
		return '{:,}'.format(i)
	else:
		raise ValueError('Please, enter only numbers')    

if __name__ == '__main__':
	try:
		assert thousands_with_commas(1234)== '1,234'
		assert thousands_with_commas(123456789) == '123,456,789'
		assert thousands_with_commas(12)== '12'
	except ValueError as msgError:
		print msgError
	except Exception:
		print 'You need support, please send a message to juaninsis@gmail.com'