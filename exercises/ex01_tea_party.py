"""Tea Party Planning"""

__author__: str = "730552953"


def main_planner(guests: int) -> None:
    """calculate the cost of the party based on the number of guests"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(tea_bags(people=guests))))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """find the number of tea bags needed for the party"""
    return people * 2


def treats(tea_bags: int) -> int:
    """find the number of treats needed for the party"""
    return int(tea_bags * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    "find the cost of the party"
    return 0.5 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
