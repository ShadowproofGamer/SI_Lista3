from random import choice
from knowledge_base import *


def main():
    # Print all possible problems with numbering
    problems = {
        1: "The dishwasher doesn't fill with water",
        2: "The dishwasher will not drain",
        3: "The programme does not start",
        4: "The dishes are not clean",
        5: "Limescale particles on the dishes",
        6: "The dishes are wet and dull",
        7: "There are streaks, milky spots or a bluish coating on glasses and dishes"
    }

    print("List of Possible Problems:")
    for number, description in problems.items():
        print(f"{number}. {description}")

    # Get user input for the problem
    while True:
        try:
            selected_problem = int(input("Enter the number of the problem you are facing (or 0 to exit): "))
            if selected_problem == 0:
                return
            elif selected_problem not in problems.keys():
                print("Invalid input. Please enter a valid problem number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Create the engine based on user selection
    if selected_problem <= 3:
        engine = DishwasherStopsWorking()
    else:
        engine = ResultsNotSatisfactory()

    # Reset and run the engine with the user-selected problem description
    engine.reset()
    print()
    engine.declare(Problem(description=problems[selected_problem]))
    engine.run()


if __name__ == "__main__":
    main()
