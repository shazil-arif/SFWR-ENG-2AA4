## @file pos_adt.py
#  @author Shazil Arif
#  @brief pos_adt.py implements a class for global position coordinates
#  @date January 18th, 2020

import math as Math
import date_adt as Date
## @brief GPosT is class that implements an object to represent coordinates using longitude and latitude values
class GPosT:
    ## @brief the constructor method for class GPost
    #  @param phi The latitude to be set for the GPost object
    #  @param _lambda the longitude value to be set for the GPost object
    def __init__(self, phi, _lambda):
        self.latitude = phi
        self.longitude = _lambda
        
    ## @brief returns the latitude for the current GPost object
    #  @return the latitude value
    def lat(self):
        return self.latitude

    ## @brief returns the longitude for the current GPost object
    #  @return the longitude value
    def long(self):
        return self.longitude

    ## @brief returns whether the coordinates of the current GPost object are west of those in object p
    #  @param p the GPost object to compare
    #  @return a boolean value indicating whether the current objects coordinates are west of p (True if they are west of p, False otherwise) 
    def west_of(self,p):
        return self.long() < p.long()

    ## @brief returns whether the coordinates of the current GPost object are north of those in object p
    #  @param p the GPost object to compare
    #  @return a boolean value indicating whether the current objects coordinates are north of coordinates in p (True if they are west of p, False otherwise) 
    def north_of(self,p):
        return self.lat() > p.lat()
    
    ## @brief returns whether the current GPost object and a GPost object p represent the same position
    #  @details considered to represent the same location if the distance between their coordinates is less than 1 km
    #  @param p the GPost object to compare againt
    #  @return a boolean value indicating whether the two objects represent same location(i.e if their distance is less than 1km). True if same location, False otherwise
    def equal(self,p):
        return self.distance(p) < 1

    ## @brief moves the position represented by the current GPost object in direction of bearing b with total distance d
    #  @param b A real number indicating the bearing/direction to move in
    #  @param d A real number indicating the distance to move in units of kilometres (km)
    def move(self,b,d):
        radius = 6371

        phi_one = Math.radians(self.lat())
        angular_dist = d/radius 

        new_lat = Math.asin(Math.sin(phi_one) * Math.cos(angular_dist) + Math.cos(phi_one)*Math.sin(angular_dist)*Math.cos(Math.radians(b)) )
        new_long = self.long() + Math.degrees(Math.atan2(Math.sin(Math.radians(b))*Math.sin(angular_dist)*Math.cos(phi_one), Math.cos(angular_dist) - Math.sin(phi_one) * Math.sin(new_lat) ))

        self.latitude = round(Math.degrees(new_lat),2)
        self.longitude = round(new_long,2)

    ## @brief calculates the distance between the positions represented by current GPost object and another GPost object 'p'. Calculates to 2 decimal places
    #  details Applies the spherical law of cosines formula to calculate the distance. See https://www.movable-type.co.uk/scripts/latlong.html under the heading 'Spherical Law of Cosines'
    #  @param p A GPost object containing the lat/long coordinates to calculate the distance to
    #  @return an integer value representing the distance between the current object and p in units of kilometres(km)
    def distance(self,p):
        #earth's approximate radius in kilometres
        radius = 6371

        lat_one = Math.radians(self.lat())
        lat_two = Math.radians(p.lat())

        long_diff = Math.radians(p.long() - self.long())

        distance = Math.acos(Math.sin(lat_one)*Math.sin(lat_two) + Math.cos(lat_one)*Math.cos(lat_two)*Math.cos(long_diff)) * radius

        return round(distance,2)
    
    ## @brief calculates the number of days required to travel from the position represented by current GPost object to another position represented by a GPost object while travelling at a specific speed and starting on a specific day
    #  @details please note that the speed parameter will be rounded to two decimal places to keep it consistent with distance values. If the speed is 0 the current DateT object will be returned
    #  @param p A GPost object representing the position to travel to
    #  @param d a DateT object respresenting the date to begin travelling on 
    #  @param s A real number indicating the speed to travel at in units of km/day
    #  @return an integer value representing the distance between the current object and p in units of kilometres(km)
    def arrival_date(self,p,d,s):
        distance = self.distance(p)

        #number of days required to cover the distance travelling at speed s
        num_days = 0
        if(s!=0): num_days = Math.floor(distance/round(s,2))
        
        return d.add_days(num_days)

        

    

