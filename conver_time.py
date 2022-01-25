t1 = '17:30'
t2 = '12:50 am'

def convert_time(time):
	time_list = time.split()
	if time_list[-1] == 'am' or time_list[-1] == 'pm':
		hour, mint = time_list[0].split(':')
		hour = 12 + (int(hour)%12) if time_list[-1] == 'pm' else int(hour)%12
		return f"{hour}:{mint}"
	else:
		hour, mint = time_list[0].split(':')
		p = 'pm' if int(hour) >= 13 else 'am'
		hour = int(hour)%12
		return f'{hour}:{mint} {p}'

print(convert_time(t1))