## @file date_adt.py
#  @author Shazil Arif
#  @brief date_adt.py contains a Class that implements a Date object containing a year, month and day
#  @date Jan 8th, 2020

from datetime import datetime
from datetime import timedelta

## @brief DateT is a class that implements a Date object containing a year, month and a day
class DateT:

  ## Represents the months with 31 days
  odd_month = [1,3,5,7,8,10,12]

  ## enum for representing the maximum number of days in the months contained in odd_month
  max_odd_month = 31

  ## Represents months with 30 days
  even_month = [4,6,9,11]

  ## enum for representing the maximum number of days in the months contained in even_month
  max_even_month = 30
  
  ## enum for the 12 month
  december = 12

  ## enum for the month of february
  february = 2

  ## enum for the first month
  january = 1

  ## enum for number of days in a leap year in the month of february
  leap_year_days = 29

  ## enum for number of days in february in a common year (not a leap year)
  feb_common_days = 28

  ## @brief the constructor method for class DateT
  #  @param d The date to be set 
  #  @param m the Month to be set
  #  @param y the Year to be set
  def __init__(self, d, m, y):
    self.day = d
    self.month = m
    self.year = y

  ## @brief returns the day
  #  @return the day
  def day(self):
    return self.day

  ## @brief returns the month
  #  @return the month
  def month(self):
    return self.month

  ## @brief returns the year
  #  @return the year
  def year(self):
    return self.month

  ## @brief returns a DateT object that is 1 day later than the current object
  #  @return DateT object that is set 1 day later
  def next(self):
    #going into new month when current month has 31 days
    if(self.month in self.odd_month and self.day + 1 > self.max_odd_month and self.month != self.december):
      return DateT(1 , self.month + 1, self.year)

    #going into new month when current month has 30 days
    if(self.month in self.even_month and self.day + 1 > self.max_even_month):
      return DateT(1, self.month + 1, self.year)

    #going into the new year
    if(self.day + 1 > self.max_odd_month and self.month == self.december):
      return DateT(1, 1, self.year + 1)

    # if current month is february
    if(self.month == self.february):
      #leap year and transitioning into march
      if(self.is_leap_year() and self.day + 1 > self.leap_year_days):
        return DateT(1, self.month + 1, self.year )

      #not a leap year but transitioning into march  
      elif(not self.is_leap_year() and self.day + 1 > self.feb_common_days):
        return DateT(1, self.month + 1, self.year)

    #otherwise return the next day in the current month and year
    return DateT(self.day + 1, self.month, self.year)

  ## @brief returns a DateT object that is 1 day before the current object
  #  @return DateT object that is set 1 day before
  def prev(self):
    #in the case where we go back to the previous month
    if(self.day - 1 < 1 and self.month != self.january):

      #if previous month is not february
      if(self.month - 1 != self.february):
        #check if previous month has 31 days
        if(self.month - 1 in self.odd_month):
          return DateT(self.max_odd_month, self.month - 1, self.year)

        #previous month has 30 days
        if(self.month - 1 in self.even_month):
          return DateT(self.max_even_month, self.month - 1, self.year)

      #in the case where previous month is february
      #first check if leap year or not
      if(self.is_leap_year()):
        return DateT(self.leap_year_days,self.february,self.year)
      return DateT(self.feb_common_days, self.february, self.year)
      

    #in the case we have to go back to the previous year
    if(self.day - 1 < 1 and self.month == self.january):
      return DateT(self.max_odd_month, self.december, self.year - 1)

    #the simplest case, where there is no month or year transition
    return DateT(self.day - 1, self.month, self.year)


  ## @brief compares if the date represented by the current DateT object is before d (d is also a DateT object)
  #  @param d The DateT object to compare with the current object
  #  @return A boolean value indicating whether the current objects date is before the date in d (True if before, False otherwise)
  def before(self,d):
    if(self.year < d.year): return True
    if(self.year == d.year and self.month < d.month): return True
    if(self.year == d.year and self.month == d.month and self.day < d.day): return True
    return False

  ## @brief compares if the date represented by the current DateT object is after d (d is also a DateT object)
  #  @param d The DateT object to compare with the current object
  #  @return A boolean value indicating whether the current objects date is after the date in d (True if before, False otherwise)
  def after(self,d):
    if (not self.before(d)): return True
    return False

  ## @brief compares if the current DateT object and another DateT object d represent the same date
  #  @param d The DateT object to compare with the current object
  #  @return A boolean value indicating whether the two objects represent the same data (True if equal, False otherwise)
  def equal(self,d):
    return (self.year == d.year and self.month == d.month and self.day == d.day)

  ## @brief adds n days to the date represented by the current DateT object
  #  @param n The number of days to add
  #  @return A DateT object with its date set n days later than the original
  def add_days(self,n):
    temp = datetime(self.year, self.month, self.day)
    temp = temp + timedelta(days=n)
    return DateT(temp.day,temp.month,temp.year)
    
  ## @brief calculates the number of days between the current DateT object and DateT object d
  #  @param d The DateT object to calculate the number of days in between with
  #  @return An integer value indicating the number of days between the two DateT objects
  def days_between(self,d):
    date_one = datetime(self.year, self.month, self.day)
    date_two = datetime(d.year,d.month,d.day)
    difference = date_one - date_two
    return difference
    
  ## @brief returns whether or not the year in the current DateT object is a leap year
  #  @return a boolean value indicating whether or not the year is a leap year (True if leap year, False otherwise)
  def is_leap_year(self):
    if(self.year % 400 == 0): return True
    if(self.year % 100 == 0): return False
    if(self.year % 4 == 0): return True
    return False

      






