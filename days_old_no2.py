'''
Days old #2
Given your birthday and the current date, calculate your age in 
days. Compensate for leap days. Assume that the birthday and 
current date are correct dates (and no time travel). Simply put, 
if you were born 1 Jan 2012 and todays date is 2 Jan 2012 you 
are 1 day old.

Hint
A whole year is 365 days, 366 if a leap year. If you know how many 
days it is from 1 Jan until a certain date, you also know how many 
days there are left from that date until 31 Dec.
'''


daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    ##
    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    ##
    '''
    if (year is not divisible by 4) then (it is a common year)
    else
    if (year is not divisible by 100) then (it is a leap year)
    else
    if (year is not divisible by 400) then (it is a common year)
    else (it is a leap year)
    '''
    if year % 4 == 0:
        return False
    elif year % 100 == 0:
        return True
    elif year % 400 == 0:
        return False
    else:
        return True

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    ##
    # Your code here.
    ##
    return days

def extraFunction(???):
    ##
    # ???
    ##


def test():
    assert daysBetweenDates(2012,1,1,2012,2,28) == 58   
    assert daysBetweenDates(2012,1,1,2012,3,1) == 60
    assert daysBetweenDates(2011,6,30,2012,6,30) == 366
    assert daysBetweenDates(2011,1,1,2012,8,8) == 585
    assert daysBetweenDates(1900,1,1,1999,12,31) == 36523
