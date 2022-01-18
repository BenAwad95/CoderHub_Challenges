# TODO convert date format yyyy-mm-dd to dd-mm-yyyy
# example 2020-02-10 to 10-02-2020

# 1
def date_formating(date):
	date = date.strip()
	year = date[:4]
	month = date[5:7]
	day = date[8:]
	return f"{day}-{month}-{year}"

# 2
from datetime import datetime
def date_formating(date):
  date = date.strip()
  return datetime.strptime(date, "%Y-%m-%d").strftime("%d-%m-%Y")

# 3
def date_formating(date):
	date = date.strip()
	year, month, day = date.split('-')
	return '-'.join((year, month, day))


print(date_formating("1932-09-23"))

