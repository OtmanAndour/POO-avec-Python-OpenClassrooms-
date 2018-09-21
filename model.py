import json
import math
import matplotlib.pyplot as plt

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
    EARTH_RADIUS_KILOMETERS=6371

    #Creates an instance of a zone
    def __init__(self,corner1,corner2):
        self.corner1=corner1
        self.corner2=corner2
        self.inhabitants=[] #No inhabitants when created

    #This adds an inhabitant in an instance of a zone
    def add_inhabitant(self,inhabitant):
        self.inhabitants.append(inhabitant)

    #This method gives the population of an instance of a zone, as a property of the instance we're working with
    @property
    def population(self):
        return len(self.inhabitants)

    @property
    def width(self):
        return abs(self.corner1.longitude - self.corner2.longitude) * self.EARTH_RADIUS_KILOMETERS

    @property
    def height(self):
        return abs(self.corner1.latitude - self.corner2.latitude) * self.EARTH_RADIUS_KILOMETERS

    @property
    def area(self):
        return self.width * self.height

    @classmethod #This allows us to create a method for the class Zone, not just for an instance of the class Zone. We then need to replace all the self by cls
    def _initialize_zones(cls): #We use an underscore to make this method protected, because we don't want to initialize the zones in the main, but rather in this method as it's avgt to do
        for latitude in range(cls.MIN_LATITUDE_DEGREES,cls.MAX_LATITUDE_DEGREES,cls.HEIGHT_DEGREES):
            for longitude in range(cls.MIN_LONGITUDE_DEGREES,cls.MAX_LONGITUDE_DEGREES,cls.WIDTH_DEGREES):
                bottom_left_corner=Position(longitude,latitude)
                top_right_corner=Position(longitude+cls.WIDTH_DEGREES,latitude+cls.HEIGHT_DEGREES)       
                zone=Zone(bottom_left_corner,top_right_corner)
                cls.ZONES.append(zone)
        

    def contains(self, position):
        return position.longitude >= min(self.corner1.longitude, self.corner2.longitude) and \
            position.longitude < max(self.corner1.longitude, self.corner2.longitude) and \
            position.latitude >= min(self.corner1.latitude, self.corner2.latitude) and \
            position.latitude < max(self.corner1.latitude, self.corner2.latitude)
            
    @classmethod
    def find_zone_that_contains(cls, position):
        # Compute the index in the ZONES array that contains the given position
        if not cls.ZONES: # We need to check if there are zones created or not
            cls._initialize_zones() # If not, we create them
        longitude_index = int((position.longitude_degrees - cls.MIN_LONGITUDE_DEGREES)/ cls.WIDTH_DEGREES)
        latitude_index = int((position.latitude_degrees - cls.MIN_LATITUDE_DEGREES)/ cls.HEIGHT_DEGREES)
        longitude_bins = int((cls.MAX_LONGITUDE_DEGREES - cls.MIN_LONGITUDE_DEGREES) / cls.WIDTH_DEGREES) # 180-(-180) / 1
        zone_index = latitude_index * longitude_bins + longitude_index

        # Just checking that the index is correct
        zone = cls.ZONES[zone_index]
        assert zone.contains(position)

        return zone

    @property
    def avg_agreeableness(self):
        if not self.inhabitants:
            return 0
     #   sum_agreeableness=0
     #   for inhabitant in self.inhabitants :
     #       sum_agreeableness += inhabitant.agreeableness
     #   return sum_agreeableness/self.population
    #We can calculate the avg_agreeableness this way, or we can be smarter and faster :

        return sum([inhabitant.agreeableness for inhabitant in self.inhabitants])/self.population

class BaseGraph:

    def __init__(self):
        self.title="Your graph title"
        self.x_label="X_axis label"
        self.y_label="Y_axis label"
        self.show_grid=True

    def show(self,zones):
        plt.plot(x_values,y_values,'.')
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.title(self.title)
        plt.grid(self.show_grid)
        plt.show()

class AgreeablenessGraph(BaseGraph): #This class is a sub-class of the BaseGraph class so that we can call the BaseGraph class but use our own attributes

    def __init__(self):
        super().__init__() #This call the main class init method, so that we kepp show_grid to True but still change the other values
        self.title="Nice people live in the countryside"
        self.x_label="population density"
        self.y_label="Agreeableness"

    

def main ():
    for agent_attributes in json.load(open("agents-100k.json")): #Open the json file and load it
        latitude=agent_attributes.pop('latitude')
        longitude=agent_attributes.pop('longitude')
        #Pop is used to fetch the agents positions and remove them from the dic since we won't use them anymore
        position=Position(longitude,latitude)
        #We then create an instance of the agent's position
        #Now we need to update the Agent class so that is gives a position to each agent created
        agent = Agent(position,**agent_attributes)
        zone=Zone.find_zone_that_contains(position)
        zone.add_inhabitant(agent)
        print(zone.avg_agreeableness)

        #Graph init
        #agreeableness_graph=AgreeablenessGraph()
        #Graph show
        #agreeableness_graph.show(Zone.ZONES)
main()