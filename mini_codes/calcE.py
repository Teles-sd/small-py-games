def e(dec=2):
	'''
	Calculates e, with given decimal precision, and returns it.
	
	Brothers' Formulae
	
	
	For comparison, e truncated to 50 decimal places:
	e = 2.71828182845904523536028747135266249775724709369995
	
	
	
	Reference:
	Brothers' Formulae (2004)
	url: (https://www.intmath.com/exponential-logarithmic-functions/calculating-e.php)
	
	E Value
	url: (https://en.wikipedia.org/wiki/E_(mathematical_constant))
	
	'''
	
	import gmpy2
	from gmpy2 import mpfr
	gmpy2.get_context().precision=200
	
	e_val = mpfr('2.71828182845904523536028747135266249775724709369995')
	e_cal = 0
	
	def factorial(num):
		ans = 1
		
		# ye, I know there no factorial of negative numbers, but we are not getting on the negatives here ok?
		# chill mate
		# nor fractions
		
		if num >=1 :
			
			for i in range(2, num+1):
				ans *= i
			
		return mpfr(ans)
		
	
	def bro():
		
		N = dec
		
		e = mpfr('0')
		
		for n in range(N+1):
			e += (2*n + 2)/factorial(2*n + 1)
		
		return e
		
	
	def truncate():
		
		nonlocal e_val
		nonlocal e_cal
		
		i, p, d = str(e_val).partition('.')
		e_val = mpfr( '{i}.{d}'.format(i=i, d=d[:dec]) )
		
		i, p, d = str(e_cal).partition('.')
		e_cal = mpfr( '{i}.{d}'.format(i=i, d=d[:dec]) )
		
	
	def compare():
		nonlocal e_val
		nonlocal e_cal
		
		if e_cal != e_val:
			print('')
			print('Diverges!')
			print('e:')
			print(e_val)
			print('e_cal:')
			print(e_cal)
			print('')
			
		
	
	# Calculate
	
	e_cal = bro()
	
	truncate()
	compare()
	
	return e_cal
		
	





### TESTS ###

if __name__ == '__main__':
	import os
	clear = lambda: os.system('clear')
	
	clear()
	
	'''
	dec = 6
	
	print('E:')
	print(float(e(dec)))
	print()
	print()
	'''
	
	for dec in range(0, 52):
		
		print()
		en = e(dec)
		print('E (prec: %d):' % dec)
		print(('{:.%d}'%dec).format(en))
		print()








