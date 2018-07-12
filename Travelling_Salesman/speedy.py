from tools import *
import sys
#*************************************
# This is where you write your code
# input: all locations
# output: locations (sorted)
#*************************************
def speedyTrip(places):
    TotalDistances = []
    listofplaces = []
    dIndex = 0
    for x in range (len(places)):
        minDistance = sys.maxsize
        Distance = 0
        
        new_places = places.copy()
        #need to place next city to start as vertex in the front of the list new_places
        temp = new_places[x]
        new_places[x] = new_places[0]
        new_places[0] = temp
        
        for z in range (len(places)):
        
            for y in range(z+1,len(places)):
                if get_distance(new_places[z],new_places[y]) < minDistance:
                    minDistance = get_distance(new_places[z],new_places[y])
                    temp1 = new_places[y]
                    new_places[y] = new_places[z+1]
                    new_places[z+1] = temp1
                    Distance += minDistance
            #need to compare distances between cities and swap position
            
        listofplaces.append(new_places)
        TotalDistances.append(Distance)
        
    for i in range (len(TotalDistances)):
        tempMin = sys.maxsize
        if TotalDistances[i] < tempMin:
            tempMin = TotalDistances[i]
            dIndex = i
            
    places = listofplaces[i].copy()
    #print (TotalDistances)
    #print (places)
    #-----------------------------------------------------------------------------------------------------------------------
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
    #print(get_distance(places[0], places[1]))
    #places.append(places[0])
    #cities=[]
    #unvisited_cities=list(range(0,50))
    #visited_cities=[0]
    #print (visited_cities)
    #print (unvisited_cities)
    #unvisited_cities.remove(0)
    #next_city= unvisited_cities[0]
    #while unvisited_cities !=[]:
    #   cities.append(next_city)
    
    #visited_cities.append(next_city)
    #unvisited_cities.remove(next_city)
    #print (visited_cities)
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