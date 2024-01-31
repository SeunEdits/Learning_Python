def num_days(month):

    if month == 'jan' or 'mar' or 'may' or 'jul' or 'aug' or 'oct' or 'dec' :
        print('number of days in',month,'is',31)
    elif month == 'feb':
        print('number of days in',month,'is',28)
    elif month == 'apr' or 'jun' or 'sep' or 'nov':
        print('number of days in',month,'is',30)

num_days('aug')
# optimize/shorten the code in the function
# try to reduce the number of conditionals 
