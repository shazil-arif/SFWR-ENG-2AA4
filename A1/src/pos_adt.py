## @file pos_adt.py
#  @author Shazil Arif
#  @brief pos_adt.py implements a class for global position coordinates
#  @date January 9th, 2020

class GPost:
    ## @brief the constructor method for class GPost
    #  @param phi The latitude to be set for the GPost object
    #  @param _lambda the longitude value to be set for the GPost object
    def __init__(self, phi, _lambda):
        self.lat = phi
        self.long = _lambda

    def lat(self):
        return self.lat
    def long(self):
        return self.long
