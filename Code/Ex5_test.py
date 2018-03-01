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
	
	
    origin1=Node(stationList[0],None)                 				# Massena L1
    destination_tmp_1_1=Node(stationList[1],origin1)     			# Charpenes L1
    destination1=Node(stationList[2],destination_tmp_1_1)			# Republique L1
	
    origin2=Node(stationList[3], None)                				# Le Tonkin L2
    destination_tmp_2_1=Node(stationList[4],origin2)      			# Charpennes L2
    destination_tmp_2_2=Node(stationList[5],destination_tmp_2_1) 	# College Bellecombe L2
    destination_tmp_2_3=Node(stationList[6],destination_tmp_2_2) 	# Thiers Lafayette L2
    destination_tmp_2_4=Node(stationList[7],destination_tmp_2_3) 	# Part-Dieu L2
    destination2=Node(stationList[8],destination_tmp_2_4)    		# Part-Dieu Sirvent L2
	
    origin3=Node(stationList[9],None) 								# Charpennes L3
    destination_tmp_3_1=Node(stationList[10],origin3) 				# Brotteaux L3
    destination3=Node(stationList[11],destination_tmp_3_1)			# Part-Dieu L3
	
    origin4=Node(stationList[12],None) 								# Part-Dieu L4
    destination4=Node(stationList[13],origin4) 						# Dauphhine Lacassagne L4
	
    origin5=Node(stationList[3], None)                				# Le Tonkin L2
    destination_tmp_5_1=Node(stationList[4],origin5)      			# Charpennes L2
    destination_tmp_5_2=Node(stationList[9],destination_tmp_5_1) 	# Charpennes L3
    destination5=Node(stationList[10],destination_tmp_5_2) 			# Brotteaux L3
	
    origin6=Node(stationList[8],None)				    			# Part-Dieu Sirvent L2
    destination_tmp_6_1=Node(stationList[7],origin6) 				# Part-Dieu L2
    destination_tmp_6_2=Node(stationList[6],destination_tmp_6_1) 	# Thiers Lafayette L2
    destination_tmp_6_3=Node(stationList[5],destination_tmp_6_2) 	# College Bellecombe L2
    destination_tmp_6_4=Node(stationList[4],destination_tmp_6_3)	# Charpennes L2
    destination_tmp_6_5=Node(stationList[9],destination_tmp_6_4) 	# Charpennes L3
    destination6=Node(stationList[10],destination_tmp_6_5)			# Brotteaux L3
	
    origin7=Node(stationList[13],None)								# Dauphhine Lacassagne L4
    destination_tmp_7_1=Node(stationList[12],origin7) 				# Part-Dieu L4
    destination_tmp_7_2=Node(stationList[7],destination_tmp_7_1) 	# Part-Dieu L2
    destination7=Node(stationList[8],destination_tmp_7_2)	   		# Part-Dieu Sirvent L2
	
    origin8=Node(stationList[5],None) 								# College Bellecombe L2
    destination_tmp_8_1=Node(stationList[4],origin8)				# Charpennes L2
    destination_tmp_8_2=Node(stationList[1],destination_tmp_8_1) 	# Charpenes L1
    destination8=Node(stationList[2],destination_tmp_8_2)			# Republique L1
	
    origin9=Node(stationList[10],None) 								# Brotteaux L3
    destination_tmp_9_1=Node(stationList[9],origin9) 				# Charpennes L3
    destination_tmp_9_2=Node(stationList[1],destination_tmp_9_1) 	# Charpenes L1
    destination9=Node(stationList[0],destination_tmp_9_2)    		# Massena L1
	
    origin10=Node(stationList[2],None)								# Republique L1
    destination_tmp_10_1=Node(stationList[1],origin10) 				# Charpenes L1
    destination_tmp_10_2=Node(stationList[4],destination_tmp_10_1)	# Charpennes L2
    destination_tmp_10_3=Node(stationList[5],destination_tmp_10_2)	# College Bellecombe L2
    destination_tmp_10_4=Node(stationList[6],destination_tmp_10_3) 	# Thiers Lafayette L2
    destination_tmp_10_5=Node(stationList[7],destination_tmp_10_4)	# Part-Dieu L2
    destination_tmp_10_6=Node(stationList[11],destination_tmp_10_5)	# Part-Dieu L3
    destination_tmp_10_7=Node(stationList[10],destination_tmp_10_6)	# Brotteaux L3
    destination_tmp_10_8=Node(stationList[9],destination_tmp_10_7)	# Charpennes L3
    destination_tmp_10_9=Node(stationList[4],destination_tmp_10_8)	# Charpennes L2
    destination10=Node(stationList[3], destination_tmp_10_9) 		# Le Tonkin L2
	
	
	
	
    print " \n\n\n___________ test EX 5 : EXPAND _______________________\n"
	
	
	#test for time
    print "       TIME: \n"
    typePreference=int(1)
    currentCostTable=setCostTable( typePreference, stationList,city)
	
    destination_tmp_1_1.setHeuristic(typePreference,destination1,city)
    destination_tmp_1_1.setRealCost(currentCostTable)
    destination_tmp_1_1.setEvaluation()
    eval_tmp=Expand(destination_tmp_1_1, stationList, typePreference, destination1, currentCostTable, city)
    eval1=[]
    for i in range(0,len(eval_tmp)):
		eval1.append(eval_tmp[i].station.id)
    eval1.sort()
	
    destination_tmp_2_1.setRealCost(currentCostTable)
    destination_tmp_2_2.setRealCost(currentCostTable)
    destination_tmp_2_2.setHeuristic(typePreference,destination2,city)
    destination_tmp_2_2.setEvaluation()
    eval_tmp=Expand(destination_tmp_2_2, stationList, typePreference, destination2, currentCostTable, city)
    eval2=[]
    for i in range(0,len(eval_tmp)):
		eval2.append(eval_tmp[i].station.id)
    eval2.sort()
	
    origin3.setRealCost(currentCostTable)
    origin3.setHeuristic(typePreference,destination3,city)
    origin3.setEvaluation()
    eval_tmp=Expand(origin3, stationList, typePreference, destination3, currentCostTable, city)
    eval3=[]
    for i in range(0,len(eval_tmp)):
		eval3.append(eval_tmp[i].station.id)
    eval3.sort()
	
    origin4.setRealCost(currentCostTable)
    origin4.setHeuristic(typePreference,destination4,city)
    origin4.setEvaluation()
    eval_tmp=Expand(origin4, stationList, typePreference, destination4, currentCostTable, city)
    eval4=[]
    for i in range(0,len(eval_tmp)):
		eval4.append(eval_tmp[i].station.id)
    eval4.sort()
	
    destination_tmp_5_1.setRealCost(currentCostTable)
    destination_tmp_5_1.setHeuristic(typePreference,destination5,city)
    destination_tmp_5_1.setEvaluation()
    eval_tmp=Expand(destination_tmp_5_1, stationList, typePreference, destination5, currentCostTable, city)
    eval5=[]
    for i in range(0,len(eval_tmp)):
		eval5.append(eval_tmp[i].station.id)
    eval5.sort()
	
    destination_tmp_6_1.setRealCost(currentCostTable)
    destination_tmp_6_2.setRealCost(currentCostTable)
    destination_tmp_6_3.setRealCost(currentCostTable)
    destination_tmp_6_3.setHeuristic(typePreference,destination6,city)
    destination_tmp_6_3.setEvaluation()
    eval_tmp=Expand(destination_tmp_6_3, stationList, typePreference, destination6, currentCostTable, city)
    eval6=[]
    for i in range(0,len(eval_tmp)):
		eval6.append(eval_tmp[i].station.id)
    eval6.sort()
	
    destination_tmp_7_1.setRealCost(currentCostTable)
    destination_tmp_7_2.setRealCost(currentCostTable)
    destination_tmp_7_2.setHeuristic(typePreference,destination7,city)
    destination_tmp_7_2.setEvaluation()
    eval_tmp=Expand(destination_tmp_7_2, stationList, typePreference, destination7, currentCostTable, city)
    eval7=[]
    for i in range(0,len(eval_tmp)):
		eval7.append(eval_tmp[i].station.id)
    eval7.sort()
	
    destination_tmp_8_1.setRealCost(currentCostTable)
    destination_tmp_8_1.setHeuristic(typePreference,destination8,city)
    destination_tmp_8_1.setEvaluation()
    eval_tmp=Expand(destination_tmp_8_1, stationList, typePreference, destination8, currentCostTable, city)
    eval8=[]
    for i in range(0,len(eval_tmp)):
		eval8.append(eval_tmp[i].station.id)
    eval8.sort()
	
    destination_tmp_9_1.setRealCost(currentCostTable)
    destination_tmp_9_2.setRealCost(currentCostTable)
    destination_tmp_9_2.setHeuristic(typePreference,destination9,city)
    destination_tmp_9_2.setEvaluation()
    eval_tmp=Expand(destination_tmp_9_2, stationList, typePreference, destination9, currentCostTable, city)
    eval9=[]
    for i in range(0,len(eval_tmp)):
		eval9.append(eval_tmp[i].station.id)
    eval9.sort()
	
    destination_tmp_10_1.setRealCost(currentCostTable)
    destination_tmp_10_2.setRealCost(currentCostTable)
    destination_tmp_10_3.setRealCost(currentCostTable)
    destination_tmp_10_4.setRealCost(currentCostTable)
    destination_tmp_10_5.setRealCost(currentCostTable)
    destination_tmp_10_6.setRealCost(currentCostTable)
    destination_tmp_10_7.setRealCost(currentCostTable)
    destination_tmp_10_8.setRealCost(currentCostTable)
    destination_tmp_10_9.setRealCost(currentCostTable)
    destination_tmp_10_9.setHeuristic(typePreference,destination10,city)
    destination_tmp_10_9.setEvaluation()
    eval_tmp=Expand(destination_tmp_10_9, stationList, typePreference, destination10, currentCostTable, city)
    eval10=[]
    for i in range(0,len(eval_tmp)):
		eval10.append(eval_tmp[i].station.id)
    eval10.sort()
	
    test_ok=0
    if eval1 == [1,3,5,10]:
		print "             1  : " + str(eval1) +  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             1  : " + str(eval1) +  "    --> FAIL!"	
	
    if eval2 == [5,7]:
		print "             2  : " + str(eval2)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             2  : " + str(eval2) +  "    --> FAIL!"	
		
    if eval3 == [2,5,11]:
		print "             3  : " + str(eval3)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             3  : " + str(eval3) +  "    --> FAIL!"	
	
    if eval4==[8,12,14]:
		print "             4  : " + str(eval4)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             4  : " + str(eval4) +  "    --> FAIL!"	
		
    if eval5 == [2,4,6,10]:
		print "             5  : " + str(eval5)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             5  : " + str(eval5) +  "    --> FAIL!"	
	
	
    if eval6 == [5,7]:
		print "             6  : " + str(eval6)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             6  : " + str(eval6) +  "    --> FAIL!"	
	
    if eval7 == [7,9,12,13]:
		print "             7  : " + str(eval7)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             7  : " + str(eval7) +  "    --> FAIL!"	

    if eval8 == [2,4,6,10]:
		print "             8  : " + str(eval8)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             8  : " + str(eval8) +  "    --> FAIL!"	
		
    if eval9 ==[1,3,5,10]:
		print "             9  : " + str(eval9)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             9  : " + str(eval9) +  "    --> FAIL!"	
	
    if eval10 ==[2,4,6,10]:
		print "             10 : " + str(eval10)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             10 : " + str(eval10) +  "    --> FAIL!"

    print "\n                   Test Passed : " + str(test_ok) + " / 10 \n"
	
	
	
	
	#.....................................................................................................
	#test for distance
    print "       DISTANCE: \n"
    typePreference=int(2)
    currentCostTable=setCostTable( typePreference, stationList,city)
	
    destination_tmp_1_1.setHeuristic(typePreference,destination1,city)
    destination_tmp_1_1.setRealCost(currentCostTable)
    destination_tmp_1_1.setEvaluation()
    eval_tmp=Expand(destination_tmp_1_1, stationList, typePreference, destination1, currentCostTable, city)
    eval1=[]
    for i in range(0,len(eval_tmp)):
		eval1.append(eval_tmp[i].station.id)
    eval1.sort()
	
    destination_tmp_2_1.setRealCost(currentCostTable)
    destination_tmp_2_2.setRealCost(currentCostTable)
    destination_tmp_2_2.setHeuristic(typePreference,destination2,city)
    destination_tmp_2_2.setEvaluation()
    eval_tmp=Expand(destination_tmp_2_2, stationList, typePreference, destination2, currentCostTable, city)
    eval2=[]
    for i in range(0,len(eval_tmp)):
		eval2.append(eval_tmp[i].station.id)
    eval2.sort()
	
    origin3.setRealCost(currentCostTable)
    origin3.setHeuristic(typePreference,destination3,city)
    origin3.setEvaluation()
    eval_tmp=Expand(origin3, stationList, typePreference, destination3, currentCostTable, city)
    eval3=[]
    for i in range(0,len(eval_tmp)):
		eval3.append(eval_tmp[i].station.id)
    eval3.sort()
	
    origin4.setRealCost(currentCostTable)
    origin4.setHeuristic(typePreference,destination4,city)
    origin4.setEvaluation()
    eval_tmp=Expand(origin4, stationList, typePreference, destination4, currentCostTable, city)
    eval4=[]
    for i in range(0,len(eval_tmp)):
		eval4.append(eval_tmp[i].station.id)
    eval4.sort()
	
    destination_tmp_5_1.setRealCost(currentCostTable)
    destination_tmp_5_1.setHeuristic(typePreference,destination5,city)
    destination_tmp_5_1.setEvaluation()
    eval_tmp=Expand(destination_tmp_5_1, stationList, typePreference, destination5, currentCostTable, city)
    eval5=[]
    for i in range(0,len(eval_tmp)):
		eval5.append(eval_tmp[i].station.id)
    eval5.sort()
	
    destination_tmp_6_1.setRealCost(currentCostTable)
    destination_tmp_6_2.setRealCost(currentCostTable)
    destination_tmp_6_3.setRealCost(currentCostTable)
    destination_tmp_6_3.setHeuristic(typePreference,destination6,city)
    destination_tmp_6_3.setEvaluation()
    eval_tmp=Expand(destination_tmp_6_3, stationList, typePreference, destination6, currentCostTable, city)
    eval6=[]
    for i in range(0,len(eval_tmp)):
		eval6.append(eval_tmp[i].station.id)
    eval6.sort()
	
    destination_tmp_7_1.setRealCost(currentCostTable)
    destination_tmp_7_2.setRealCost(currentCostTable)
    destination_tmp_7_2.setHeuristic(typePreference,destination7,city)
    destination_tmp_7_2.setEvaluation()
    eval_tmp=Expand(destination_tmp_7_2, stationList, typePreference, destination7, currentCostTable, city)
    eval7=[]
    for i in range(0,len(eval_tmp)):
		eval7.append(eval_tmp[i].station.id)
    eval7.sort()
	
    destination_tmp_8_1.setRealCost(currentCostTable)
    destination_tmp_8_1.setHeuristic(typePreference,destination8,city)
    destination_tmp_8_1.setEvaluation()
    eval_tmp=Expand(destination_tmp_8_1, stationList, typePreference, destination8, currentCostTable, city)
    eval8=[]
    for i in range(0,len(eval_tmp)):
		eval8.append(eval_tmp[i].station.id)
    eval8.sort()
	
    destination_tmp_9_1.setRealCost(currentCostTable)
    destination_tmp_9_2.setRealCost(currentCostTable)
    destination_tmp_9_2.setHeuristic(typePreference,destination9,city)
    destination_tmp_9_2.setEvaluation()
    eval_tmp=Expand(destination_tmp_9_2, stationList, typePreference, destination9, currentCostTable, city)
    eval9=[]
    for i in range(0,len(eval_tmp)):
		eval9.append(eval_tmp[i].station.id)
    eval9.sort()
	
    destination_tmp_10_1.setRealCost(currentCostTable)
    destination_tmp_10_2.setRealCost(currentCostTable)
    destination_tmp_10_3.setRealCost(currentCostTable)
    destination_tmp_10_4.setRealCost(currentCostTable)
    destination_tmp_10_5.setRealCost(currentCostTable)
    destination_tmp_10_6.setRealCost(currentCostTable)
    destination_tmp_10_7.setRealCost(currentCostTable)
    destination_tmp_10_8.setRealCost(currentCostTable)
    destination_tmp_10_9.setRealCost(currentCostTable)
    destination_tmp_10_9.setHeuristic(typePreference,destination10,city)
    destination_tmp_10_9.setEvaluation()
    eval_tmp=Expand(destination_tmp_10_9, stationList, typePreference, destination10, currentCostTable, city)
    eval10=[]
    for i in range(0,len(eval_tmp)):
		eval10.append(eval_tmp[i].station.id)
    eval10.sort()
	
    test_ok=0
    if eval1 == [1,3,5,10]:
		print "             1  : " + str(eval1) +  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             1  : " + str(eval1) +  "    --> FAIL!"	
	
    if eval2 == [5,7]:
		print "             2  : " + str(eval2)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             2  : " + str(eval2) +  "    --> FAIL!"	
		
    if eval3 == [2,5,11]:
		print "             3  : " + str(eval3)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             3  : " + str(eval3) +  "    --> FAIL!"	
	
    if eval4==[8,12,14]:
		print "             4  : " + str(eval4)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             4  : " + str(eval4) +  "    --> FAIL!"	
		
    if eval5 == [2,4,6,10]:
		print "             5  : " + str(eval5)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             5  : " + str(eval5) +  "    --> FAIL!"	
	
	
    if eval6 == [5,7]:
		print "             6  : " + str(eval6)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             6  : " + str(eval6) +  "    --> FAIL!"	
	
    if eval7 == [7,9,12,13]:
		print "             7  : " + str(eval7)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             7  : " + str(eval7) +  "    --> FAIL!"	

    if eval8 == [2,4,6,10]:
		print "             8  : " + str(eval8)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             8  : " + str(eval8) +  "    --> FAIL!"	
		
    if eval9 ==[1,3,5,10]:
		print "             9  : " + str(eval9)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             9  : " + str(eval9) +  "    --> FAIL!"	
	
    if eval10 ==[2,4,6,10]:
		print "             10 : " + str(eval10)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             10 : " + str(eval10) +  "    --> FAIL!"

    print "\n                   Test Passed : " + str(test_ok) + " / 10 \n"
	
	
	
	#.....................................................................................................
	#test for TRANSFERS
    print "       TRANSFERS: \n"
    typePreference=int(3)
    currentCostTable=setCostTable( typePreference, stationList,city)
	
    destination_tmp_1_1.setHeuristic(typePreference,destination1,city)
    destination_tmp_1_1.setRealCost(currentCostTable)
    destination_tmp_1_1.setEvaluation()
    eval_tmp=Expand(destination_tmp_1_1, stationList, typePreference, destination1, currentCostTable, city)
    eval1=[]
    for i in range(0,len(eval_tmp)):
		eval1.append(eval_tmp[i].station.id)
    eval1.sort()
	
    destination_tmp_2_1.setRealCost(currentCostTable)
    destination_tmp_2_2.setRealCost(currentCostTable)
    destination_tmp_2_2.setHeuristic(typePreference,destination2,city)
    destination_tmp_2_2.setEvaluation()
    eval_tmp=Expand(destination_tmp_2_2, stationList, typePreference, destination2, currentCostTable, city)
    eval2=[]
    for i in range(0,len(eval_tmp)):
		eval2.append(eval_tmp[i].station.id)
    eval2.sort()
	
    origin3.setRealCost(currentCostTable)
    origin3.setHeuristic(typePreference,destination3,city)
    origin3.setEvaluation()
    eval_tmp=Expand(origin3, stationList, typePreference, destination3, currentCostTable, city)
    eval3=[]
    for i in range(0,len(eval_tmp)):
		eval3.append(eval_tmp[i].station.id)
    eval3.sort()
	
    origin4.setRealCost(currentCostTable)
    origin4.setHeuristic(typePreference,destination4,city)
    origin4.setEvaluation()
    eval_tmp=Expand(origin4, stationList, typePreference, destination4, currentCostTable, city)
    eval4=[]
    for i in range(0,len(eval_tmp)):
		eval4.append(eval_tmp[i].station.id)
    eval4.sort()
	
    destination_tmp_5_1.setRealCost(currentCostTable)
    destination_tmp_5_1.setHeuristic(typePreference,destination5,city)
    destination_tmp_5_1.setEvaluation()
    eval_tmp=Expand(destination_tmp_5_1, stationList, typePreference, destination5, currentCostTable, city)
    eval5=[]
    for i in range(0,len(eval_tmp)):
		eval5.append(eval_tmp[i].station.id)
    eval5.sort()
	
    destination_tmp_6_1.setRealCost(currentCostTable)
    destination_tmp_6_2.setRealCost(currentCostTable)
    destination_tmp_6_3.setRealCost(currentCostTable)
    destination_tmp_6_3.setHeuristic(typePreference,destination6,city)
    destination_tmp_6_3.setEvaluation()
    eval_tmp=Expand(destination_tmp_6_3, stationList, typePreference, destination6, currentCostTable, city)
    eval6=[]
    for i in range(0,len(eval_tmp)):
		eval6.append(eval_tmp[i].station.id)
    eval6.sort()
	
    destination_tmp_7_1.setRealCost(currentCostTable)
    destination_tmp_7_2.setRealCost(currentCostTable)
    destination_tmp_7_2.setHeuristic(typePreference,destination7,city)
    destination_tmp_7_2.setEvaluation()
    eval_tmp=Expand(destination_tmp_7_2, stationList, typePreference, destination7, currentCostTable, city)
    eval7=[]
    for i in range(0,len(eval_tmp)):
		eval7.append(eval_tmp[i].station.id)
    eval7.sort()
	
    destination_tmp_8_1.setRealCost(currentCostTable)
    destination_tmp_8_1.setHeuristic(typePreference,destination8,city)
    destination_tmp_8_1.setEvaluation()
    eval_tmp=Expand(destination_tmp_8_1, stationList, typePreference, destination8, currentCostTable, city)
    eval8=[]
    for i in range(0,len(eval_tmp)):
		eval8.append(eval_tmp[i].station.id)
    eval8.sort()
	
    destination_tmp_9_1.setRealCost(currentCostTable)
    destination_tmp_9_2.setRealCost(currentCostTable)
    destination_tmp_9_2.setHeuristic(typePreference,destination9,city)
    destination_tmp_9_2.setEvaluation()
    eval_tmp=Expand(destination_tmp_9_2, stationList, typePreference, destination9, currentCostTable, city)
    eval9=[]
    for i in range(0,len(eval_tmp)):
		eval9.append(eval_tmp[i].station.id)
    eval9.sort()
	
    destination_tmp_10_1.setRealCost(currentCostTable)
    destination_tmp_10_2.setRealCost(currentCostTable)
    destination_tmp_10_3.setRealCost(currentCostTable)
    destination_tmp_10_4.setRealCost(currentCostTable)
    destination_tmp_10_5.setRealCost(currentCostTable)
    destination_tmp_10_6.setRealCost(currentCostTable)
    destination_tmp_10_7.setRealCost(currentCostTable)
    destination_tmp_10_8.setRealCost(currentCostTable)
    destination_tmp_10_9.setRealCost(currentCostTable)
    destination_tmp_10_9.setHeuristic(typePreference,destination10,city)
    destination_tmp_10_9.setEvaluation()
    eval_tmp=Expand(destination_tmp_10_9, stationList, typePreference, destination10, currentCostTable, city)
    eval10=[]
    for i in range(0,len(eval_tmp)):
		eval10.append(eval_tmp[i].station.id)
    eval10.sort()
	
    test_ok=0
    if eval1 == [1,3,5,10]:
		print "             1  : " + str(eval1) +  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             1  : " + str(eval1) +  "    --> FAIL!"	
	
    if eval2 == [5,7]:
		print "             2  : " + str(eval2)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             2  : " + str(eval2) +  "    --> FAIL!"	
		
    if eval3 == [2,5,11]:
		print "             3  : " + str(eval3)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             3  : " + str(eval3) +  "    --> FAIL!"	
	
    if eval4==[8,12,14]:
		print "             4  : " + str(eval4)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             4  : " + str(eval4) +  "    --> FAIL!"	
		
    if eval5 == [2,4,6,10]:
		print "             5  : " + str(eval5)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             5  : " + str(eval5) +  "    --> FAIL!"	
	
	
    if eval6 == [5,7]:
		print "             6  : " + str(eval6)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             6  : " + str(eval6) +  "    --> FAIL!"	
	
    if eval7 == [7,9,12,13]:
		print "             7  : " + str(eval7)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             7  : " + str(eval7) +  "    --> FAIL!"	

    if eval8 == [2,4,6,10]:
		print "             8  : " + str(eval8)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             8  : " + str(eval8) +  "    --> FAIL!"	
		
    if eval9 ==[1,3,5,10]:
		print "             9  : " + str(eval9)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             9  : " + str(eval9) +  "    --> FAIL!"	
	
    if eval10 ==[2,4,6,10]:
		print "             10 : " + str(eval10)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             10 : " + str(eval10) +  "    --> FAIL!"

    print "\n                   Test Passed : " + str(test_ok) + " / 10 \n"
	
    
	
	#.....................................................................................................
		#test for stop Stations
    print "       STOP STATIONS: \n"
    typePreference=int(4)
    currentCostTable=setCostTable( typePreference, stationList,city)
	
    destination_tmp_1_1.setHeuristic(typePreference,destination1,city)
    destination_tmp_1_1.setRealCost(currentCostTable)
    destination_tmp_1_1.setEvaluation()
    eval_tmp=Expand(destination_tmp_1_1, stationList, typePreference, destination1, currentCostTable, city)
    eval1=[]
    for i in range(0,len(eval_tmp)):
		eval1.append(eval_tmp[i].station.id)
    eval1.sort()
	
    destination_tmp_2_1.setRealCost(currentCostTable)
    destination_tmp_2_2.setRealCost(currentCostTable)
    destination_tmp_2_2.setHeuristic(typePreference,destination2,city)
    destination_tmp_2_2.setEvaluation()
    eval_tmp=Expand(destination_tmp_2_2, stationList, typePreference, destination2, currentCostTable, city)
    eval2=[]
    for i in range(0,len(eval_tmp)):
		eval2.append(eval_tmp[i].station.id)
    eval2.sort()
	
    origin3.setRealCost(currentCostTable)
    origin3.setHeuristic(typePreference,destination3,city)
    origin3.setEvaluation()
    eval_tmp=Expand(origin3, stationList, typePreference, destination3, currentCostTable, city)
    eval3=[]
    for i in range(0,len(eval_tmp)):
		eval3.append(eval_tmp[i].station.id)
    eval3.sort()
	
    origin4.setRealCost(currentCostTable)
    origin4.setHeuristic(typePreference,destination4,city)
    origin4.setEvaluation()
    eval_tmp=Expand(origin4, stationList, typePreference, destination4, currentCostTable, city)
    eval4=[]
    for i in range(0,len(eval_tmp)):
		eval4.append(eval_tmp[i].station.id)
    eval4.sort()
	
    destination_tmp_5_1.setRealCost(currentCostTable)
    destination_tmp_5_1.setHeuristic(typePreference,destination5,city)
    destination_tmp_5_1.setEvaluation()
    eval_tmp=Expand(destination_tmp_5_1, stationList, typePreference, destination5, currentCostTable, city)
    eval5=[]
    for i in range(0,len(eval_tmp)):
		eval5.append(eval_tmp[i].station.id)
    eval5.sort()
	
    destination_tmp_6_1.setRealCost(currentCostTable)
    destination_tmp_6_2.setRealCost(currentCostTable)
    destination_tmp_6_3.setRealCost(currentCostTable)
    destination_tmp_6_3.setHeuristic(typePreference,destination6,city)
    destination_tmp_6_3.setEvaluation()
    eval_tmp=Expand(destination_tmp_6_3, stationList, typePreference, destination6, currentCostTable, city)
    eval6=[]
    for i in range(0,len(eval_tmp)):
		eval6.append(eval_tmp[i].station.id)
    eval6.sort()
	
    destination_tmp_7_1.setRealCost(currentCostTable)
    destination_tmp_7_2.setRealCost(currentCostTable)
    destination_tmp_7_2.setHeuristic(typePreference,destination7,city)
    destination_tmp_7_2.setEvaluation()
    eval_tmp=Expand(destination_tmp_7_2, stationList, typePreference, destination7, currentCostTable, city)
    eval7=[]
    for i in range(0,len(eval_tmp)):
		eval7.append(eval_tmp[i].station.id)
    eval7.sort()
	
    destination_tmp_8_1.setRealCost(currentCostTable)
    destination_tmp_8_1.setHeuristic(typePreference,destination8,city)
    destination_tmp_8_1.setEvaluation()
    eval_tmp=Expand(destination_tmp_8_1, stationList, typePreference, destination8, currentCostTable, city)
    eval8=[]
    for i in range(0,len(eval_tmp)):
		eval8.append(eval_tmp[i].station.id)
    eval8.sort()
	
    destination_tmp_9_1.setRealCost(currentCostTable)
    destination_tmp_9_2.setRealCost(currentCostTable)
    destination_tmp_9_2.setHeuristic(typePreference,destination9,city)
    destination_tmp_9_2.setEvaluation()
    eval_tmp=Expand(destination_tmp_9_2, stationList, typePreference, destination9, currentCostTable, city)
    eval9=[]
    for i in range(0,len(eval_tmp)):
		eval9.append(eval_tmp[i].station.id)
    eval9.sort()
	
    destination_tmp_10_1.setRealCost(currentCostTable)
    destination_tmp_10_2.setRealCost(currentCostTable)
    destination_tmp_10_3.setRealCost(currentCostTable)
    destination_tmp_10_4.setRealCost(currentCostTable)
    destination_tmp_10_5.setRealCost(currentCostTable)
    destination_tmp_10_6.setRealCost(currentCostTable)
    destination_tmp_10_7.setRealCost(currentCostTable)
    destination_tmp_10_8.setRealCost(currentCostTable)
    destination_tmp_10_9.setRealCost(currentCostTable)
    destination_tmp_10_9.setHeuristic(typePreference,destination10,city)
    destination_tmp_10_9.setEvaluation()
    eval_tmp=Expand(destination_tmp_10_9, stationList, typePreference, destination10, currentCostTable, city)
    eval10=[]
    for i in range(0,len(eval_tmp)):
		eval10.append(eval_tmp[i].station.id)
    eval10.sort()
	
    test_ok=0
    if eval1 == [1,3,5,10]:
		print "             1  : " + str(eval1) +  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             1  : " + str(eval1) +  "    --> FAIL!"	
	
    if eval2 == [5,7]:
		print "             2  : " + str(eval2)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             2  : " + str(eval2) +  "    --> FAIL!"	
		
    if eval3 == [2,5,11]:
		print "             3  : " + str(eval3)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             3  : " + str(eval3) +  "    --> FAIL!"	
	
    if eval4==[8,12,14]:
		print "             4  : " + str(eval4)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             4  : " + str(eval4) +  "    --> FAIL!"	
		
    if eval5 == [2,4,6,10]:
		print "             5  : " + str(eval5)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             5  : " + str(eval5) +  "    --> FAIL!"	
	
	
    if eval6 == [5,7]:
		print "             6  : " + str(eval6)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             6  : " + str(eval6) +  "    --> FAIL!"	
	
    if eval7 == [7,9,12,13]:
		print "             7  : " + str(eval7)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             7  : " + str(eval7) +  "    --> FAIL!"	

    if eval8 == [2,4,6,10]:
		print "             8  : " + str(eval8)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             8  : " + str(eval8) +  "    --> FAIL!"	
		
    if eval9 ==[1,3,5,10]:
		print "             9  : " + str(eval9)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             9  : " + str(eval9) +  "    --> FAIL!"	
	
    if eval10 ==[2,4,6,10]:
		print "             10 : " + str(eval10)+  "    --> OK!"
		test_ok=test_ok+1
    else:
		print "             10 : " + str(eval10) +  "    --> FAIL!"

    print "\n                   Test Passed : " + str(test_ok) + " / 10 \n"
	
   
	
if __name__ == '__main__':
    main()