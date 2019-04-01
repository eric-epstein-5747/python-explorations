 x = int(input('Enter an integer.'))
root = 0
while root < abs(x):
	for i in range(0,6):
		if root**i == abs(x):
			if x > 0:
				print('root = ', root, 'pwr =', i, '.', x, '=', root, '**', i)
				break
			else: 
				print('root = ', root*(-1), 'pwr =', i, '.', x, '=', root*(-1), '**', i)
				break
			
	root = root + 1
if root==abs(x):
	if x > 0: 
		print('root = ', root, 'pwr =', '1', x, '=', root, '**', '1')
	else: 
		print('root = ', root*(-1), 'pwr =', '1', x, '=', root*(-1), '**', '1')