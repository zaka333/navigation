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
import heapq

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
    print " \n\n\n___________ test EX 8 : REMOVE REDUNDANT PATHS _______________________\n"
    typePreference=int(1)
    currentCostTable=setCostTable( typePreference, stationList,city)
	
    destination=Node(stationList[13],None)								# Dauphhine Lacassagne L4
    test_ok=0
    print "\n \n     1: "
	
    partialCostTable = {}
    nodeList = []  #Nodes to be visited
    node1=Node(stationList[4],None)			# Charpennes L2
    node1.setHeuristic(typePreference,destination,city)
    node1.setRealCost(currentCostTable)
    node1.setEvaluation()
    heapq.heappush(nodeList, node1)
    childrenList=Expand(node1, stationList, typePreference, destination, currentCostTable, city)
    eval1=[]

    for i in range(0,len(childrenList)):
		eval1.append(childrenList[i].station.id)  
    eval1.sort()
	
    childrenList, nodeList, partialCostTable = RemoveRedundantPaths(childrenList, nodeList, partialCostTable)
    eval1=[]
    for i in range(0,len(childrenList)):
		eval1.append(childrenList[i].station.id)
    eval1.sort()

    correctTCP={}
    correctTCP[2]=20
    correctTCP[4]=5.42857142857
    correctTCP[10]=8
    correctTCP[6]=7.14285714286
	
    if eval1 == [2,4,6,10]:
		print "              childrenList --> OK!"
		test_ok=test_ok+1
    else:
		print "              childrenList --> FAIL!"
    num_correct=0
    for i in correctTCP.keys():
		if partialCostTable.has_key(int(i)) == False:
			print "                     TCP FAILS. Your table has not the primary key " + str(i)
		else:
			
			if abs (partialCostTable[i] - correctTCP[i])> 0.01:
				print "                     TCP FAILS. Incorrect value in the table at (" + str(i) + ")"
			else:
				num_correct=num_correct+1
    
	
	
    if num_correct==len(correctTCP.keys()):
		print "              TCP          --> OK!"
		test_ok=test_ok+1
    else:
		print "              TCP          --> FAILS!"
    current_ids_nodeList=[]
    for i in nodeList:
		current_ids_nodeList.append(i.station.id)
    
	
    current_ids_nodeList.sort()
	
    if current_ids_nodeList==[5]:
		print "              nodeList     --> OK!"
		test_ok=test_ok+1
    else:
		print "              nodeList     --> FAIL!"
	
    for child in childrenList:
        heapq.heappush(nodeList, child)
	
	
	
	#----------------------------------------------------------------------------------------------------------
	
    print "\n \n     2: "
    node1=Node(stationList[6],None)			# College-Bellecombe L2
    node1.setHeuristic(typePreference,destination,city)
    node1.setRealCost(currentCostTable)
    node1.setEvaluation()
    
    childrenList=Expand(node1, stationList, typePreference, destination, currentCostTable, city)
    eval1=[]
    for i in range(0,len(childrenList)):
		eval1.append(childrenList[i].station.id)
    eval1.sort()
	
    childrenList, nodeList, partialCostTable = RemoveRedundantPaths(childrenList, nodeList, partialCostTable)
    eval1=[]
    costes=[]
    for i in range(0,len(childrenList)):
		eval1.append(childrenList[i].station.id)
		costes.append(childrenList[i].g)
    eval1.sort()

    correctTCP={}
    correctTCP[2]=20
    correctTCP[4]=5.42857142857
    correctTCP[10]=8
    correctTCP[6]=4.21428571429
    correctTCP[8]=6.03739282526
	
    if eval1 == [6,8]:
		print "              childrenList --> OK!"
		test_ok=test_ok+1
    else:
		print "              childrenList --> FAIL!"
    num_correct=0
    for i in correctTCP.keys():
		if partialCostTable.has_key(int(i)) == False:
			print "                     TCP FAILS. Your table has not the primary key " + str(i)
		else:
			
			if abs (partialCostTable[i] - correctTCP[i])> 0.01:
				print "                     TCP FAILS. Incorrect value in the table at (" + str(i) + ")"
			else:
				num_correct=num_correct+1
    
	
	
    if num_correct==len(correctTCP.keys()):
		print "              TCP          --> OK!"
		test_ok=test_ok+1
    else:
		print "              TCP          --> FAILS!"
    current_ids_nodeList=[]
    costes=[]
    for child in childrenList:
        heapq.heappush(nodeList, child)
    for i in nodeList:
		current_ids_nodeList.append(i.station.id)
	
    current_ids_nodeList.sort()
	
    if current_ids_nodeList==[2,4,5,6,8,10]:
		print "              nodeList     --> OK!"
		test_ok=test_ok+1
    else:       
		print "              nodeList     --> FAIL!"
	

	
	
	#-----------------------------------------------------------------------------
    print "\n \n     3: "
    node1=Node(stationList[4],Node(stationList[3],None))			# College-Bellecombe L2
    node1.setHeuristic(typePreference,destination,city)
    node1.setRealCost(currentCostTable)
    node1.setEvaluation()
    
    childrenList=Expand(node1, stationList, typePreference, destination, currentCostTable, city)
    eval1=[]
    for i in range(0,len(childrenList)):
		eval1.append(childrenList[i].station.id)
    eval1.sort()
	
    childrenList, nodeList, partialCostTable = RemoveRedundantPaths(childrenList, nodeList, partialCostTable)
    eval1=[]
    for i in range(0,len(childrenList)):
		eval1.append(childrenList[i].station.id)
    eval1.sort()

    correctTCP={}
    correctTCP[2]=20
    correctTCP[4]=5.42857142857
    correctTCP[10]=8
    correctTCP[6]=4.21428571429
    correctTCP[8]=6.03739282526
	
    if eval1 == []:
		print "              childrenList --> OK!"
		test_ok=test_ok+1
    else:
		print "              childrenList --> FAIL!"
    num_correct=0
    for i in correctTCP.keys():
		if partialCostTable.has_key(int(i)) == False:
			print "                     TCP FAILS. Your table has not the primary key " + str(i)
		else:
			
			if abs (partialCostTable[i] - correctTCP[i])> 0.01:
				print "                     TCP FAILS. Incorrect value in the table at (" + str(i) + ")"
			else:
				num_correct=num_correct+1
    
	
	
    if num_correct==len(correctTCP.keys()):
		print "              TCP          --> OK!"
		test_ok=test_ok+1
    else:
		print "              TCP          --> FAILS!"
    current_ids_nodeList=[]
    for i in nodeList:
		current_ids_nodeList.append(i.station.id)
	
    current_ids_nodeList.sort()
	
    if current_ids_nodeList==[2,4,5,6,8,10]:
		print "              nodeList     --> OK!"
		test_ok=test_ok+1
    else:
		print "              nodeList     --> FAIL!"
	
    for child in childrenList:
        heapq.heappush(nodeList, child)
		
    print "\n                   Test Passed : " + str(test_ok) + " / 9 \n"
		
		
if __name__ == '__main__':
    main()