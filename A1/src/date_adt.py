## @file date_adt.py
#  @author Shazil Arif
#  @brief date_adt.py contains a Class that implements a Date object containing a year, month and day
#  @date Jan 8th, 2020

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

  ## enum for the month with 28 days
  february = 28

  ## enum for the first month
  january = 1

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
    if(self.month in odd_month and self.day + 1 > max_odd_month and self.month != december):
      return DateT(1 , self.month + 1, self.year)

    #going into new month when current month has 30 days
    if(self.month in even_month and self.day + 1 > max_even_month):
      return DateT(1, self.month + 1, self.year)

    #going into the new year
    if(self.month in odd_month and self.day + 1 > max_odd_month and self.month == december):
      return DateT(1, 1, self.year + 1)

    #otherwise return the next day in the current month and year
    return DateT(self.day + 1, self.month, self.year)

  def prev(self):
    if(self.day - 1 < 1 and self.month != self.january):
      if(self.month - 1 in self.odd_month):
        return DateT(self.max_odd_month, self.month - 1, self.year)
      if(self.month - 1 in self.even_month):
        return DateT(self.max_even_month, self.month - 1, self.year)
    
    if(self.day - 1 < 1 and self.month == self.january):
      return DateT(self.max_odd_month, self.december, self.year - 1)

    return DateT(self.day - 1, self.month, self.year)



