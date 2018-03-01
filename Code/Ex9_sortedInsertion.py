# TO TEST setHeuristic FUNCTION
#
__authors__='TO_BE_FILLED'
__group__='DL01'
# _________________________________________________________________________________________
# Intel.ligencia Artificial
# Grau en Enginyeria Informatica
# Curs 2016- 2017
# Universitat Autonoma de Barcelona
# _______________________________________________________________________________________

import os
import sys

from SearchAlgorithm import *

from SubwayMap import *

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
	
	
    typePreference=int(1)
    nodeList=[]
    childrenList=[]
    childrenList.append(Node(stationList[0],None))
    childrenList[0].g=10
    childrenList[0].h=5
    childrenList[0].setEvaluation()
    nodeList=sorted_insertion(nodeList,childrenList)
    print "\n FIRST INSERTION: "
    for i in nodeList:
		print "  id: " + str(i.station.id) + "   cost: " + str(i.f)

    print "\n SECOND INSERTION: "
    childrenList=[]
    childrenList.append(Node(stationList[1],None))
    childrenList[0].g=38
    childrenList[0].h=25
    childrenList[0].setEvaluation()
    childrenList.append(Node(stationList[2],None))
    childrenList[1].g=8
    childrenList[1].h=3
    childrenList[1].setEvaluation()
    nodeList=sorted_insertion(nodeList,childrenList)
    for i in nodeList:
		print "  id: " + str(i.station.id) + "   cost: " + str(i.f)
    print "\n THIRD INSERTION: "
    childrenList=[]	
    childrenList.append(Node(stationList[3],None))
    childrenList[0].g=600
    childrenList[0].h=150
    childrenList[0].setEvaluation()
    childrenList.append(Node(stationList[4],None))
    childrenList[1].g=2
    childrenList[1].h=90
    childrenList[1].setEvaluation()
    childrenList.append(Node(stationList[5],None))
    childrenList[2].g=7
    childrenList[2].h=20
    childrenList[2].setEvaluation()
    nodeList=sorted_insertion(nodeList,childrenList)
    for i in nodeList:
		print "  id: " + str(i.station.id) + "   cost: " + str(i.f)
	
		
if __name__ == '__main__':
    main()