# With this exercise we will work on the evaluation function of the algorithm.
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

    origin=Node(stationList[1],None)            # Charpennes L1
    child=Node(stationList[4], origin)          # Charpennes L2
    destination=Node(stationList[13],None)      # Dauphine lacassagne L4

    #------------------------------------------------------------------#


    #HEURISTIC 1 : TIME
    timeCostTable=setCostTable(1,stationList, city)
    child.setHeuristic(1,destination,city)
    child.setRealCost( timeCostTable)
    child.setEvaluation()
    print " Evaluation Function (TIME) from " + child.station.name + " L" + str(child.station.line) + " to " + destination.station.name + " L" + str(destination.station.line) +  ": \t\t" +  str(child.f)
    print "                               g : " + str(child.g)
    print "                               h : " + str(child.h) + "\n"

    #HEURISTIC 2 : DISTANCE
    distCostTable=setCostTable( 2,  stationList,city)
    child.setHeuristic(2,destination,city)
    child.setRealCost( distCostTable)
    child.setEvaluation()
    print " Evaluation Function (DISTANCE) from " + child.station.name + " L" + str(child.station.line) + " to " + destination.station.name + " L" + str(destination.station.line) +  ": \t\t" +  str(child.f)
    print "                               g : "  + str(child.g)
    print "                               h : " + str(child.h) + "\n"

    #HEURISTIC 3 : TRANSFERS
    transCostTable=setCostTable( 3,  stationList,city)
    child.setHeuristic(3,destination,city)
    child.setRealCost( transCostTable)
    child.setEvaluation()
    print " Evaluation Function (#TRANSFERS) from " + child.station.name + " L" + str(child.station.line) + " to " + destination.station.name + " L" + str(destination.station.line) +  ": \t\t" +  str(child.f)
    print "                               g : " + str(child.g)
    print "                               h : " + str(child.h) + "\n"

    #HEURISTIC 4 : STOP STATIONS
    stopCostTable=setCostTable(4, stationList,city)
    child.setHeuristic(4,destination,city)
    child.setRealCost(  stopCostTable)
    child.setEvaluation()
    print " Evaluation Function (#STATIONS) from " + child.station.name + " L" + str(child.station.line) + " to " + destination.station.name + " L" + str(destination.station.line) +  ": \t\t" +  str(child.f)
    print "                               g : " + str(child.g)
    print "                               h : " + str(child.h) + "\n"



if __name__ == '__main__':
    main()