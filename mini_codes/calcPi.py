def pi(dec=2, alg='quadratic'):
	'''
	Calculates Pi with given decimal precision, and returns it.
	
	Borwein's Algorithm
	Iterative Algorithms
	
	For comparison, pi with 300 decimal cases precision:
	pi = 3,14159 26535 89793 23846 26433 83279 50288 41971 69399 37510 58209 74944 59230 78164 06286 20899 86280 34825 34211 70679 82148 08651 32823 06647 09384 46095 50582 23172 53594 08128 48111 74502 84102 70193 85211 05559 64462 29489 54930 38196 44288 10975 66593 34461 28475 64823 37867 83165 27120 19091 45648 56692 34603 48610 45432 66482 13393 60726 02491 41273
	
	Reference:
	Algorithms
	url: (https://en.wikipedia.org/wiki/Borwein%27s_algorithm#Iterative_algorithms)
	
	Pi Value
	url: (https://pt.wikipedia.org/wiki/Pi#Valor_de_%7F'%22%60UNIQ--postMath-00000008-QINU%60%22'%7F)
	
	GMPY2, MPFR
	url: (https://gmpy2.readthedocs.io/en/latest/mpfr.html)
	
	'''
	
	import gmpy2
	from gmpy2 import sqrt
	from gmpy2 import mpfr
	#gmpy2.get_context().precision=53
	gmpy2.get_context().precision=200
	
	pi_val = mpfr('3.14159265358979323846264338327950288419716939937510582097494459230781640628208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273')
	
	pi_cal = 3
	
	# Quadratic Convergence (1984)
	def quadCon():
		
		# Values
		a_n = 0
		a_np1 = 0
		b_n = 0
		b_np1 = 0
		p_n = 0
		p_np1 = 0
		pi_ = 0
		
		# Auxiliar Calculation Values
		a = sqrt(2)
		b = mpfr('0')
		p = ( 2 + sqrt(2) )
		
		def a_genNext():
			'''
			a(n+1)
			'''
			# Variable
			nonlocal a
			
			# To be updated
			nonlocal a_n
			nonlocal a_np1
			
			# Iteration
			a_n = a
			a = (sqrt(a_n) + (1/(sqrt(a_n)))) / 2
			a_np1 = a
			
		
		def b_genNext():
			'''
			b(n+1)
			'''
			# Variables
			nonlocal b
			nonlocal a_n
			
			# To be updated
			nonlocal b_n
			nonlocal b_np1
			
			# Iteration
			b_n = b
			b = ((1+b_n)*(sqrt(a_n))) / (a_n + b_n)
			b_np1 = b
			
		
		def p_genNext():
			'''
			Generates PI more and more precise, one iteration at a time.
			p(n+1)
			'''
			# Variables
			nonlocal p
			nonlocal a_np1
			nonlocal b_np1
			
			# To be updated
			nonlocal p_n
			nonlocal p_np1
			
			# Iteration
			p_n = p
			p = ((1+a_np1)*p_n*(b_np1)) / (1 + b_np1)
			p_np1 = p
			
		
		
		# The Calc
		for _ in range(dec):
			a_genNext()
			b_genNext()
			p_genNext()
		
		return p_np1
		
		### TESTS ###
		
		'''
		
		print()
		print('dec:')
		print(dec)
		print()
		
		# StartUp
		a_genNext()
		b_genNext()
		p_genNext()
		
		for n in range(dec):
			
			print('[n=%d]' %n)
			print()
			print(a_n)
			print(b_n)
			print(p_n)
			print()
			print()
			
			a_genNext()
			b_genNext()
			p_genNext()
		'''
		
	
	# Cubic Convergence (1991)
	def cubCon():
		
		a = ( 1/3 )
		s = ( (sqrt(3)-1)/2 )
		
	
	def truncate():
		nonlocal pi_val
		nonlocal pi_cal
		
		
		i, p, d = str(pi_val).partition('.')
		pi_val = mpfr( '{i}.{d}'.format(i=i, d=d[:dec]) )
		
		i, p, d = str(pi_cal).partition('.')
		pi_cal = mpfr( '{i}.{d}'.format(i=i, d=d[:dec]) )
		
	
	def compare():
		nonlocal pi_val
		nonlocal pi_cal
		
		if pi_cal != pi_val:
			print('')
			print('Diverges !')
			print('pi:')
			print(pi_val)
			print('pi_cal:')
			print(pi_cal)
			
		
	
	# Calculate
	
	try:
		alg.lower()
	except:
		alg = 'quadratic'
	
	algorithms = {'quadratic':quadCon, 'cubic':cubCon}
	
	pi_cal = algorithms[alg]()
	
	truncate()
	compare()
	
	return pi_cal
	




### TESTS ###

if __name__ == '__main__':
	
	import os
	clear = lambda: os.system('clear')
	
	clear()
	
	
	
	dec = 20
	
	print('Pi:')
	print(pi(dec))
	print()
	print()













