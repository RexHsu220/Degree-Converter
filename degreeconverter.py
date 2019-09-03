print('1 : Celsius Degree to Ferenheit Degree')
print('2 : Ferenheit to Celsius Degree')
mode = eval(input('Please enter the mode you want: '))
if mode == 1:
	c = eval(input('Please enter a celsius degree: '))
	fmla1 = (c * 9 / 5) + 32
	print('%s Degree Celsius = %4.1f Degree Ferenheit' % (c, fmla1))
else:
	f = eval(input('Please enter a Ferenheit degree: '))
	fmla2 = (f - 32) * 5 /9
	print('%s Degree Ferenheit = %4.1f Degree Celsius' % (f, fmla2))
