#!/usr/bin/python

# start with defining variables
ss = 0.062
medicare = 0.0145 
wage = float(input('How much do you make per hour?:\n'))
hours = float(input('How many hours do you work per pay period?:\n'))
period = lower(input('How often do you get paid, valid options include;\n Daily, Weekly, Bi-Weekly, Semi-Monthly, Monthly, Custom\n (custom values are in months) \n'))
exempt = input('Are you exempt from income tax? (0 for no 1 for yes)\n')
state = input('What state do you reside in?\n')
marital_status = int(input('Are you married? (0 for no 1 for yes)\n'))
# joint status
if (marital_status==1):
	joint = input('Are you filing seperately, or jointly. (0 for seperate 1 for jointly')


# a few functions to make for easier reading
def tax_calc():
	"calculates tax percentage"
	if (gross < 9225):
		tax = 0.1
		print ("Less than $9225")
	elif(gross < 37450):
		tax = 0.15
		print ("Less than $37,450 more than $9,225")
	elif(gross < 90750):
		tax = 0.25
		print ("Less than $90,750")
	elif(gross < 189300):
		tax = 0.28
		print ("Less than $189,300")
	elif(gross < 411500):
		tax = 0.33
		print ("Less than $411,500")
	elif(gross < 413200):
		tax = 0.396
		print ("Less than $413,200")
	return tax

def ann_gross_calc():
	if (isdigit(period)):
		ann = float(period)*
	elif (period == daily):
		
	elif (period == weekly):
		
	elif (period == bi-weekly or period == biweekly):
		
	elif (period == semi-monthly or period == semimonthly):
		
	elif (monthly == monthly):
		
	return ann_gross

# next we'll calculate allowances
if (exempt==1):
	ex = 0
else:
	ex = 1

allowances = ex + marital_status + int(input('Can you claim anyone besides yourself?\n (Additional Allowances in number 0 for no)\n'))

# verify allowances are accurate
print("Is ", allowances, " the correct amount of allowances \n(If you can't file exempt it should be at least 1)\n")

# calculate gross per period then annually
gross_period = float(wage*hours)
ann_gross = ann_gross_calc();

tax = tax_calc();
net = gross - ((gross * tax) + (gross * ss) + (gross * medicare))

print("Gross pay: $", gross, "\n Net Pay: $", net ) #,"""

#Taxes: """,  ,"""
#State: """,  ,"""
#Federal: """)
