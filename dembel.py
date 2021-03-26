try:
	start_day = int(input('How days you are in army: '))
except:
	print('Only numbers:  ')
	start_day = int(input('How days you are in army: '))
try:
	year = int(input('Year/Start  '))
	second_year = year + 1
	if (2021 - year) > 2:
		print('Carayutyunt tevum e 2 tari,sxal tvyalner')
		raise ValueError
except ValueError:
	print('Try again')
	year = int(input('Year/Start  '))
	second_year = year + 1

days = 0
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
	days = 365 + 366
elif second_year % 4 == 0 and second_year % 100 != 0 or second_year % 400 == 0:
	days = 365 + 366
else:
	days = 365 + 365

if start_day < 365:
	mnacord = days - start_day
	print('Dzez mnac-->' ,mnacord, 'or')
else:
	mnacord = days - start_day - 365
	print('Dzez mnac-->' ,mnacord, 'or')



