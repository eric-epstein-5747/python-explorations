s = input('Enter a sequence of decimal numbers separated by commas, with no spaces.')
remainder = s
i = 0
sum = 0
while i < len(s):
	if s[i] == ',': 
		j = 0
		while remainder[j] != ',': 
		    j = j+1   
		sum = sum + float(remainder[0:j])
		remainder = remainder[j+1:len(remainder)]
	i = i + 1
sum = sum + float(remainder)
print('s =', '`', s, '`', '.', 'Sum of rationals in s =', sum, '.')