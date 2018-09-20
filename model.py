import json
import math

class Agent:
    #This is how to define a method on a class
    def say_hello(self,first_name):
        return "Howdy "+first_name+" :D"
    #This is how to define an attribute on a class
    def __init__(self,position,**agent_attributes):  #We added position in the parameters so that each agent created has a position defined
        self.position=position
        for attr_name, attr_value in agent_attributes.items():
            setattr(self,attr_name,attr_value)

class Position:

    def __init__(self,longitude_degrees,latitude_degrees):
        self.latitude_degrees=latitude_degrees
        self.longitude_degrees=longitude_degrees

    @property #By doing so, the longitude method is turned into a porperty and can be called without using () afer longitude E.g : print(agent.position.longitude)
    def longitude(self): #This method will convert the longitude in rad
        return self.longitude_degrees * (math.pi/180)

    @property
    def latitude(self):
        return self.latitude_degrees * (math.pi/180)

class Zone:

    ZONES=[]
    MIN_LONGITUDE_DEGREES=-180
    MAX_LONGITUDE_DEGREES=180
    MIN_LATITUDE_DEGREES=-90
    MAX_LATITUDE_DEGREES=90
    HEIGHT_DEGREES=1
    WIDTH_DEGREES=1

    def __init__(self,corner1,corner2):
        self.corner1=corner1
        self.corner2=corner2
        self.inhabitants=0

    @classmethod #This allows us to create an instance of the Zone class inside of the Zone class. We then need to replace all the self by cls
    def initialize_zones(cls):
        for latitude in range(cls.MIN_LATITUDE_DEGREES,cls.MAX_LATITUDE_DEGREES,cls.HEIGHT_DEGREES):
            for longitude in range(cls.MIN_LONGITUDE_DEGREES,cls.MAX_LONGITUDE_DEGREES,cls.WIDTH_DEGREES):
                bottom_left_corner=Position(longitude,latitude)
                top_right_corner=Position(longitude+cls.WIDTH_DEGREES,latitude+cls.HEIGHT_DEGREES)       
                zone=Zone(bottom_left_corner,top_right_corner)
                cls.ZONES.append(zone)
        print (len(cls.ZONES))

def main ():
    for agent_attributes in json.load(open("agents-100k.json")): #Open the json file and load it
        latitude=agent_attributes.pop('latitude')
        longitude=agent_attributes.pop('longitude')
        #Pop is used to fetch the agents positions and remove them from the dic since we won't use them anymore
        position=Position(longitude,latitude)
        #We then create an instance of the agent's position
        #Now we need to update the Agent class so that is gives a position to each agent created
        agent = Agent(position,**agent_attributes)
        Zone.initialize_zones()
main()