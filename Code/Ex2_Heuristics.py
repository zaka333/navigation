# With this exercise we will work on the definition of the heuristics.
#
__authors__='TO_BE_FILLED'
__group__='DL01'
# _________________________________________________________________________________________
# Intel.ligencia Artificial
# Grau en Enginyeria Informatica
# Curs 2016- 2017
# Universitat Autonoma de Barcelona
# _______________________________________________________________________________________

from SearchAlgorithm import *
from SubwayMap import *
import os

def main():

    #------------------------------------------------------------------#
    city_string="Lyon_smallCity"
    #read file
    filename = os.path.join(os.path.dirname(__file__),"..","CityInformation",city_string,"Stations.txt")
    stationList=readStationInformation(filename)
    #read adjacency matrix
    filename = os.path.join(os.path.dirname(__file__),"..","CityInformation",city_string,"Connections.txt")
    adjacency=readCostTable(filename)

    #Real TIME cost table
    filename = os.path.join(os.path.dirname(__file__),"..","CityInformation",city_string,"Time.txt")
    timeStations = readCostTable(filename)
    setNextStations(stationList, timeStations)

    # CITY information
    # velocity
    filename = os.path.join(os.path.dirname(__file__),"..","CityInformation",city_string,"InfoVelocity.txt")
    infoVelocity = readInformation(filename)
    # Transfers times
    filename = os.path.join(os.path.dirname(__file__),"..","CityInformation",city_string,"InfoTransfers.txt")
    infoTransfers = readInformation(filename)
    multipleLines=search_multiple_lines(stationList)
    city=CityInfo(len(infoVelocity),infoVelocity,infoTransfers,adjacency, multipleLines)

    #------------------------------------------------------------------#

    origin=Node(stationList[5],None)                    # Charpennes L2
    destination=Node(stationList[13],None)               # Dauphine Lacassagne L4

    #------------------------------------------------------------------#


    #HEURISTIC 1 : TIME
    origin.setHeuristic( 1, destination,city)
    print " HEURISTIC (TIME) from " + origin.station.name + " L" + str(origin.station.line) + " to " + destination.station.name + " L" + str(destination.station.line) + "  : \t\t" +   str(origin.h)


    #HEURISTIC 2 : DISTANCE
    origin.setHeuristic( 2, destination,city)
    print " HEURISTIC (DISTANCE) from " + origin.station.name + " L" + str(origin.station.line) + " to " + destination.station.name + " L" + str(destination.station.line) + "  : \t\t" +  str(origin.h)

    #HEURISTIC 3 : TRANSFERS
    origin.setHeuristic( 3, destination,city)
    print " HEURISTIC (#TRANSFERS) from " + origin.station.name + " L" + str(origin.station.line) + " to " + destination.station.name + " L" + str(destination.station.line) + "  : \t\t" +   str(origin.h)


    #HEURISTIC 4 : STOP STATIONS
    origin.setHeuristic( 4, destination,city)
    print " HEURISTIC (#STATIONS) from " + origin.station.name + " L" + str(origin.station.line) + " to " + destination.station.name + " L" + str(destination.station.line) + "  : \t\t" +   str(origin.h)




if __name__ == '__main__':
    main()