from random import choice
from experta import *


class Display(Fact):
    """Info about the dishwasher's display."""
    pass


class Problem(Fact):
    """Info about the dishwasher's problem"""
    pass


class DishwasherStopsWorking(KnowledgeEngine):
    @Rule(Display(number=L(10) | L('10'))
          | Problem(description="The dishwasher doesn't fill with water"))
    def no_water(self):
        if input("Is the water tap blocked or furred with limescale? \nyes/no: ") == "yes":
            print("Clean the water tap.")
        if input("Is the water tap is closed? \nyes/no: ") == "yes":
            print("Open the water tap.")
        if input("Is the filter in the water inlet hose blocked? \nyes/no: ") == "yes":
            print("Clean the filter.")
        if input("Is the connection of the water inlet hose not correct? \nyes/no: ") == "yes":
            print("The hose can be kinked or squashed. Make sure that the connection is correct")
        else:
            print("Try to reset the dishwasher. If the problem persists contact Support")

    @Rule(Display(number=L(20) | L('20'))
          | Problem(description="The dishwasher will not drain"))
    def no_drain(self):
        if input("Is There a blockage in the sink spigot? \nyes/no: ") == "yes":
            print("Clean the sink spigot.")
        if input("Is the connection of the water drain hose not correct? \nyes/no: ") == "yes":
            print("The hose can be kinked or squashed. Make sure that the connection is correct")
        else:
            print("Try to reset the dishwasher. If the problem persists contact Support")

    @Rule(Problem(description=L("the drain pump operates continuously")
                              | L("all indicators lights on the control panel go off")))
    def anti_flood_device_operates(self):
        print("Close the water tap and contact your local Service Force Centre.")

    @Rule(Problem(description="The programme does not start"))
    def programme_not_starting(self):
        if input("Is the appliance door not closed? \nyes/no: ") == "yes":
            print("Close the door.")
        if input("Is mains plug not connected in? \nyes/no: ") == "yes":
            print("Put in the mains")
        if input("Has the fuse blown out in the household fuse box? \nyes/no: ") == "yes":
            print("Replace the fuse.")
        if input("Is delay start set? \nyes/no: ") == "yes":
            print("Cancel the delay start to start the programme immediately.")
        else:
            print("Try to reset the dishwasher (press on/off button). If the problem persists contact Support\n")




class ResultsNotSatisfactory(KnowledgeEngine):

    @Rule(Problem(description="The dishes are not clean"))
    def dishes_not_clean(self):
        print("Possible causes:\n"
              "-The selected washing programme is not applicable for the type of load and soil.\n"
              "-The basket is loaded incorrectly so that water cannot reach all surfaces.\n"
              "-Spray arm does not turn freely because of incorrect arrangement of the load.\n"
              "-The filters are dirty or not correctly installed.\n"
              "-The quantity of detergent is too little or missing.\n")

    @Rule(Problem(description="Limescale particles on the dishes"))
    def limescale_on_dishes(self):
        print("Possible causes:\n"
              "-The salt container is empty.\n"
              "-The water softener is adjusted on a wrong level.\n"
              "-The salt container cap is not closed correctly.\n")

    @Rule(Problem(description="The dishes are wet and dull"))
    def dishes_wet_or_dull(self):
        print("Possible causes:\n"
              "-No rinse aid has been used.\n"
              "-The rinse aid dispenser is empty.\n")

    @Rule(Problem(description="There are streaks, milky spots or a bluish coating on glasses and dishes"))
    def spots_on_dishes(self):
        print("Possible cause:\n"
              "-Decrease the rinse aid dosage.\n")
