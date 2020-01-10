## @file test_driver.py
#  @author Shazil Arif
#  @brief ?
#  @date ?
from date_adt import DateT
import pos_adt


def compare(description, expected, actual):
    print("Description: {description}".format(description=description))
    print("Expected: {expected}".format(expected=expected))  
    print("Actual:   {actual}".format(actual=actual))
    if(expected == actual): print('Result: ' + '\x1b[6;30;42m' + 'Passed' + '\x1b[0m')
    else: print('Result: ' + '\x1b[1;37;41m' + 'Failed' + '\x1b[0m')
    print("\n------------------------------------------------\n")

def main():
    #testing date_adt.py

    #2020 is a leap year!
    test = DateT(1,1,2020)

    #test constructor
    compare("test for constructor",test.d,1)
    compare("test for constructor",test.m,10)
    compare("test for constructor", test.y,2020)

    #test getter
    compare("testing getter method for day",test.day(),1)
    compare("testing getter method for month",test.month(),1)
    compare("testing getter method for year",test.year(),2020)

    #test next function
    #ideally for a functions like this the number of tests to run should be equal to or greater than the number of execution paths
    #there are 6 cases
    # i) simply the next day within current month and year
    # ii) Transition into The next month where the current month has 30 days
    # iii) Transition into The next month where the current month has 31 days
    # iv) Transition into The next year 
    # v) Transition into the next month when the current month is february and it a leap year
    # vi) Transition into the next month when current month is february and it is not a leap year

    compare("should return January 2nd 2020",test.next())


    
main()

    