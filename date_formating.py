# TODO convert date format yyyy-mm-dd to dd-mm-yyyy
# example 2020-02-10 to 10-02-2020


def date_formating(date):
	import datetime
	# year = date[:4]
	# month = date[5:7]
	# day = date[8:]
	# return day + "-" + month + "-" + year 
	date_obj = datetime.datetime.strptime(date, "%Y-%m-%d")
	out = date_obj.strftime("%d-%m-%Y")
	return out

print(date_formating("1932-09-01"))