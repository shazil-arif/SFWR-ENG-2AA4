## @file test_driver.py
#  @author Shazil Arif
#  @brief this test driver module is used to test modules DateT and GPost
#  @date January 10th, 2020
from date_adt import DateT
from pos_adt import GPost

failed = []

def compare(description, expected, actual):
    print("Description: {description}\n".format(description=description))

    #if expected value is instance of DateT or GPost class
    if(isinstance(expected,DateT) or isinstance(expected,GPost)): 
        expected_keys = expected.__dict__
        actual_keys = actual.__dict__
        print("Expected properties")
        for i in expected_keys:
            print("{key} : {value}".format(key=i,value=expected_keys[i]))  
        print("\nActual properties")
        for i in actual_keys:        
            print("{key} : {value}".format(key=i,value=actual_keys[i]))  
        if(expected.__dict__ == actual.__dict__):
            print('\nResult: ' + '\x1b[6;30;42m' + 'Passed' + '\x1b[0m') #source: https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
        else:
            failed.append({"Description":description,"Expected":expected,"Actual":actual})
            print('\nResult: ' + '\x1b[1;37;41m' + 'Failed' + '\x1b[0m')

    else: #comparing other types...string, int, float etc.
        print("Expected: {expected}".format(expected=expected))  
        print("Actual:   {actual}".format(actual=actual))
        if(expected == actual): print('\nResult: ' + '\x1b[6;30;42m' + 'Passed' + '\x1b[0m')
        else: 
            failed.append({"Description":description,"Expected":expected,"Actual":actual})
            print('\nResult: ' + '\x1b[1;37;41m' + 'Failed' + '\x1b[0m')
    print("\n------------------------------------------------\n")

def test_adt():
    #testing date_adt.py


    #2020 is a leap year!
    test = DateT(1,1,2020)

    #test constructor
    compare("test for constructor",1,test.d)
    compare("test for constructor",1,test.m)
    compare("test for constructor",2020,test.y)

    #test getter
    compare("testing getter method for day",1, test.day())
    compare("testing getter method for month",1, test.month())
    compare("testing getter method for year",2020, test.year())


    #test next function
    #ideally for a functions like this the number of tests to run should be equal to or greater than the number of execution paths
    #there are 6 cases
    # i) simply the next day within current month and year
    # ii) Transition into The next month where the current month has 30 days
    # iii) Transition into The next month where the current month has 31 days
    # iv) Transition into The next year 
    # v) Transition into the next month when the current month is february and it a leap year
    # vi) Transition into the next month when current month is february and it is not a leap year

    compare("testing next method, it should return January 2nd 2020 and pass",test.next(),DateT(2,1,2020))

    test = DateT(31,1,2020)
    compare("test for transitioning into next month with current month having 31 days. It should return february 1st 2020 and pass",test.next(),DateT(1,2,2020))

    test = DateT(30,4,2020) #April 30th, 2020
    compare("test for transitioning into next month with current month having 30 days. It should return May 1st 2020 and pass",test.next(),DateT(1,5,2020))

    test = DateT(28,2,2020) 
    compare("test for transitioning into next month with current month being february and the year is a leap year. It should return Feb 29th 2020 and pass",test.next(),DateT(29,2,2020))

    test = DateT(28,2,2021) 
    compare("test for transitioning into next month with current month being february and the year is NOT leap year. It should return March 1st 2021 and pass",test.next(),DateT(1,3,2021))

    test = DateT(31,12,2020) 
    compare("test for transitioning into next year. It should return Jan 1st 2021 and pass",test.next(),DateT(1,1,2021))

    #test prev method
    test=DateT(2,1,2020)
    compare("test for prev method, it should return January 1st 2020 and pass",DateT(1,1,2020),test.prev())

    test=DateT(1,5,2020)
    compare("test for transitioning into previous month with current month having 31 days. It should return April 30th 2020 and pass",DateT(30,4,2020),test.prev())

    test=DateT(1,6,2020)
    compare("test for transitioning into previous month with current month having 30 days. It should return May 31st 2020 and pass",DateT(31,5,2020),test.prev())

    test=DateT(1,3,2020)
    compare("test for transitioning back into february and the year is a leap year. It should return Feb 29th 2020 and pass",DateT(29,2,2020),test.prev())
    
    test=DateT(1,3,2021)
    compare("test for transitioning back into february and the year is NOT leap year. It should return Feb 28th 2021 and pass",DateT(28,2,2021),test.prev())
    
    test=DateT(1,1,2020)
    compare("test for transitioning into previous year. It should return Dec 31st 2019 and pass",DateT(31,12,2019),test.prev())

    #test for before method
    test  = DateT(1,1,2020)
    test2 = DateT(1,5,2020)

    compare("test for before method , it should return True and pass",True,test.before(test2))

    compare("test for before method , it should return False and pass",False,test2.before(test))

    #test for after method
    compare("test for after method , it should return True and pass",True,test2.after(test))

    compare("test for after method , it should return False and pass",False,test.after(test2))

    #test equals method
    test = DateT(1,1,2020)
    test2 = DateT(1,1,2020)
    test3 = DateT(1,2,2020)
    compare("test for equals method, it should return True and pass",True,test.equal(test2))

    compare("test for equals method, it should return False and pass",False,test.equal(test3))

    #test add_days method
    test = DateT(31,1,2020)
    compare("test add days method, it should return Feb 1st 2020 and pass",DateT(1,2,2020),test.add_days(1))

    compare("test add days method, it should return Feb 29, 2020", DateT(29,2,2020),test.add_days(29))

    test = DateT(31,1,2021)
    compare("test add days method, it should return March 1st, 2021", DateT(1,3,2021),test.add_days(29))

    test = DateT(1,1,2021)
    compare("test add days method, add 365 days when current year is NOT leap year, it should return january 1st 2022",DateT(1,1,2022),test.add_days(365))

    test = DateT(1,1,2020)
    compare("test add days method, add 365 days when current year IS LEAP YEAR. it should return Dec 31st, 2020",DateT(31,12,2020),test.add_days(365))

    test = DateT(1,1,2020)
    compare("test add days method, add 366 days when current year IS LEAP YEAR. it should return Jan 1st, 2021",DateT(1,1,2021),test.add_days(366))


    #test days_between method
    test = DateT(31,1,2020)
    test2 = DateT(1,3,2020)

    compare("test days_between method with March and January when current year is leap year, it should return 30 days",30,test2.days_between(test))

    test = DateT(31,1,2021)
    test2 = DateT(1,3,2021)
    compare("test days_between method with March and January when current year is NOT leap year, it should return 29 days",29,test2.days_between(test))

    


    if(len(failed)!=0): print("\x1b[1;37;41m {num} tests failed \x1b[0m \n".format(num=len(failed)))
    else: print("\x1b[6;30;42m All tests passed \x1b[0m")
    # for test in failed:
    #     for i in test:
    #         if(isinstance(test[i],DateT) or isinstance(test[i],GPost)):
    #             expected_keys = test["Expected"].__dict__
    #             actual_keys = test["Actual"].__dict__
    #             print("Expected properties")
    #             for i in expected_keys:
    #                 print("{key} : {value}".format(key=i,value=expected_keys[i]))  
    #             print("\nActual properties")
    #             for i in actual_keys:        
    #                 print("{key} : {value}".format(key=i,value=actual_keys[i])) 
    #             break
    #         else:    
    #             print("{key} : {value}".format(key=i,value=test[i]))
    #     print("\n")

    
test_adt()

    