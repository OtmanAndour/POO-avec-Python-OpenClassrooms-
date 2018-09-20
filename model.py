import json

class Agent:
    #This is how to define a method on a class
    def say_hello(self,first_name):
        return "Howdy "+first_name+" :D"
    #This is how to define an attribute on a class
    def __init__(self,**agent_attributes):
        for attr_name, attr_value in agent_attributes.items():
            setattr(self,attr_name,attr_value)

def main ():
    for agent_attributes in json.load(open("agents-100k.json")): #Open the json file and load it
        agent = Agent(**agent_attributes)
        print(agent.country_name)

main()