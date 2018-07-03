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
    
    #these are random code statement that you may or may not want to use.
    print(get_distance(places[0], places[1]))
    places.append(places[0])
    cities=[]
    unvisited_cities=list(range(0,50))
    visited_cities=[0]
    print (visited_cities)
    print (unvisited_cities)
    unvisited_cities.remove(0)
    next_city= unvisited_cities[0]
    #while unvisited_cities !=[]:
    #   cities.append(next_city)
    
    visited_cities.append(next_city)
    unvisited_cities.remove(next_city)
    print (visited_cities)
    # you can iterate through the places as:
    #N = length(places)
    #for i in range(0,N):
    #   x = 0
    #   ye = get_distance(places[i], places[x])
    #   x = x + 1
    #   print ye

    # ...
    # 
    # or 
    # foreach place in places:
    # ...


    # return the places to be evaluated
    return places