from knowledge_base import *

#tests
engine = DishwasherStopsWorking()
engine.reset()
print("\nThe dishwasher doesn't fill with water:")
engine.declare(Problem(description="The dishwasher doesn't fill with water"))
engine.run()

engine.reset()
print("\nthe drain pump operates continuously:")
engine.declare(Problem(description="the drain pump operates continuously"))
engine.run()

engine.reset()
print("\nDisplay shows number 20:")
engine.declare(Display(number=20))
engine.run()

engine = ResultsNotSatisfactory()
engine.reset()
print("\nThe dishes are not clean")
engine.declare(Problem(description="The dishes are not clean"))
engine.run()


engine.reset()
print("\nThe dishes are wet and dull")
engine.declare(Problem(description="The dishes are wet and dull"))
engine.run()