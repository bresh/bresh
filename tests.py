def is_year_leap(year):
#
# Your code from LAB 4.3.1.6.
#
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
             return True
    else:
        return False
def days_in_month(year, month):
#
# Write your new code here.
#
    if month % 2 == 0:
        if month == 2 and is_year_leap(year):
            n = 28
            return n
        else:
            z = 29
            return z
            
        x = 30
        return x
    else:
        y = 31
        return y
        
    
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print(result)
	else:
		print("nada")