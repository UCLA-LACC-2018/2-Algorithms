from tools import *
#*************************************
# This is where you write your code
# input: all locations
# output: locations (sorted)
#*************************************
def speedyTrip(places):
    # places is a list of locations
    # the first place is places[0]
    # places[0].name : name of the first place
    # places[0].x
    # x_location
    # places[0].y
    # y_location
    # get_distance(places[0], places[1]) returns
    # the distance between places[0] and places[1]
    current = 0
    cities = [places[0]]
    unvisited_cities = list(range(1, len(places)))

    while len(unvisited_cities) > 0:
        closest = unvisited_cities[0]
        shortest = get_distance(places[current], places[closest])
        for city in unvisited_cities:
            distance = get_distance(places[current], places[city])
            if distance < shortest:
                shortest = distance
                closest = city
        current = closest
        cities.append(places[current])
        unvisited_cities.remove(current)

    cities.append(places[0])

    return cities







