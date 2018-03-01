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
    currentCostTable=setCostTable( typePreference, stationList,city)
    origin1=Node(stationList[13],None)                 				# Dauphhine Lacassagne L4
    destination=Node(stationList[2],None)							# Republique L1
    childrenList=Expand(origin1, stationList, typePreference, destination, currentCostTable, city)
    nodeList=sorted_insertion(nodeList,childrenList)
    current_ids=[]
    test_ok=0
    for i in nodeList:
		current_ids.append(i.station.id)
    if current_ids==[13]:
		print "     1:  sorted insertion  --> OK!"
		test_ok=test_ok+1
    else:
		print "     1:  sorted insertion  --> FAIL!"
	#----------------------------------------------------------------------
    print "\n"
    origin1=Node(stationList[12],None)                 				
    childrenList=Expand(origin1, stationList, typePreference, destination, currentCostTable, city)
    nodeList=sorted_insertion(nodeList,childrenList)
    current_ids=[]
    for i in nodeList:
		current_ids.append(i.station.id)
    if current_ids==[8,12,13,14]:
		print "     2:  sorted insertion  --> OK!"
		test_ok=test_ok+1
    else:
		print "     2:  sorted insertion  --> FAIL!"
		
	#----------------------------------------------------------------------	
    print "\n"
    origin1=Node(stationList[3],None)                 	

    childrenList=Expand(origin1, stationList, typePreference, destination, currentCostTable, city)
    nodeList=sorted_insertion(nodeList,childrenList)
    current_ids=[]
    for i in nodeList:
		current_ids.append(i.station.id)
    if current_ids==[5,8,12,13,14]:
		print "     3:  sorted insertion  --> OK!"
		test_ok=test_ok+1
    else:
		print "     3:  sorted insertion  --> FAIL!"
	
	#----------------------------------------------------------------------
    print "\n"
    origin1=Node(stationList[0],None)                 		
    childrenList=Expand(origin1, stationList, typePreference, destination, currentCostTable, city)
    nodeList=sorted_insertion(nodeList,childrenList)
    current_ids=[]
    for i in nodeList:
		current_ids.append(i.station.id)
    if current_ids==[2,5,8,12,13,14]:
		print "     4:  sorted insertion  --> OK!"
		test_ok=test_ok+1
    else:
		print "     4:  sorted insertion  --> FAIL!"
	
	#----------------------------------------------------------------------
    print "\n                   Test Passed : " + str(test_ok) + " / 4 \n"
	
	
		
if __name__ == '__main__':
    main()