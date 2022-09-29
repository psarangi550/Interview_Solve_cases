# import calendar #importing the calender module 
# calendar.setfirstweekday(calendar.SUNDAY)
# print(calendar.firstweekday())


import calendar


# fetching the particular day_number in this case
#####################################################

# day_number=calendar.weekday(2015,5,8)
# print(day_number)

#fetching the calender with custom header as weekheader=3 and space as 1
###########################################################

# print(calendar.calendar(2022,3,1))


#fetch all the month and days 
#######################################

#here the month_name and day_name provide a localized_month and localized_date object based on that we can create the list over here


# print(list(calendar.month_name))

# print(list(calendar.day_name))


#how to change the weekday from default to particular value
############################################################


# calendar.setfirstweekday(calendar.SUNDAY)

# print(calendar.weekheader(2))

# print(calendar.firstweekday())

#checking whether a leap year or not
############################################

# print(calendar.isleap(2020))

#checking the leapday between the years 
###########################################

# print(calendar.leapdays(2016,2022))

#finding the day value from the particular date value is 
#########################################################

freedom_day=calendar.weekday(1947,8,15)

# print(freedom_day)

all_day=list(calendar.day_name)

for i in range(len(all_day)):
	if i==freedom_day:
		print(all_day[i])
		
