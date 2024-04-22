
from enum import Enum

class District(Enum):
    BURNABYHEIGHTS = 1
    CAPITOLHILL = 2
    WESTRIDGE = 3
    BRENTWOOD = 4
    WILLINGDONHEIGHTS = 5
    LOCHDALE = 6
    MENTECITO = 7
    BURQUITLAM = 8
    AUSTINHEIGHTS = 9
    MAILLARDVILLE = 10
    LAURENTIANBELAIRE = 11
    #Bucket enums to catch all other classifications
    GENERALSOUTHBURNABY = 12 #SOUTH
    COQUITLAM = 13 #WEST
    METROVANCOUVER = 14 #EAST


class Property:

    # cost per person
    # number of available rooms
    # location enums
    def __init__(self, cost, rooms, url, location=District.GENERALSOUTHBURNABY):
        self.cost = cost
        self.rooms = rooms
        self.url = url
        self.location = location
    
    def setLocation(self, latitude, longitude):
        self.location = Location(latitude, longitude)
        
    def __str__(self):
        return "Rooms: {}, Cost: {}, Location: {}, Link: {}".format(self.rooms, self.cost, self.location, self.url)

class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

