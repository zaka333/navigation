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

	
	#test for TIME
    print " ___________ test EX 2 : SET HEURISTIC _______________________\n"
    print "       TIME: \n"
	
    typePreference=int(1)
    time_test=0
    correct_test_time=[]
    diference_time=0
	#test n.1
    origin=Node(stationList[0],None)                # Massena L1
    destination=Node(stationList[0],origin)         # Massena L1
    origin.setHeuristic( typePreference, destination,city)
    diference_time=diference_time + abs(0 - origin.h)
    if origin.h <= 0:
		time_test=time_test+1
		correct_test_time.append(1)
		print "             1 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             1 : " + str(origin.h) +  "    --> FAIL!"

   
	
	#test n.2
    origin=Node(stationList[0],None)                # Massena L1
    destination=Node(stationList[3],origin)         # Le Tonkin L2
    origin.setHeuristic( typePreference, destination,city)
    diference_time=diference_time + abs(34.4824 - origin.h)
    if origin.h<=34.4824:
		time_test=time_test+1 
		correct_test_time.append(2)
		print "             2 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             2 : " + str(origin.h) +  "    --> FAIL!"
    
	
	#test n.3
    origin=Node(stationList[9],None)                # Charpennes L3
    destination=Node(stationList[2],origin)          # Republique L1
    origin.setHeuristic( typePreference, destination,city)
    diference_time=diference_time + abs(6.6258 - origin.h)
    if origin.h<=6.6258:
		time_test=time_test+1
		correct_test_time.append(3)
		print "             3 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             3 : " + str(origin.h) +  "    --> FAIL!"
	
	#test n.4
    origin=Node(stationList[8],None)                # Part-Dieu Sirvent L2
    destination=Node(stationList[6],origin)         # Thiers La Fayete L2
    origin.setHeuristic( typePreference, destination,city)
    diference_time=diference_time + abs(8.55391 - origin.h)
    if origin.h<=8.55391:
		time_test=time_test+1
		correct_test_time.append(4)
		print "             4 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             4 : " + str(origin.h) +  "    --> FAIL!"
	
    #test n.5
    origin=Node(stationList[11],None)                # Part-Dieu L3
    destination=Node(stationList[7],origin)          # Part-Dieu L2
    origin.setHeuristic( typePreference, destination,city)
    diference_time=diference_time + abs(12 - origin.h)
    if origin.h<=12:
		time_test=time_test+1
		correct_test_time.append(5)
		print "             5 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             5 : " + str(origin.h) +  "    --> FAIL!"
	
	#test n.6
    origin=Node(stationList[5],None)                # College Bellecombe L2
    destination=Node(stationList[1],origin)         # Charpennes L1
    origin.setHeuristic( typePreference, destination,city)
    diference_time=diference_time + abs(7.31112 - origin.h)
    if origin.h<=7.31112:
		time_test=time_test+1
		correct_test_time.append(6)
		print "             6 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             6 : " + str(origin.h) +  "    --> FAIL!"
		
	#test n.7
    origin=Node(stationList[13],None)                # Dauphine Lacasagne L4
    destination=Node(stationList[10],origin)         # Broteaux L3
    origin.setHeuristic( typePreference, destination,city)
    diference_time=diference_time + abs(38.99551 - origin.h)
    if origin.h<=38.99551:
		time_test=time_test+1
		correct_test_time.append(7)
		print "             7 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             7 : " + str(origin.h) +  "    --> FAIL!"
	
	#test n.8
    origin=Node(stationList[12],None)               #Part-Dieu L4
    destination=Node(stationList[7],origin)         #part-Dieu L2
    origin.setHeuristic( typePreference, destination,city)
    diference_time=diference_time + abs( 6- origin.h)
    if origin.h<=6:
		time_test=time_test+1
		correct_test_time.append(8)
		print "             8 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             8 : " + str(origin.h) +  "    --> FAIL!"
		
	#test n.9
    origin=Node(stationList[11],None)                #Part-Dieu L3
    destination=Node(stationList[9],origin)         #Charpennes L3
    origin.setHeuristic( typePreference, destination,city)
    diference_time=diference_time + abs(4.7847 - origin.h)
    if origin.h<=4.7847:
		time_test=time_test+1
		correct_test_time.append(9)
		print "             9 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             9 : " + str(origin.h) +  "    --> FAIL!"
		
	#test n.10
    origin=Node(stationList[11],None)                #Part-Dieu L3
    destination=Node(stationList[1],origin)         #Charpennes L1
    origin.setHeuristic( typePreference, destination,city)
    diference_time=diference_time + abs(9.40835 - origin.h)
    if origin.h<=9.40835:
		time_test=time_test+1
		correct_test_time.append(10)
		print "             10 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             10 : " + str(origin.h) +  "    --> FAIL!"
	
	
    print "\n            test passed: " + str(time_test) + " / 10" + "\n"
    print "             difference: " + str(diference_time) + "\n"
    
	
	#............................................................................................"
	#test for DISTANCE
    print "       DISTANCE: \n"
    typePreference=int(2)
    walk_test=0
    correct_test_walk=[]
    diference_distance=0
	#test n.11
    origin=Node(stationList[0],None)                # Massena L1
    destination=Node(stationList[0],origin)         # Massena L1
    origin.setHeuristic( typePreference, destination,city)
    diference_distance=diference_distance + abs(0 - origin.h)
    if origin.h <= 0:
		walk_test=walk_test+1
		correct_test_walk.append(11)
		print "             1 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             1 : " + str(origin.h) +  "    --> FAIL!"
	
	#test n.12
    origin=Node(stationList[0],None)                # Massena L1
    destination=Node(stationList[3],origin)         # Le Tonkin L2
    origin.setHeuristic( typePreference, destination,city)
    diference_distance=diference_distance + abs(166.5376 - origin.h)
    if origin.h<=166.5376:
		walk_test=walk_test+1 
		correct_test_walk.append(12)
		print "             2 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             2 : " + str(origin.h) +  "    --> FAIL!"
	
	#test n.13
    origin=Node(stationList[9],None)                # Charpennes L3
    destination=Node(stationList[2],origin)          # Republique L1
    origin.setHeuristic( typePreference, destination,city)
    diference_distance=diference_distance + abs(42.16026 - origin.h)
    if origin.h<=42.16026:
		walk_test=walk_test+1
		correct_test_walk.append(13)
		print "             3 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             3 : " + str(origin.h) +  "    --> FAIL!"
	
	#test n.14
    origin=Node(stationList[8],None)                # Part-Dieu Sirvent L2
    destination=Node(stationList[6],origin)         # Thiers La Fayete L2
    origin.setHeuristic( typePreference, destination,city)
    diference_distance=diference_distance + abs(119.75469 - origin.h)
    if origin.h<=119.75469:
		walk_test=walk_test+1
		correct_test_walk.append(14)
		print "             4 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             4 : " + str(origin.h) +  "    --> FAIL!"
	
    #test n.15
    origin=Node(stationList[11],None)                # Part-Dieu L3
    destination=Node(stationList[7],origin)          # Part-Dieu L2
    origin.setHeuristic( typePreference, destination,city)
    diference_distance=diference_distance + abs(0 - origin.h)
    if origin.h<=0:
		walk_test=walk_test+1
		correct_test_walk.append(15)
		print "             5 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             5 : " + str(origin.h) +  "    --> FAIL!"
	
	#test n.16
    origin=Node(stationList[5],None)                # College Bellecombe L2
    destination=Node(stationList[1],origin)         # Charpennes L1
    origin.setHeuristic( typePreference, destination,city)
    diference_distance=diference_distance + abs(100 - origin.h)
    if origin.h<=100.0000001:
		walk_test=walk_test+1
		correct_test_walk.append(16)
		print "             6 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             6 : " + str(origin.h) +  "    --> FAIL!"
		
	#test n.17
    origin=Node(stationList[13],None)                # Dauphine Lacasagne L4
    destination=Node(stationList[10],origin)         # Broteaux L3
    origin.setHeuristic( typePreference, destination,city)
    diference_distance=diference_distance + abs(182.1198 - origin.h)
    if origin.h<=182.1198:
		walk_test=walk_test+1
		correct_test_walk.append(17)
		print "             7 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             7 : " + str(origin.h) +  "    --> FAIL!"
	
	#test n.18
    origin=Node(stationList[12],None)               #Part-Dieu L4
    destination=Node(stationList[7],origin)         #part-Dieu L2
    origin.setHeuristic( typePreference, destination,city)
    diference_distance=diference_distance + abs(0 - origin.h)
    if origin.h<=0:
		walk_test=walk_test+1
		correct_test_walk.append(18)
		print "             8 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             8 : " + str(origin.h) +  "    --> FAIL!"
		
	#test n.19
    origin=Node(stationList[11],None)                #Part-Dieu L3
    destination=Node(stationList[9],origin)         #Charpennes L3
    origin.setHeuristic( typePreference, destination,city)
    diference_distance=diference_distance + abs(215.30896 - origin.h)
    if origin.h<=215.30896:
		walk_test=walk_test+1
		correct_test_walk.append(19)
		print "             9 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             9 : " + str(origin.h) +  "    --> FAIL!"
		
	#test n.20
    origin=Node(stationList[11],None)                #Part-Dieu L3
    destination=Node(stationList[1],origin)         #Charpennes L1
    origin.setHeuristic( typePreference, destination,city)
    diference_distance=diference_distance + abs(215.30896 - origin.h)
    if origin.h<=215.30896:
		walk_test=walk_test+1
		correct_test_walk.append(20)
		print "             10: " + str(origin.h)+  "    --> OK!"
    else:
		print "             10: " + str(origin.h) +  "    --> FAIL!"
	
	
    print "\n            test passed: " + str(walk_test) + " / 10" + "\n"
    print "             difference: " + str(diference_distance) + "\n"
	
	#............................................................................................"
	#test for TRANSFERS
    print "       TRANSFERS: \n"
    typePreference=int(3)
    transfers_test=0
    correct_test_transfers=[]
    diference_transfers=0
	
	#test n.21
    origin=Node(stationList[0],None)                # Massena L1
    destination=Node(stationList[0],origin)         # Massena L1
    origin.setHeuristic( typePreference, destination,city)
    diference_transfers=diference_transfers + abs(0 - origin.h)
    if origin.h <= 0:
		transfers_test=transfers_test+1
		correct_test_transfers.append(21)
		print "             1 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             1 : " + str(origin.h) +  "    --> FAIL!"
	
	#test n.22
    origin=Node(stationList[0],None)                # Massena L1
    destination=Node(stationList[3],origin)         # Le Tonkin L2
    origin.setHeuristic( typePreference, destination,city)
    diference_transfers=diference_transfers + abs(1 - origin.h)
    if origin.h<=1:
		transfers_test=transfers_test+1 
		correct_test_transfers.append(22)
		print "             2 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             2 : " + str(origin.h) +  "    --> FAIL!"
	
	#test n.23
    origin=Node(stationList[9],None)                # Charpennes L3
    destination=Node(stationList[2],origin)          # Republique L1
    origin.setHeuristic( typePreference, destination,city)
    diference_transfers=diference_transfers + abs(1 - origin.h)
    if origin.h<=1:
		transfers_test=transfers_test+1
		correct_test_transfers.append(23)
		print "             3 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             3 : " + str(origin.h) +  "    --> FAIL!"
	
	#test n.14
    origin=Node(stationList[8],None)                # Part-Dieu Sirvent L2
    destination=Node(stationList[6],origin)         # Thiers La Fayete L2
    origin.setHeuristic( typePreference, destination,city)
    diference_transfers=diference_transfers + abs(0 - origin.h)
    if origin.h<=0:
		transfers_test=transfers_test+1
		correct_test_transfers.append(24)
		print "             4 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             4 : " + str(origin.h) +  "    --> FAIL!"
	
    #test n.25
    origin=Node(stationList[11],None)                # Part-Dieu L3
    destination=Node(stationList[7],origin)          # Part-Dieu L2
    origin.setHeuristic( typePreference, destination,city)
    diference_transfers=diference_transfers + abs(1 - origin.h)
    if origin.h<=1:
		transfers_test=transfers_test+1
		correct_test_transfers.append(25)
		print "             5 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             5 : " + str(origin.h) +  "    --> FAIL!"
	
	#test n.26
    origin=Node(stationList[5],None)                # College Bellecombe L2
    destination=Node(stationList[1],origin)         # Charpennes L1
    origin.setHeuristic( typePreference, destination,city)
    diference_transfers=diference_transfers + abs(1 - origin.h)
    if origin.h<=1:
		transfers_test=transfers_test+1
		correct_test_transfers.append(26)
		print "             6 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             6 : " + str(origin.h) +  "    --> FAIL!"
		
	#test n.27
    origin=Node(stationList[13],None)                # Dauphine Lacasagne L4
    destination=Node(stationList[10],origin)         # Broteaux L3
    origin.setHeuristic( typePreference, destination,city)
    diference_transfers=diference_transfers + abs(1 - origin.h)
    if origin.h<=1:
		transfers_test=transfers_test+1
		correct_test_transfers.append(27)
		
		print "             7 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             7 : " + str(origin.h) +  "    --> FAIL!"
	
	#test n.28
    origin=Node(stationList[12],None)               #Part-Dieu L4
    destination=Node(stationList[7],origin)         #part-Dieu L2
    origin.setHeuristic( typePreference, destination,city)
    diference_transfers=diference_transfers + abs(1 - origin.h)
    if origin.h<=1:
		transfers_test=transfers_test+1
		correct_test_transfers.append(28)
		print "             8 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             8 : " + str(origin.h) +  "    --> FAIL!"
		
	#test n.29
    origin=Node(stationList[11],None)                #Part-Dieu L3
    destination=Node(stationList[9],origin)         #Charpennes L3
    origin.setHeuristic( typePreference, destination,city)
    diference_transfers=diference_transfers + abs(0 - origin.h)
    if origin.h<=0:
		transfers_test=transfers_test+1
		correct_test_transfers.append(29)
		print "             9 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             9 : " + str(origin.h) +  "    --> FAIL!"
		
	#test n.30
    origin=Node(stationList[13],None)               #Dauphine Lacasagne L3
    destination=Node(stationList[0],origin)         #Massena L1
    origin.setHeuristic( typePreference, destination,city)
    diference_transfers=diference_transfers + abs(2 - origin.h)
    if origin.h<=2:
		transfers_test=transfers_test+1
		correct_test_transfers.append(30)
		print "             10: " + str(origin.h)+  "    --> OK!"
    else:
		print "             10: " + str(origin.h) +  "    --> FAIL!"		
		
	
    print "\n            test passed: " + str(transfers_test) + " / 10" + "\n"
    print "             difference: " + str(diference_transfers) + "\n"
	
	#............................................................................................"
	#test for STOP STATIONS
    print "       STOP STATION: \n"
   
    typePreference=int(4)
    stopStation_test=0
    correct_test_stopStation=[]
    diference_stopStation=0
	#test n.31
    origin=Node(stationList[0],None)                # Massena L1
    destination=Node(stationList[0],origin)         # Massena L1
    origin.setHeuristic( typePreference, destination,city)
    diference_stopStation=diference_stopStation + abs(0 - origin.h)
    if origin.h <= 0:
		stopStation_test=stopStation_test+1
		correct_test_stopStation.append(31)
		print "             1 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             1 : " + str(origin.h) +  "    --> FAIL!"
	
	#test n.32
    origin=Node(stationList[0],None)                # Massena L1
    destination=Node(stationList[3],origin)         # Le Tonkin L2
    origin.setHeuristic( typePreference, destination,city)
    diference_stopStation=diference_stopStation + abs(2 - origin.h)
    if origin.h<=2:
		stopStation_test=stopStation_test+1 
		correct_test_stopStation.append(32)
		print "             2 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             2 : " + str(origin.h) +  "    --> FAIL!"
	
	#test n.33
    origin=Node(stationList[9],None)                # Charpennes L3
    destination=Node(stationList[2],origin)          # Republique L1
    origin.setHeuristic( typePreference, destination,city)
    diference_stopStation=diference_stopStation + abs(1 - origin.h)
    if origin.h<=1:
		stopStation_test=stopStation_test+1
		correct_test_stopStation.append(33)
		print "             3 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             3 : " + str(origin.h) +  "    --> FAIL!"
	
	#test n.34
    origin=Node(stationList[8],None)                # Part-Dieu Sirvent L2
    destination=Node(stationList[6],origin)         # Thiers La Fayete L2
    origin.setHeuristic( typePreference, destination,city)
    diference_stopStation=diference_stopStation + abs(2 - origin.h)
    if origin.h<=2:
		stopStation_test=stopStation_test+1
		correct_test_stopStation.append(24)
		print "             4 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             4 : " + str(origin.h) +  "    --> FAIL!"
	
    #test n.35
    origin=Node(stationList[11],None)                # Part-Dieu L3
    destination=Node(stationList[7],origin)          # Part-Dieu L2
    origin.setHeuristic( typePreference, destination,city)
    diference_stopStation=diference_stopStation + abs(0 - origin.h)
    if origin.h<=0:
		stopStation_test=stopStation_test+1
		correct_test_stopStation.append(35)
		print "             5 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             5 : " + str(origin.h) +  "    --> FAIL!"
	
	#test n.36
    origin=Node(stationList[5],None)                # College Bellecombe L2
    destination=Node(stationList[1],origin)         # Charpennes L1
    origin.setHeuristic( typePreference, destination,city)
    diference_stopStation=diference_stopStation + abs(1 - origin.h)
    if origin.h<=1:
		stopStation_test=stopStation_test+1
		correct_test_stopStation.append(36)
		print "             6 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             6 : " + str(origin.h) +  "    --> FAIL!"
		
	#test n.37
    origin=Node(stationList[13],None)                # Dauphine Lacasagne L4
    destination=Node(stationList[10],origin)         # Broteaux L3
    origin.setHeuristic( typePreference, destination,city)
    diference_stopStation=diference_stopStation + abs(2 - origin.h)
    if origin.h<=2:
		stopStation_test=stopStation_test+1
		correct_test_stopStation.append(37)
		print "             7 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             7 : " + str(origin.h) +  "    --> FAIL!"
	
	#test n.28
    origin=Node(stationList[12],None)               #Part-Dieu L4
    destination=Node(stationList[7],origin)         #part-Dieu L2
    origin.setHeuristic( typePreference, destination,city)
    diference_stopStation=diference_stopStation + abs(0 - origin.h)
    if origin.h<=0:
		stopStation_test=stopStation_test+1
		correct_test_stopStation.append(38)
		print "             8 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             8 : " + str(origin.h) +  "    --> FAIL!"
		
	#test n.39
    origin=Node(stationList[11],None)                #Part-Dieu L3
    destination=Node(stationList[9],origin)         #Charpennes L3
    origin.setHeuristic( typePreference, destination,city)
    diference_stopStation=diference_stopStation + abs(2 - origin.h)
    if origin.h<=2:
		stopStation_test=stopStation_test+1
		correct_test_stopStation.append(39)
		print "             9 : " + str(origin.h)+  "    --> OK!"
    else:
		print "             9 : " + str(origin.h) +  "    --> FAIL!"
		
	#test n.40
    origin=Node(stationList[13],None)               #Dauphine Lacasagne L3
    destination=Node(stationList[0],origin)         #Massena L1
    origin.setHeuristic( typePreference, destination,city)
    diference_stopStation=diference_stopStation + abs(4 - origin.h)
    if origin.h<=4:
		stopStation_test=stopStation_test+1
		correct_test_stopStation.append(40)
		print "             10: " + str(origin.h)+  "    --> OK!"
    else:
		print "             1: " + str(origin.h) +  "    --> FAIL!"		
	
    print "                     OK: " + str(correct_test_stopStation) + "\n"
    print "            test passed: " + str(stopStation_test) + " / 10" + "\n"
    print "             difference: " + str(diference_stopStation) + "\n"
    
  
    
    
    print "\n *********** Make sure you have passed all the tests."
    print "               As lower is the 'difference' value, much better is your heuristic (in the same type of preference)"
    print "               Prove different heuristics for each type of preference and keep the best one."
    print "               Nevertheless, if you get a difference of 0 probably you have wrongly understood what is an heuristic\n \n"
    #------------------------------------------------------------------#
	
if __name__ == '__main__':
    main()