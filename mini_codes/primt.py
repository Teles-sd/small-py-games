#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Apr  7 20:37:22 2020

@author: teles
"""


def primt(mat,pad=3):
	'''
	mat: matrix
	pad: padding given to write the values
	'''
	
	if mat == []:
		print('Empty')
		return
	
	from functools import reduce
	
	# biggest line length
	b_lin = reduce( (lambda a,b: a if a>b else b) , [len(lin) for lin in mat] )
	
	# biggest length in string form from every element on matrix
	pad = reduce( (lambda a,b: a if a>b else b) , [len(str(mat[i][j])) for i in range(len(mat)) for j in range(len(mat[i]))] + [pad] )
	
	# adds empty elements to the lines that are smaller than the biggest
	mat = [ lin + (['']*(b_lin-len(lin))) for lin in mat]
	
	# print
	print( ('-'*pad).join(','*(b_lin+1)) )
	print('\n'.join( ( '|' + ('{:^{pad}}|'*len(row)).format( *row ,pad=pad) ) for row in mat ))
	print( ('-'*pad).join("'"*(b_lin+1)) )
	




### TESTS ###

if __name__ == "__main__":

	print()

	import pprint

	inf = float('inf')

	A = [[0,1,4,inf,3],  [1,0,2,inf,4], [4,2,0,1,5], [inf,inf,1,0,3], [3,4,5,3,0]]

	print('primt(A):')
	print()
	primt(A)
	print()


	print('pprint(A):')
	print()
	pprint.pprint(A)
	print()

	print()
	print('----')
	print()


	B = [[0,1,4,5],  [1,0,2,5,4, 3], [4,2,16151650,1,5], [5,5,1,0,3], [3]]

	print('primt(B):')
	print()
	primt(B,5)
	print()


	print('pprint(B):')
	print()
	pprint.pprint(B)
	print()

	primt([])
