# With this exercise we will work on removing cycles from a path
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
    destination=Node(stationList[13],None)      #Dauphine lacassagne L4

    #------------------------------------------------------------------#




    #HEURISTIC 1 : TIME
    print "\n________ TIME ____________"
    timeCostTable=setCostTable( 1, stationList,city)
    origin.setHeuristic( 1, destination,city)
    origin.setRealCost(timeCostTable)
    origin.setEvaluation()
    childrenList=Expand(origin, stationList, 1, destination, timeCostTable, city)
    childrenList=RemoveCycles(childrenList)
    print " Current: [" + str(origin.station.id) + "] " + origin.station.name + " L" + str(origin.station.line)  +  " \tf = " + str('%.2f' % origin.f) + " -> g: " + str( '%.2f' %origin.g) + " + h: " + str('%.2f' % origin.h)
    print "\n"
    for i in childrenList:
        print "  ---  Child: [" + str(i.station.id) + "] " + i.station.name + " L" + str(i.station.line) +  " \tf = " + str('%.2f' % i.f) + "\tg: " + str('%.2f' % i.g) + " \th: " + str('%.2f' % i.h)


    print "\n"
    origin2=childrenList[3] #Charpennes L2 (to be connected to the previous route)
    origin2.setHeuristic( 1, destination,city)
    origin2.setRealCost(timeCostTable)
    origin2.setEvaluation()
    childrenList=Expand(origin2, stationList, 1, destination, timeCostTable,city)
    childrenList=RemoveCycles(childrenList)
    print "\n"
    print " Current: [" + str(origin2.station.id) + "] " + origin2.station.name + " L" + str(origin2.station.line) +  " \tf = " + str('%.2f' % origin2.f) + " -> g: " + str( '%.2f' %origin2.g) + " + h: " + str('%.2f' % origin2.h)
    for i in childrenList:
        print "  ---  Child: [" + str(i.station.id) + "] " + i.station.name + " L" + str(i.station.line) +  " \tf = " + str('%.2f' % i.f) + "\tg: " + str('%.2f' % i.g) + " \th: " + str('%.2f' % i.h)



    #HEURISTIC 1 : DISTANCE
    print "\n"
    print "\n________ DISTANCE ____________"
    distanceCostTable=setCostTable( 2, stationList,city)
    origin.setHeuristic( 2, destination,city)
    origin.setRealCost(distanceCostTable)
    origin.setEvaluation()
    childrenList=Expand(origin, stationList, 2, destination, distanceCostTable, city)
    childrenList=RemoveCycles(childrenList)
    print " Current: [" + str(origin.station.id) + "] " + origin.station.name + " L" + str(origin.station.line) + " \tf = " + str('%.2f' % origin.f) + " -> g: " + str( '%.2f' %origin.g) + " + h: " + str('%.2f' % origin.h)
    print "\n"
    for i in childrenList:
        print "  ---  Child: [" + str(i.station.id) + "] " + i.station.name + " L" + str(i.station.line) +   " \tf = " + str('%.2f' % i.f) + "\tg: " + str('%.2f' % i.g) + " \th: " + str('%.2f' % i.h)


    print "\n"
    origin2=childrenList[3] #Charpennes L2 (to be connected to the previous route)
    origin2.setHeuristic( 2, destination,city)
    origin2.setRealCost(distanceCostTable)
    origin2.setEvaluation()
    childrenList=Expand(origin2, stationList, 2, destination, distanceCostTable,city)
    childrenList=RemoveCycles(childrenList)
    print " Current: [" + str(origin2.station.id) + "] " + origin2.station.name + " L" + str(origin2.station.line) + " \tf = " + str('%.2f' % origin2.f) + " -> g: " + str( '%.2f' %origin2.g) + " + h: " + str('%.2f' % origin2.h)
    print "\n"
    for i in childrenList:
        print "  ---  Child: [" + str(i.station.id) + "] " + i.station.name + " L" + str(i.station.line) +   " \tf = " + str('%.2f' % i.f) + "\tg: " + str('%.2f' % i.g) + " \th: " + str('%.2f' % i.h)


    #HEURISTIC 3 : TRANSFERS
    print "\n"
    print "\n________ # TRANSFERS ____________"
    transferCostTable=setCostTable( 3, stationList,city)
    origin.setHeuristic( 3, destination,city)
    origin.setRealCost(transferCostTable)
    origin.setEvaluation()
    childrenList=Expand(origin, stationList, 3, destination, transferCostTable, city)
    childrenList=RemoveCycles(childrenList)
    print " Current: [" + str(origin.station.id) + "] " + origin.station.name + " L" + str(origin.station.line) + " \tf = " + str('%.2f' % origin.f) + " -> g: " + str( '%.2f' %origin.g) + " + h: " + str('%.2f' % origin.h)
    print "\n"
    for i in childrenList:
        print "  ---  Child: [" + str(i.station.id) + "] " + i.station.name + " L" + str(i.station.line) +  " \tf = " + str('%.2f' % i.f) + "\tg: " + str('%.2f' % i.g) + " \th: " + str('%.2f' % i.h)

    print "\n"
    origin2=childrenList[3] #Charpennes L2 (to be connected to the previous route)
    origin2.setHeuristic( 3, destination,city)
    origin2.setRealCost(transferCostTable)
    origin2.setEvaluation()
    childrenList=Expand(origin2, stationList, 3, destination, transferCostTable,city)
    childrenList=RemoveCycles(childrenList)
    print " Current: [" + str(origin2.station.id) + "] " + origin2.station.name + " L" + str(origin2.station.line) + " \tf = " + str('%.2f' % origin2.f) + " -> g: " + str( '%.2f' %origin2.g) + " + h: " + str('%.2f' % origin2.h)
    print "\n"
    for i in childrenList:
        print "  ---  Child: [" + str(i.station.id) + "] " + i.station.name + " L" + str(i.station.line) +  " \tf = " + str('%.2f' % i.f) + "\tg: " + str('%.2f' % i.g) + " \th: " + str('%.2f' % i.h)



    #HEURISTIC 4 : STOPS
    print "\n"
    print "\n________ # STATIONS ____________"
    stationCostTable=setCostTable( 4, stationList,city)
    origin.setHeuristic( 4, destination,city)
    origin.setRealCost(stationCostTable)
    origin.setEvaluation()
    childrenList=Expand(origin, stationList, 4, destination, stationCostTable, city)
    childrenList=RemoveCycles(childrenList)
    print " Current: [" + str(origin.station.id) + "] " + origin.station.name + " L" + str(origin.station.line)+ " \tf = " + str('%.2f' % origin.f) + " -> g: " + str( '%.2f' %origin.g) + " + h: " + str('%.2f' % origin.h)
    print "\n"
    for i in childrenList:
        print "  ---  Child: [" + str(i.station.id) + "] " + i.station.name + " L" + str(i.station.line) +   " \tf = " + str('%.2f' % i.f) + "\tg: " + str('%.2f' % i.g) + " \th: " + str('%.2f' % i.h)

    print "\n"
    origin2=childrenList[3] #Charpennes L2 (to be connected to the previous route)
    origin2.setHeuristic( 4, destination,city)
    origin2.setRealCost(stationCostTable)
    origin2.setEvaluation()
    childrenList=Expand(origin2, stationList, 4, destination, stationCostTable,city)
    childrenList=RemoveCycles(childrenList)
    print " Current: [" + str(origin2.station.id) + "] " + origin2.station.name + " L" + str(origin2.station.line)+ " \tf = " + str('%.2f' % origin2.f) + " -> g: " + str( '%.2f' %origin2.g) + " + h: " + str('%.2f' % origin2.h)
    print "\n"
    for i in childrenList:
        print "  ---  Child: [" + str(i.station.id) + "] " + i.station.name + " L" + str(i.station.line) +  " \tf = " + str('%.2f' % i.f) + "\tg: " + str('%.2f' % i.g) + " \th: " + str('%.2f' % i.h)


if __name__ == '__main__':
    main()