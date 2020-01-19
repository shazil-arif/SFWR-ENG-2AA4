## @file test_driver.py
#  @author Shazil Arif
#  @brief this test driver module is used to test modules DateT and GPost
#  @date January 10th, 2020
from date_adt import DateT
from pos_adt import GPosT
import time

failed = []
count = 0

def compare(description, expected, actual):
    print("Description: {description}\n".format(description=description))
    global count
    count = count + 1

    #if expected value is instance of DateT or GPost class
    if(isinstance(expected,DateT) or isinstance(expected,GPosT)): 
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
            failed.append({"Description":description,
            "Expected":expected,
            "Actual":actual})
            print('\nResult: ' + '\x1b[1;37;41m' + 'Failed' + '\x1b[0m')

    else: #comparing other types...string, int, float etc.
        print("Expected: {expected}".format(expected=expected))  
        print("Actual:   {actual}".format(actual=actual))
        if(expected == actual): print('\nResult: ' + '\x1b[6;30;42m' + 'Passed' + '\x1b[0m')
        else: 
            failed.append({"Description":description,"Expected":expected,"Actual":actual})
            print('\nResult: ' + '\x1b[1;37;41m' + 'Failed' + '\x1b[0m')
    print("\n------------------------------------------------\n")

def test_date_adt():
    #testing date_adt.py

    #2020 is a leap year!
    start = time.time()
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

    compare("testing next method, it should return January 2nd 2020 and pass",DateT(2,1,2020),test.next())

    test = DateT(31,1,2020)
    compare("test for transitioning into next month with current month having 31 days. It should return february 1st 2020 and pass",DateT(1,2,2020), test.next())

    test = DateT(30,4,2020) #April 30th, 2020
    compare("test for transitioning into next month with current month having 30 days. It should return May 1st 2020 and pass",DateT(1,5,2020),test.next())

    test = DateT(28,2,2020) 
    compare("test for transitioning into next month with current month being february and the year is a leap year. It should return Feb 29th 2020 and pass",DateT(29,2,2020),test.next())

    test = DateT(28,2,2021) 
    compare("test for transitioning into next month with current month being february and the year is NOT leap year. It should return March 1st 2021 and pass",DateT(1,3,2021),test.next())

    test = DateT(31,12,2020) 
    compare("test for transitioning into next year. It should return Jan 1st 2021 and pass",DateT(1,1,2021),test.next())

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

def test_post_adt():
    test = GPosT(45,45)
    compare("test for constructor",45, test.latitude)
    compare("test for constructor",45, test.longitude)
    compare("test getter method for latitude",45,test.lat())
    compare("test getter method for longitude",45,test.long())

    test = GPosT(43.580605, -79.625668)
    test2 = GPosT(40.723606, -73.860514)
    compare("test distance method , it should return 571.44 km rounded to the 2 decimal places",571.44,test2.distance(test))

    test = GPosT(43.261897, -79.921433)
    test2 = GPosT(43.262545, -79.922549)
    compare("test equal method for distance < 1 km, it should return True",True, test2.equal(test))

    test2 = GPosT(43.250880, -79.920292)
    compare("test equal method for distance > 1km, it should return False",False,test2.equal(test)) 

    test = GPosT(45,45)
    test2 = GPosT(45,-45)
    compare("test west_of method , it should return True",True,test2.west_of(test))

    compare("test west_of method, it should return False",False,test.west_of(test2))

    test = GPosT(45,45)
    test2 = GPosT(50,-45)
    compare("test north_of method, it should return True",True,test2.north_of(test))
    compare("test north_of method, it should return False",False,test.north_of(test2))

    test = GPosT(43,-75)
    test2 = GPosT(44.078061, -73.170068)

    test.move(45,100)
    compare("test move method",GPosT(43.63, -74.12),test)

    date = DateT(18,1,2020)
    test = GPosT(43,-75)
    val = test.arrival_date(test2,date,180) #starting from 43,-75 travel to test2 at 190.1km/day starting on date
    compare("test arrival date while travelling at speed that allowed to reach within the same (i.e days required < 1), it should return Jan 19th, 2020",DateT(19,1,2020),val)

    test_distance = test.distance(test2)
    val = test.arrival_date(test2,date,test_distance)
    compare("test arrival date with travelling speed that takes exactly 1 day in total, it should return Jan 19th 2020",DateT(19,1,2020),val)

    val = test.arrival_date(test2,date,14.62)
    compare("test arrival date with travelling speed that takes until the 31st of the month, it should return Jan 31st 2020",DateT(31,1,2020),val)

    date = DateT(1,2,2020)
    val = test.arrival_date(test2,date,6.55)
    compare("test arrival date that takes 29 days to travel in feb, it should return March 1st 2020",DateT(1,3,2020),val)

    val = test.arrival_date(test2,date,0)
    compare("test arrival date with 0 speed it should return the current date",DateT(1,2,2020),val)


def main():
    start = time.time()
    print("Tests for date_adt.py")
    test_date_adt()

    print("\nTESTS FOR pos_adt.py")
    test_post_adt()
    end = time.time()
    end = round(end - start,5)

    if(len(failed)!=0): 
        print("\x1b[1;37;41m {num} tests failed\n Tests highlighted above in red failed. The following tests failed: \x1b[0m \n".format(num=len(failed)))
        for i in range(len(failed)):
            print("{num}) Description: {Description}".format(num=(i+1),Description=failed[i]["Description"]))
    else: print("\x1b[6;30;42m All tests passed. Executed {count} tests in {time} seconds \x1b[0m.".format(count=count,time=end))

main()
    
