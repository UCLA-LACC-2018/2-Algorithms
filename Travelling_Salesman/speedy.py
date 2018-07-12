from tools import *
#*************************************
# This is where you write your code
# input: all locations
# output: locations (sorted)
#*************************************
#number 2 is the first smallest
#number 15 is next smallest
#number 24
#number 49
#number 1
#number 4
#number 31
def speedyTrip(places):
    # places is a list of locations
    # the first place is places[0]
    # places[0].name : name of the first place
    # places[0].x
    # x_location
    # places[0].y
    # y_location
    # the distance between places[0] and places[1]
    mindistance = 1000000000
    minplace = places[0]
    currplace = places[0]
    for x :
        for i in range(1,51):
            if(get_distance(currplace, places[i]) < mindistance):
            mindistance = get_distance(currplace, places[i])
            minplace = places[i]    
    print(minplace.name + " " + str(mindistance))


    #these are random code statement that you may or may not want to use.
    print(get_distance(places[0], places[51]))
    places.append(places[0])
    cities=[52]
    unvisited_cities=list(range(0,51))
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
    
    N = len(places)
    #for i in range(0,N):
       # x = 0
        #ye = get_distance(places[i], places[52])
       # x = x + 1
   # print (ye)

    # ...
    # 
    # or 
    # foreach place in places:
    # ...


    # return the places to be evaluated
    return places