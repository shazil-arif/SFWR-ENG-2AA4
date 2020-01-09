## @file pos_adt.py
#  @author Shazil Arif
#  @brief pos_adt.py implements a class for global position coordinates
#  @date January 9th, 2020

import math as Math
import date_adt as Date

class GPost:
    ## @brief the constructor method for class GPost
    #  @param phi The latitude to be set for the GPost object
    #  @param _lambda the longitude value to be set for the GPost object
    def __init__(self, phi, _lambda):
        self.lat = phi
        self.long = _lambda
        

    ## @brief returns the latitude for the current GPost object
    #  @return the latitude value
    def lat(self):
        return self.lat

    ## @brief returns the longitude for the current GPost object
    #  @return the longitude value
    def long(self):
        return self.long

    ## @brief returns whether the coordinates of the current GPost object are west of those in object p
    #  @param p the GPost object to compare
    #  @return a boolean value indicating whether the current objects coordinates are west of p (True if they are west of p, False otherwise) 
    def west_of(self,p):
        return self.long < p.long

    ## @brief returns whether the coordinates of the current GPost object are north of those in object p
    #  @param p the GPost object to compare
    #  @return a boolean value indicating whether the current objects coordinates are north of coordinates in p (True if they are west of p, False otherwise) 
    def north_of(self,p):
        return self.lat > p.lat
    
    def equal(self,p):
        return self.distance(p) < 1

    def move(self,b,d):
        radius = 6371

        phi_one = Math.radians(self.lat)
        angular_dist = d/radius #row/sigma lookking

        new_lat = Math.asin(Math.sin(phi_one) * Math.cos(angular_dist) + Math.cos(phi_one)*Math.sin(angular_dist)*Math.cos(b) )
        new_long = self.long + Math.atan2(Math.sin(b)*Math.sin(angular_dist)*Math.cos(phi_one), (Math.cos(angular_dist) - Math.sin(phi_one)) * Math.sin(new_lat) )

        self.lat = new_lat
        self.long = new_long

    def distance(self,p):
        #earth's approximate radius in kilometres
        radius = 6371

        lat_one = Math.radians(self.lat)
        lat_two = Math.radians(p.lat)

        long_diff = Math.radians(p.long - self.long)

        distance = Math.acos(Math.sin(lat_one)*Math.sin(lat_two) + Math.cos(lat_one)*Math.cos(lat_two*Math.cos(long_diff))) * radius

        return distance
    
    def arrival_date(self,p,d,s):
        distance = self.distance(p)

        #number of days required to cover the distance travelling at speed s
        num_days = distance/s 

        return d.add_days(num_days)

        

    

