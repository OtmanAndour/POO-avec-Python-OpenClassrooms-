class Agent:
    #This is how to define a method on a class
    def say_hello(self,first_name):
        return "Howdy "+first_name+" :D"
    #This is how to define an attribute on a class
    def __init__(self,agreeableness):
        self.agreeableness = agreeableness


agent=Agent(2)
print(agent.agreeableness)
