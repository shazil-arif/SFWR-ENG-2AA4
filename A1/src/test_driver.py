## @file test_driver.py
#  @author ?
#  @brief ?
#  @date ?
import date_adt as Date
import pos_adt

obj = Date.DateT(1,2,2021)
p = obj.add_days(28)
print(p.day)
print(p.month)
print(p.year)

