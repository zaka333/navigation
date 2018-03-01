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
	
    typePreference=int(1)
    nodeList=[]
    partialCostTable = {}
    currentCostTable=setCostTable( typePreference, stationList,city)
	
	
	
	#Imagine that we have not explored anything. This is the first time that we analyze a specific node.
	#     - It means that the TCP is empty.
	#	  - For example, we suppose that we are starting our search algorithm on Massena L1 as the origin
	#	  - We set g and h with random values
	
	#nodeList is a list of Nodes to be visited (set of childs of several nodes that never have been expanded.)
    node1=Node(stationList[7],None)			# Part-Dieu L2
    node1.g=30
    node1.h=500
    heapq.heappush(nodeList, node1)
    print "\n ---------------------  (1)  ----------------- \n"	
    print "\n NODELIST :"
	
    for i in nodeList:
		print "        " + str(i.station.id) + "     --> parents.ID : " + str(i.parentsID) + "   asoc. cost: " + str(i.g)
	
	# Now we have to analyze the head of our list:
    current = heapq.heappop(nodeList)
	
	# look at the list again!
    print "\n NODELIST  (after taking out the head): "
	
    for i in nodeList:
		print "        " + str(i.station.id) + "     --> parents.ID : " + str(i.parentsID) + "   asoc. cost: " + str(i.g)
    destination=Node(stationList[13],None)								# Dauphhine Lacassagne L4
	
	# Expand head of the list
    childrenList=Expand(current, stationList, typePreference, destination, currentCostTable, city)
	
	# Look to its childrens:
	#		- It is recommended to set .g and .h values inside Expand function for each child. 
	#		- You should have values inside i.g in the following print
    print "\n CHILDRENLIST   "
    for i in childrenList:
		print "        " + str(i.station.id) + "     --> parents.ID : " + str(i.parentsID) + "   asoc. cost: " + str(i.g)
    
	#Remove Redundant paths
    childrenList, nodeList, partialCostTable = RemoveRedundantPaths(childrenList, nodeList, partialCostTable)
	
	# Look to the TCP:
    print "\n TCP  (after removing Redundant Paths): "
    for i in partialCostTable.keys():
        print "        ID : " + str(i) + "    cost: " + str(partialCostTable[i])
	
    print "\n NODELIST  (after removing Redundant Paths): "
	
    for i in nodeList:
		print "        " + str(i.station.id) + "     --> parents.ID : " + str(i.parentsID) + "   asoc. cost: " + str(i.g)
	
    print "\n CHILDRENLIST (after removing Redundant Paths):  "
    for i in childrenList:
		print "        " + str(i.station.id) + "     --> parents.ID : " + str(i.parentsID) + "   asoc. cost: " + str(i.g)
	

	#add childs into the list for visiting. IN THIS EXAMPLE, WE DO NOT INSTERT THEM SORTEDLY!
    for child in childrenList:
        heapq.heappush(nodeList, child)
    print "\n NODELIST  (after adding childs): "
	
    for i in nodeList:
		print "        " + str(i.station.id) + "     --> parents.ID : " + str(i.parentsID) + "   asoc. cost: " + str(i.g)
	
    print "\n ---------------------  (2)  ----------------- \n"	
	# Now we have to analyze the head of our list:
    current = heapq.heappop(nodeList)

    # Expand head of the list
    childrenList=Expand(current, stationList, typePreference, destination, currentCostTable, city)
	
	# Look to its childrens:
    print "\n CHILDRENLIST  of the node :  "  + str(current.station.id)
    for i in childrenList:
		print "        " + str(i.station.id) + "     --> parents.ID : " + str(i.parentsID) + "   asoc. cost: " + str(i.g)
	
	#Remove Redundant paths
    childrenList, nodeList, partialCostTable = RemoveRedundantPaths(childrenList, nodeList, partialCostTable)
	
	# Look to the TCP:
	#    - Compare current TCP with the previous one. You should have another entry and previous entries, should have the same associated cost.
    print "\n TCP  (after removing Redundant Paths): "
    for i in partialCostTable.keys():
        print "        ID : " + str(i) + "    cost: " + str(partialCostTable[i])
	
	#Look to Nodelist
	#	- compare with the previous one
	#	- one item should be removed (why?)
    print "\n NODELIST  (after removing Redundant Paths): "
    for i in nodeList:
		print "        " + str(i.station.id) + "     --> parents.ID : " + str(i.parentsID) + "   asoc. cost: " + str(i.g)
	
	#Look to ChildrenList
	#	- compare with the previous one
	#	- We should have exactly the same childrenList as before removing reduntant paths
    print "\n CHILDRENLIST (after removing Redundant Paths):  "
    for i in childrenList:
		print "        " + str(i.station.id) + "     --> parents.ID : " + str(i.parentsID) + "   asoc. cost: " + str(i.g)
	
	#add childs into the list for visiting. IN THIS EXAMPLE, WE DO NOT INSTERT THEM SORTEDLY!
    for child in childrenList:
        heapq.heappush(nodeList, child)
    
	
	#Look to Nodelist
	#	- compare with the previous one
	#	- one item should be added
    print "\n NODELIST  (after adding childs): "
	
    for i in nodeList:
		print "        " + str(i.station.id) + "     --> parents.ID : " + str(i.parentsID) + "   asoc. cost: " + str(i.g)
		
    print "\n ---------------------  (3)  ----------------- \n"	
	# Now we have to analyze the head of our list:
    current = heapq.heappop(nodeList)

    # Expand head of the list
    childrenList=Expand(current, stationList, typePreference, destination, currentCostTable, city)
	
	# Look to its childrens:
    print "\n CHILDRENLIST  of the node :  "  + str(current.station.id)
    for i in childrenList:
		print "        " + str(i.station.id) + "     --> parents.ID : " + str(i.parentsID) + "   asoc. cost: " + str(i.g)
	
	#Remove Redundant paths
    childrenList, nodeList, partialCostTable = RemoveRedundantPaths(childrenList, nodeList, partialCostTable)
	
	# Look to the TCP:
	#    - Compare current TCP with the previous one. You should have more entries. (why?)
    print "\n TCP  (after removing Redundant Paths): "
    for i in partialCostTable.keys():
        print "        ID : " + str(i) + "    cost: " + str(partialCostTable[i])
	
	#Look to Nodelist
	#	- compare with the previous one
	#	- one item should be removed (why?)
    print "\n NODELIST  (after removing Redundant Paths): "
    for i in nodeList:
		print "        " + str(i.station.id) + "     --> parents.ID : " + str(i.parentsID) + "   asoc. cost: " + str(i.g)
	
	#Look to ChildrenList
	#	- compare with the previous one
	#	- Two items should be removed. (why?)
    print "\n CHILDRENLIST (after removing Redundant Paths):  "
    for i in childrenList:
		print "        " + str(i.station.id) + "     --> parents.ID : " + str(i.parentsID) + "   asoc. cost: " + str(i.g)
	#add childs into the list for visiting. IN THIS EXAMPLE, WE DO NOT INSTERT THEM SORTEDLY!
    for child in childrenList:
        heapq.heappush(nodeList, child)
 
	#Look to Nodelist
	#	- compare with the previous one
	#	- one item should be added
    print "\n NODELIST  (after adding childs): "
	
    for i in nodeList:
		print "        " + str(i.station.id) + "     --> parents.ID : " + str(i.parentsID) + "   asoc. cost: " + str(i.g)	
		
		
    print "\n ---------------------  (4)  ----------------- \n"	
	# Now we have to analyze the head of our list:
    current = heapq.heappop(nodeList)

    # Expand head of the list
    childrenList=Expand(current, stationList, typePreference, destination, currentCostTable, city)
	
	# we modify randomly the values of the childrens to have less associated cost
    for i in childrenList:
		i.g=2
		
	# Look to its childrens:
    print "\n CHILDRENLIST  of the node :  "  + str(current.station.id)
    for i in childrenList:
		print "        " + str(i.station.id) + "     --> parents.ID : " + str(i.parentsID) + "   asoc. cost: " + str(i.g)
	
	#Remove Redundant paths
    childrenList, nodeList, partialCostTable = RemoveRedundantPaths(childrenList, nodeList, partialCostTable)
	
	# Look to the TCP:
	#    - Compare current TCP with the previous one. 
	#	 - two of the previous entries should have less associated cost than the previous print
	#	 - one extra entry has been set into the TCP
    print "\n TCP  (after removing Redundant Paths): "
    for i in partialCostTable.keys():
        print "        ID : " + str(i) + "    cost: " + str(partialCostTable[i])
	
	#Look to Nodelist
	#	- should be empty!!! (why???)
    print "\n NODELIST  (after removing Redundant Paths): "
    for i in nodeList:
		print "        " + str(i.station.id) + "     --> parents.ID : " + str(i.parentsID) + "   asoc. cost: " + str(i.g)
	
	#Look to ChildrenList
	#	- compare with the previous one
	#	- Should be the same than the previous one
    print "\n CHILDRENLIST (after removing Redundant Paths):  "
    for i in childrenList:
		print "        " + str(i.station.id) + "     --> parents.ID : " + str(i.parentsID) + "   asoc. cost: " + str(i.g)
	#add childs into the list for visiting. IN THIS EXAMPLE, WE DO NOT INSTERT THEM SORTEDLY!
    for child in childrenList:
        heapq.heappush(nodeList, child)
 
	#Look to Nodelist
	#	- compare with the previous one
	#	- 3 new items
    print "\n NODELIST  (after adding childs): "	
    for i in nodeList:
		print "        " + str(i.station.id) + "     --> parents.ID : " + str(i.parentsID) + "   asoc. cost: " + str(i.g)		
    
		
		
		
		
if __name__ == '__main__':
    main()