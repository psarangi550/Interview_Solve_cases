import calendar

#iterating over the calender month dates

c=calendar.Calendar()

# for date in c.itermonthdates(2022,1):
# 	print(date)


#iterating over the calender days

for date in c.itermonthdays(2022,1):
	print(date)