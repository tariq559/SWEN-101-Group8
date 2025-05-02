#s
class Planet:
    __slots__ = ['__name', '__size', '__orbit']

    def __init__(self, name, size, orbit):
        self.__name = name
        self.__size = size
        self.__orbit = orbit

    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size

    def get_orbit(self):
        return self.__orbit

    def __str__(self):
        return f"{self.__name}:{self.__size}:{self.__orbit}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Planet):
            return self.__size == other.__size
        return False

    def __lt__(self, other):
        if isinstance(other, Planet):
            return self.__size < other.__size
        return False

    def __hash__(self):
        return hash((self.__name, self.__size, self.__orbit))

class Planets:
    __slots__ = ['__planetsDB']

    def __init__(self) -> None:
        self.__planetsDB = {}
        for planet in PLANET_DATA:
            new_planet = Planet(planet[0], planet[1], planet[2])
            self.__planetsDB[planet[0]] = new_planet

    def get_names(self):
        return sorted(self.__planetsDB.keys())

    def get_planet(self, name):
        return self.__planetsDB.get(name, None)

    def get_orbit_delta(self, planet1, planet2):
        p1 = self.get_planet(planet1)
        p2 = self.get_planet(planet2)
        if p1 is None or p2 is None:
            return None
        return abs(p1.get_orbit() - p2.get_orbit())


from list_stack import Stack

BACKSPACE_CHAR = '<'

def backspace(a_string):
    stack = Stack()

    for char in a_string:
        if char == BACKSPACE_CHAR:
            if not stack.is_empty():
                stack.pop()
        else:
            stack.push(char)

    # Construct the resulting string
    result = ""
    while not stack.is_empty():
        result = stack.pop() + result

    return result


def compete(team1, team2):
    q1 = Queue()
    q2 = Queue()

    for player in team1:
        q1.enqueue(player)
    for player in team2:
        q2.enqueue(player)

    round_num = 1
    while not q1.is_empty() and not q2.is_empty():
        p1 = q1.dequeue()
        p2 = q2.dequeue()

        c1 = make_choice()
        c2 = make_choice()

        print(f"Round {round_num}: {p1} ({c1}) vs {p2} ({c2})")

        result = winner(c1, c2)

        if result == 1:
            print(f"{p1} wins and returns to the back of their line\n")
            q1.enqueue(p1)
        elif result == 2:
            print(f"{p2} wins and returns to the back of their line\n")
            q2.enqueue(p2)
        else:
            print("It's a tie, both return to the back of their lines\n")
            q1.enqueue(p1)
            q2.enqueue(p2)

        round_num += 1

    if q1.is_empty():
        print("Team 2 wins!")
    else:
        print("Team 1 wins!")
